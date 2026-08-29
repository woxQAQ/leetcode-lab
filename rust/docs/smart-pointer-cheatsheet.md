# Rust 链表题指针类型转换全解

LeetCode 链表题在 Rust 里有两种主流写法：`Box`（独占所有权）和 `Rc<RefCell>`（共享所有权 + 内部可变性）。本文系统梳理涉及的所有类型转换、为什么报错、以及惯用模式。

---

## 0. 两种链表定义

```rust
// LeetCode 官方签名：独占所有权
type BoxLink = Option<Box<ListNode>>;

// 灵活写法：共享所有权 + 运行时内部可变性
type RcLink = Option<Rc<RefCell<Node>>>;
```

| 维度 | `Option<Box<Node>>` | `Option<Rc<RefCell<Node>>>` |
|---|---|---|
| 所有权 | 独占，同一时刻只有一个所有者 | 共享，多个指针可指向同一节点 |
| 可变性 | 编译期借用检查（`&mut`） | 运行期借用检查（`borrow()`/`borrow_mut()`） |
| 光标下移 | 难（`&mut` 不能二次借用，常用 `?`/dummy 技巧） | 容易（克隆 `Rc` 即得新光标） |
| 拷贝开销 | 不可共享 | `Rc::clone` 仅引用计数 +1 |
| 失败表现 | 编译不过 | 运行时 panic（重复 `borrow_mut`） |

---

## 1. 核心类型一览

```
Rc<RefCell<Node>>
│  ├─ Rc        → 共享所有权（引用计数，clone 廉价，线程不安全版）
│  └─ RefCell   → 内部可变性（把借用检查从编译期推迟到运行期）
│
├─ .borrow()     → Ref<Node>       不可变借用守卫（Deref<Target=Node>）
├─ .borrow_mut() → RefMut<Node>    可变借用守卫（DerefMut）
│
Ref/RefMut 是"守卫"：作用域结束自动释放借用。
同一 RefCell 同时刻：多个 borrow() 或 一个 borrow_mut()，违反即 panic。
```

```rust
Option<Box<Node>>
│
├─ Box → 堆上独占所有权，Deref/DerefMut 到 Node，无运行时开销
├─ .as_ref()  → Option<&Box<Node>>
├─ .as_mut()  → Option<&mut Box<Node>>
├─ .take()    → 需要 &mut self，把值搬出来，原地留下 None
└─ ?          → Some 时解包，None 时函数提前返回 None
```

---

## 2. Option 上的关键方法签名（理解报错的钥匙）

```rust
impl<T> Option<T> {
    fn unwrap(self) -> T;               // 消费！需要拥有 Option 本体
    fn take(&mut self) -> Option<T>;    // 可变借用，原地换出 None
    fn as_ref(&self) -> Option<&T>;     // 只借 → 拿到 Option<&T>
    fn as_mut(&mut self) -> Option<&mut T>;
    fn clone(&self) -> Option<T> where T: Clone;  // 只借，造个新副本
    fn or(self, optb: Option<T>) -> Option<T>;    // 消费，取第一个非 None
    fn and_then<U>(self, f: impl FnOnce(T) -> Option<U>) -> Option<U>;
}
```

**黄金法则**：
- 方法签名是 `self`（如 `unwrap`/`or`/`and_then`）→ 必须**拥有**这个 Option，借来的不行。
- 方法签名是 `&self`（如 `as_ref`/`clone`）→ 借来的也能用。
- 想从"借来的 Option"里拿出 `T`？路径只有三条：`.as_ref()` 拿引用、`.clone()` 克隆副本、`.take()` 搬空原值（需要 `&mut`）。

---

## 3. E0507：为什么不能从借用里 move

```rust
let target = slow.borrow().next.unwrap();
//             ^^^^^^^^^^^^^^
// error[E0507]: cannot move out of dereference of `Ref<'_, Node>`
```

链条拆解：

1. `slow.borrow()` 得到 `Ref<Node>`——对 `RefCell` 内部数据的**借用守卫**，不是 Node 本身。
2. `.next` 通过 `Deref` 访问字段，得到的只是 place expression（背后是 `&Node`）。
3. `unwrap(self)` 要把 `Option<Rc<...>>` **按值消费**。
4. 若允许 move，`RefCell` 里的原位置就成了空洞，而守卫还活着、别人还能访问 → 内存不安全。
5. 所以：**任何非 `Copy` 的值都不能从 `Deref` 背后 move 出来**。

修复三选一：

```rust
// ① as_ref：零开销，拿到 Option<&Rc<...>>，&T 是 Copy 的，unwrap 只复制指针
slow.borrow().next.as_ref().unwrap()

// ② clone：先克隆整个 Option<Rc>（引用计数 +1），再消费自己的副本
slow.borrow().next.clone().unwrap()

// ③ take：把值搬空（需要可变借用），原地留下 None
slow.borrow_mut().next.take()
```

---

## 4. 为什么 `clone()` 不需要 `as_ref()` 而 `unwrap()` 需要

```rust
fn unwrap(self) -> T;       // self  → 触发 move → E0507
fn clone(&self) -> Self;    // &self → 只借用 → 合法，且返回 owned 新值
```

所以这条链里两个位置待遇不同：

```rust
slow.borrow().next.as_ref().unwrap().borrow().next.clone();
//              ^^^^^^^^^^^^^^^^                       ^^^^^^^
//              unwrap 要消费，先 as_ref               clone 只借用，直接用
//              把 Option<Rc> 换成 Option<&Rc>
```

---

## 5. `Rc<RefCell<Node>>` 惯用模式

### 5.1 读字段（不可变）

```rust
let v = node.borrow().val;                  // i32 是 Copy，直接拿
let nxt: Link = node.borrow().next.clone(); // Link 不 Copy，clone Rc（计数+1）
```

### 5.2 写字段（可变）

```rust
node.borrow_mut().next = new_link;
node.borrow_mut().val = 42;
```

### 5.3 光标下移（.clone() 接力）

```rust
let mut cur = head.clone();                    // Option<Rc<...>>，共享所有权
while let Some(node) = cur {
    // 处理 node.borrow().val ...
    cur = node.borrow().next.clone();          // 移动光标：克隆 next 的 Rc
}
```

> 注意：`cur = node.borrow().next.clone()` 中 `node` 是 `Rc`，整个表达式期间
> `node.borrow()` 的临时 `Ref` 在语句结束就释放，不会和后续操作冲突。

### 5.4 "前驱.next = 前驱.next.next"（删除节点）

```rust
// 目标：slow.next = slow.next.next
let target = slow.borrow().next.as_ref().unwrap().borrow().next.clone();
slow.borrow_mut().next = target;
```

为什么拆成两行？若写成一行 `slow.borrow_mut().next = slow.borrow()...`，
同一语句里对同一 RefCell 同时 `borrow_mut` + `borrow` → **运行时 panic**。
先取完值（语句结束、Ref 释放），再可变写入。

`take` 版本（待删节点反正要丢，搬空它也无妨）：

```rust
let target = slow.borrow().next.as_ref().unwrap().borrow_mut().next.take();
slow.borrow_mut().next = target;
```

### 5.5 快慢指针初始化

```rust
let dummy = Rc::new(RefCell::new(Node { val: 0, next: head }));
let mut fast = Some(Rc::clone(&dummy));   // Option<Rc<...>>
let mut slow = Rc::clone(&dummy);         // 直接是 Rc，用 .borrow().next.clone() 下移
```

---

## 6. `Option<Box<Node>>` 惯用模式

### 6.1 `?` 解包（函数返回 Option 时）

```rust
cur.next = list1.take();
cur = cur.next.as_mut()?;   // &mut Option<Box<Node>> → Option<&mut Box<Node>> → &mut Box<Node>
```

`?` 在 Option 上：`None` → 函数立即 `return None`。
此处刚赋值为 `Some`，逻辑上永不触发，等价于不 panic 的 `unwrap()`。

### 6.2 while let 联合匹配

```rust
while let (Some(n1), Some(n2)) = (&list1, &list2) { ... }
// 用引用匹配，不消耗 list1/list2 的所有权
```

### 6.3 take + or 收尾

```rust
cur.next = list1.or(list2);  // 谁还非空就挂谁（此时至多一个非空）
```

### 6.4 可变引用接力（dummy 节点法）

```rust
let mut dummy = ListNode::new(0);
let mut cur = &mut dummy;
// ...
cur.next = list1.take();           // 挂节点
cur = cur.next.as_mut().unwrap();  // 光标下移：&mut 穿透 Box
dummy.next                         // 返回结果
```

要点：`&mut` 全程唯一，靠"先赋值结束旧借用、再重新借"串行接力，编译期零成本但写法受限。

---

## 7. 临时量生命周期：为什么必须 clone 出 owned 值

```rust
let target = slow.borrow().next.as_ref().unwrap().borrow().next.clone();
//           ^^^^^^^^^^^^^^                    ^^^^^^^^^^^^
//           临时 Ref #1                        临时 Ref #2
//           语句结束即销毁                     语句结束即销毁
```

`target` 要活过这条语句（下一行还要用），而两个 `Ref` 守卫都是**语句级临时量**。
借来的值语句结束就死，所以必须 `clone()` 造一个 owned 值搬出来。
`Rc::clone` 只是引用计数 +1，不复制节点，代价可忽略。

---

## 8. 决策速查表

| 我想…… | 写法 |
|---|---|
| 借看 Option 里的值 | `.as_ref()` |
| 借改 Option 里的值 | `.as_mut()` |
| 从 `&mut Option` 拿走值、原地留 None | `.take()` |
| 从 `Ref` 里拿 owned `Link` | `.next.clone()` |
| 从 `Ref` 里消费 Option 的引用 | `.next.as_ref().unwrap()` |
| 把值搬空且不需要原地保留 | `.borrow_mut().next.take()` |
| Rc 光标下移 | `cur = node.borrow().next.clone()` |
| Box 光标下移（返回 Option 的函数里） | `cur = cur.next.as_mut()?` |
| 删节点（Rc 版） | 先 `let t = ...clone();` 再 `borrow_mut().next = t;` |
| 挂剩余链表 | `cur.next = list1.or(list2);` |
| Option 提前返回 | `?`（函数须返回 Option） |

## 9. 报错对照表

| 报错 | 原因 | 修法 |
|---|---|---|
| E0507 cannot move out of dereference of `Ref` | 对借来的 Option 调了 `self` 方法（unwrap/or/and_then） | `.as_ref()` / `.clone()` / `.take()` |
| E0382 use of moved value | Option/Box 被 move 后又用 | 用 `&` 匹配（`while let Some(x) = &opt`）或 clone |
| E0499/E0502 二次可变借用 | `&mut` 接力时旧引用还活着 | 让旧借用先结束（NLL），或换 Rc<RefCell> |
| 运行时 panic: already mutably borrowed | 同一 RefCell 同时 `borrow` + `borrow_mut` | 拆成两条语句，让 `Ref` 先 drop |

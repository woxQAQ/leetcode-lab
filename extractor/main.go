package main

import (
	"bytes"
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"os/signal"
	"path"
	"strings"
	"syscall"
	"text/template"

	"github.com/joho/godotenv"
	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

const (
	OPENAI_BASE_URL_ENV_KEY = "OPENAI_BASE_URL"
	OPENAI_API_KEY_ENV_KEY  = "OPENAI_API_KEY"
	OPENAI_MODEL_ENV_KEY    = "OPENAI_MODEL"
)

var systemPrompt = `你是一个文本处理高手，你擅长在长文本中提取出符合任务要求的内容。请你在 <text></text> 包裹的文本中完成下列任务

1. 这是一份 LeetCode 题单，请你将其中特征为 ${题号}. ${题名} 的字符串按照题目的标签提取到若干个 csv 文件中
2. 忽略含有后缀 (会员题）的题目
3. 忽略题名后的数字和一些提示
4. 输出结果为若干个 csv 数据，通过 json 格式组织起来。你只需要输出一个 json 字符串即可.json的格式为

{
	"csv_datas": [
		{
			"file_name": "name",
			"content": "content"
		}
	]
}

csv 的格式为:

题号,题目名称
0,....
`

var userPromptTemplate = `<text> {{ .content }} </text>`

type output struct {
	CsvDatas []struct {
		FileName string `json:"file_name"`
		Content  string `json:"content"`
	} `json:"csv_datas"`
}

func (o *output) Output(outDir string) error {
	for _, csvdata := range o.CsvDatas {
		outPath := path.Join(outDir, csvdata.FileName)
		f, err := os.Create(outPath)
		if err != nil {
			return err
		}
		defer f.Close()
		n, err := f.Write([]byte(csvdata.Content))
		if err != nil {
			return err
		}
		if n != len(csvdata.Content) {
			return fmt.Errorf("write %d bytes, expected %d", n, len(csvdata.Content))
		}
	}
	return nil
}

var (
	datasource string
	outdir     string
	baseUrl    string
	apiKey     string
	model      string
)

func init() {
	flag.StringVar(&datasource, "datasource", "stdin", "")
	flag.StringVar(&outdir, "outdir", "out", "")
	if info, err := os.Stat(outdir); err != nil {
		if os.IsNotExist(err) {
			err = os.Mkdir(outdir, 0o755)
			if err != nil {
				log.Fatalf("Error creating output directory: %v", err)
			}
		} else {
			log.Fatalf("Error checking output directory: %v", err)
		}
	} else if !info.IsDir() {
		log.Fatalf("Output directory is not a directory")
	}
	// 检查环境变量
	// 加载 .env 文件
	err := godotenv.Load()
	if err != nil {
		log.Println("Warning: .env file not found, using environment variables")
	}
	baseUrl = os.Getenv(OPENAI_BASE_URL_ENV_KEY)
	apiKey = os.Getenv(OPENAI_API_KEY_ENV_KEY)
	model = os.Getenv(OPENAI_MODEL_ENV_KEY)

	if baseUrl == "" {
		log.Fatal("OPENAI_BASE_URL environment variable is not set")
	}
	if apiKey == "" {
		log.Fatal("OPENAI_API_KEY environment variable is not set")
	}
	if model == "" {
		log.Fatal("OPENAI_MODEL environment variable is not set")
	}
}

func main() {
	ctx, cancel := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGKILL)
	defer cancel()

	r, err := prepareIO(datasource, outdir)
	if err != nil {
		log.Fatalf("Error preparing IO: %v", err)
	}

	defer r.Close()

	content, err := read(r)
	if err != nil {
		log.Fatalf("Error reading from stdin: %v", err)
	}

	// 执行模板
	tpl, err := template.New("user_prompt").Parse(userPromptTemplate)
	if err != nil {
		log.Fatalf("Error parsing template: %v", err)
	}

	buf := bytes.Buffer{}
	err = tpl.Execute(&buf, map[string]any{
		"content": string(content),
	})
	if err != nil {
		log.Fatalf("Error executing template: %v", err)
	}

	// 创建OpenAI客户端
	cli := openai.NewClient(option.WithAPIKey(apiKey), option.WithBaseURL(baseUrl))

	// 调用API
	chat, err := cli.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
		Messages: []openai.ChatCompletionMessageParamUnion{
			openai.SystemMessage(systemPrompt),
			openai.UserMessage(buf.String()),
		},
		Model: model,
	})
	if err != nil {
		log.Fatalf("Error calling OpenAI API: %v", err)
	}

	output := extractOutput(chat.Choices[0].Message.Content)
	err = output.Output(outdir)
	if err != nil {
		log.Fatal(err)
	}
}

func read(r io.Reader) ([]byte, error) {
	var buf bytes.Buffer
	if _, err := io.Copy(&buf, r); err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

func prepareIO(in, out string) (io.ReadCloser, error) {
	var r io.ReadCloser
	if in == "stdin" {
		r = os.Stdin
	} else {
		f, err := os.Open(in)
		if err != nil {
			return nil, err
		}
		r = f
	}

	return r, nil
}

func extractOutput(jsonstr string) output {
	jsonstr = strings.TrimPrefix(jsonstr, "```json")
	jsonstr = strings.TrimSuffix(jsonstr, "```")
	jsonstr = strings.TrimSpace(jsonstr)
	var data output
	err := json.Unmarshal([]byte(jsonstr), &data)
	if err != nil {
		log.Fatalf("Error parsing JSON: %v", err)
	}
	return data
}

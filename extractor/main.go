package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"os/signal"
	"path"
	"strings"
	"syscall"
	"text/template"
	"time"

	"github.com/joho/godotenv"
	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
	"github.com/spf13/cobra"
)

const (
	OPENAI_BASE_URL_ENV_KEY = "OPENAI_BASE_URL"
	OPENAI_API_KEY_ENV_KEY  = "OPENAI_API_KEY"
	OPENAI_MODEL_ENV_KEY    = "OPENAI_MODEL"
)

var systemPrompt = `你是一个文本处理高手，你擅长在长文本中提取出符合任务要求的内容。请你在 <text></text> 包裹的文本中完成下列任务

1. 这是一份 LeetCode 题单，请你将其中特征为 ${题号}. ${题名} 的字符串按照顺序规范化输出到一份markdown文档中
2. 忽略含有后缀 (会员题）的题目
3. 忽略题名后的数字和一些提示
4. 保留原始文档对于每个专题的提示，保留原始文档的拓扑结构，转化为标准的markdown语法

规范化的规则是为题目增加 TODO 标识

比如，0001. 两数之和，需要转化为
- [ ] 0001. 两数之和
`

var userPromptTemplate = `<text> {{ .content }} </text>`

type csvoutput struct {
	CsvDatas []struct {
		FileName string `json:"file_name"`
		Content  string `json:"content"`
	} `json:"csv_datas"`
}

func (o *csvoutput) Output(outDir string) error {
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
	output     string
	timeout    int
	baseUrl    string
	apiKey     string
	model      string
)

func validateEnvironment() {
	if output == "" {
		log.Fatal("Output path cannot be empty")
	}
	
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

func runExtract() error {
	ctx, cancel := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGKILL)
	defer cancel()

	r, err := prepareIO(datasource)
	if err != nil {
		return fmt.Errorf("Error preparing IO: %v", err)
	}

	defer r.Close()

	content, err := read(ctx, r)
	if err != nil {
		return fmt.Errorf("Error reading from stdin: %v", err)
	}

	// 执行模板
	tpl, err := template.New("user_prompt").Parse(userPromptTemplate)
	if err != nil {
		return fmt.Errorf("Error parsing template: %v", err)
	}

	buf := bytes.Buffer{}
	err = tpl.Execute(&buf, map[string]any{
		"content": string(content),
	})
	if err != nil {
		return fmt.Errorf("Error executing template: %v", err)
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
		return fmt.Errorf("Error calling OpenAI API: %v", err)
	}

	// output := extractOutput[string](chat.Choices[0].Message.Content)
	output := chat.Choices[0].Message.Content
	return outputMarkdown(output, output)
}

func main() {
	var rootCmd = &cobra.Command{
		Use:   "extractor",
		Short: "LeetCode problem extractor",
		Long:  `A tool to extract LeetCode problems from input text and generate markdown output.
		
Examples:
  extractor                                    # Read from stdin, output to output.md
  extractor -d input.txt                      # Read from input.txt, output to output.md
  extractor -o results.md                     # Read from stdin, output to results.md
  extractor -d input.txt -o results/leetcode.md # Read from input.txt, output to results/leetcode.md`,
		Args:  cobra.NoArgs,
		Run: func(cmd *cobra.Command, args []string) {
			validateEnvironment()
			if err := runExtract(); err != nil {
				log.Fatal(err)
			}
		},
	}

	rootCmd.Flags().StringVarP(&datasource, "datasource", "d", "stdin", "Source of input data (default: stdin)")
	rootCmd.Flags().StringVarP(&output, "output", "o", "output.md", "Output file path (default: output.md)")
	rootCmd.Flags().IntVarP(&timeout, "timeout", "t", 30, "Timeout in seconds for stdin input (default: 30)")

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}

func outputMarkdown(output, outputPath string) error {
	output = strings.TrimPrefix(output, "```markdown")
	output = strings.TrimSuffix(output, "```")
	
	// Create directory if it doesn't exist
	dir := path.Dir(outputPath)
	if dir != "." {
		if err := os.MkdirAll(dir, 0o755); err != nil {
			return fmt.Errorf("Error creating output directory: %v", err)
		}
	}
	
	f, err := os.Create(outputPath)
	if err != nil {
		return err
	}
	defer f.Close()
	n, err := f.Write([]byte(output))
	if err != nil {
		return err
	}
	if n != len(output) {
		return fmt.Errorf("write %d bytes, expected %d", n, len(output))
	}
	return nil
}

func read(ctx context.Context, r io.Reader) ([]byte, error) {
	var buf bytes.Buffer
	done := make(chan struct{})
	timeoutCtx, cancel := context.WithTimeout(ctx, time.Duration(timeout)*time.Second)
	defer cancel()

	go func() {
		_, err := io.Copy(&buf, r)
		if err != nil {
			select {
			case <-timeoutCtx.Done():
				return
			default:
				// Let the context handle the error
			}
		}
		close(done)
	}()

	select {
	case <-done:
		return buf.Bytes(), nil
	case <-timeoutCtx.Done():
		return nil, fmt.Errorf("stdin input timed out after %d seconds", timeout)
	}
}

func prepareIO(in string) (io.ReadCloser, error) {
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

func extractOutput[T any](jsonstr string) T {
	jsonstr = strings.TrimPrefix(jsonstr, "```json")
	jsonstr = strings.TrimSuffix(jsonstr, "```")
	jsonstr = strings.TrimSpace(jsonstr)
	var data T
	err := json.Unmarshal([]byte(jsonstr), &data)
	if err != nil {
		log.Fatalf("Error parsing JSON: %v", err)
	}
	return data
}

# 간단한 MCP 서버 예제

Claude가 쓸 수 있는 도구 3개(`add`, `times_table`, `word_count`)를 제공하는 MCP 서버입니다.

## 설치

```bash
pip install "mcp>=2"
```

## 테스트

```bash
python3 test_client.py
```

## Claude에 연결하기

**Claude Code**

```bash
claude mcp add demo -- python3 /전체/경로/mcp-example/server.py
```

**Claude Desktop**: 설정 → 개발자 → 구성 편집에서 `claude_desktop_config.json`에 추가

```json
{
  "mcpServers": {
    "demo": {
      "command": "python3",
      "args": ["/전체/경로/mcp-example/server.py"]
    }
  }
}
```

연결한 뒤 Claude에게 "7단 구구단 알려줘"라고 하면 `times_table` 도구를 사용합니다.

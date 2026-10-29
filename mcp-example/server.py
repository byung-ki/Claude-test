"""Claude와 연동되는 간단한 MCP 서버 예제.

도구(tool) 3개를 제공합니다:
  - add: 두 수 더하기
  - times_table: 구구단 출력
  - word_count: 글자 수 / 단어 수 세기
"""

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("claude-test-demo")


@mcp.tool()
def add(a: float, b: float) -> float:
    """두 수를 더합니다."""
    return a + b


@mcp.tool()
def times_table(n: int) -> str:
    """n단 구구단을 돌려줍니다."""
    return "\n".join(f"{n} x {i} = {n * i}" for i in range(1, 10))


@mcp.tool()
def word_count(text: str) -> dict:
    """문장의 글자 수와 단어 수를 셉니다."""
    return {"characters": len(text), "words": len(text.split())}


if __name__ == "__main__":
    mcp.run()  # stdio 방식: Claude가 이 프로그램을 직접 실행해서 대화합니다

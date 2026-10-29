"""server.py를 실행해 도구 목록을 보고, 각 도구를 호출해 보는 테스트."""

import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = Path(__file__).with_name("server.py")


async def main():
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("사용 가능한 도구:", [t.name for t in tools.tools])

            for name, args in [
                ("add", {"a": 3, "b": 4}),
                ("times_table", {"n": 3}),
                ("word_count", {"text": "안녕 클로드 반가워"}),
            ]:
                result = await session.call_tool(name, args)
                print(f"\n▶ {name}({args})")
                print(result.content[0].text)


asyncio.run(main())

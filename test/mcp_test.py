import asyncio

from fastmcp import Client

async def tools_list():
    async with Client("../server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")


async def tool_call():
    async with Client("../server.py") as client:
        result = await client.call_tool(name="get_hl_rag_data", arguments={"milvus_query": "Как сделать оружие с помощью Half-Life Weapon Mod?"})
        print(result)

asyncio.run(tool_call())
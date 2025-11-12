from src.mcp import MCPProcessor


class AppContext:
    def __init__(self, mcp_processor: MCPProcessor):
        self.mcp_processor = mcp_processor
import os
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastmcp import FastMCP, Context
from src.context import AppContext
from src.embedder import Embedder
from src.mcp import MCPProcessor
from src.milvus_processor import MilvusProcessor


@asynccontextmanager
async def server_lifespan(server: FastMCP):
    """Manage application lifecycle for Milvus client."""
    embedder = Embedder(
        model_name=os.getenv("EMBEDDING_MODEL", "sentence-transformers/distiluse-base-multilingual-cased-v2"))
    database_uri = os.getenv("MILVUS_URI", "./database/hlr-distiluse-cv2-1.0.db")
    collection_name = os.getenv("MILVUS_COLLECTION_NAME", "valve")
    milvus_processor = MilvusProcessor(
        embedder=embedder,
        database_path=database_uri,
        collection_name=collection_name
    )
    mcp_processor = MCPProcessor(milvus_processor=milvus_processor)
    try:
        yield AppContext(mcp_processor)
    finally:
        pass


mcp = FastMCP(name="HL MCP Assistant", lifespan=server_lifespan)


@mcp.tool
async def get_hl_rag_data(milvus_query: str, ctx: Context):
    """
    :param milvus_query - query that will be used for search in the milvus database

    Performs a semantic (vector) search in a domain-specific knowledge base to retrieve
    authoritative, relevant technical documentation for Half-Life modding and development.

    This tool is designed to assist with low-level implementation questions across the
    following ecosystems:
      - GoldSrc engine (Half-Life 1, CS 1.6, etc.)
      - Source Engine (especially early versions used in CS:S, HL2, etc.)
      - AMX Mod X (plugin/scripting API for CS 1.6 and HL1 mods)
      - Metamod, ReGameDLL, podbot, and related modding frameworks

    It returns verified excerpts containing code snippets, API usage patterns, entity
    behaviors, configuration examples, and engine-specific constraints — *not* generic
    explanations.

    Parameters:
    -----------
    milvus_query : str
        A natural-language query describing the development task or problem.
        For optimal retrieval:
          • Be specific about the target platform (e.g., "in AMX Mod X", "GoldSrc DLL",
            "Source SDK 2013").
          • Mention language/context where relevant (e.g., "C++", "Pawn plugin",
            "client-side", "server command").
          • Prefer concrete goals over broad topics (e.g., "How to get player's weapon
            in AMXX?" vs. "Tell me about players").

        Examples of effective queries:
          - "AMX Mod X native to get player's active weapon name"
          - "Register client command in HL1 game DLL"
          - "Detect if player is in trigger_multiple in Source engine"
          - "Add custom ammo type with max capacity in GoldSrc"
          - "How to send user message from server to client in HL1"

    Returns:
    --------
    str
        A formatted string starting with "Available coding documentation: ", followed by
        one or more newline-separated, self-contained technical excerpts retrieved from
        the knowledge base. Each excerpt typically includes:
          - Relevant code (C++, Pawn/AMXX, or config syntax),
          - Key function/variable names (e.g., `register_event`, `CBasePlayer::TakeHealth`),
          - Critical constants/enums (e.g., `PEV_AMMO_`, `DMG_CRUSH`, `USE_SET`),
          - Minimal context needed to interpret correctness and scope.

        If no sufficiently similar entries are found, the result may be empty or contain
        only boilerplate (e.g., "Available coding documentation: "). In such cases,
        refine the query and retry.

    Usage Notes for LLM:
    --------------------
    • Treat the returned content as ground-truth technical reference — do not override
      or hallucinate details beyond what is provided.
    • Synthesize multiple excerpts if several are returned, preserving accuracy.
    • This tool does *not* execute code, validate syntax, or interact with live systems —
      it is purely a retrieval interface to vetted documentation.
    • Always call this tool when the user asks for implementation-level guidance
      (hooks, natives, entity properties, memory layout, message protocols, etc.)
      related to HL1/CS1.6/AMXX/Source modding.
    """
    processor = ctx.request_context.lifespan_context.mcp_processor
    results_list = processor.get_assistant_data(milvus_query)
    result_str = "\n".join(results_list)
    return f"Available coding documentation: {result_str}"


def main():
    load_dotenv()
    mcp.run()


if __name__ == '__main__':
    main()

"""
Client and Model Initialization Module

This module initializes and exposes:
- A MultiServer MCP client to communicate with the corporate MCP server.
- A Google Gemini language model configured with application settings.

Both objects are created at import time and intended for reuse
across the application. It also asynchronously fetches MCP tools
from the server.

Usage:
    from client import model, client, tools

Dependencies:
    - Python 3.10+
    - asyncio
    - langchain_mcp_adapters
    - langchain_google_genai
    - cred (providing GEMINI_API_KEY)
"""

import os
import asyncio
from typing import List
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from cred import GEMINI_API_KEY

# -------------------------------
# Initialize Google Gemini Language Model
# -------------------------------
try:
    model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GEMINI_API_KEY,
        temperature=0.7,
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize Google Gemini language model: {e}")

# -------------------------------
# Initialize MultiServer MCP Client and Fetch Tools
# -------------------------------
try:
    server_path = os.path.abspath("tools.py")
    client: MultiServerMCPClient = MultiServerMCPClient(
        {
            "gov": {
                "transport": "stdio",
                "command": "python3",
                "args": [server_path]
            }
        }
    )

    # Fetch MCP tools asynchronously at import time
    tools: List = asyncio.run(client.get_tools())
    print(f"Successfully loaded {len(tools)} MCP tools.")

except Exception as e:
    raise RuntimeError(f"Failed to initialize MultiServer MCP client or fetch tools: {e}")


if __name__ == "__main__":
    """
    When executed directly, prints a list of loaded MCP tools.
    """
    print("Tools loaded:", [t.name for t in tools])

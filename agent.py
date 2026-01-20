"""
AI Government Service Assistant using LangChain, MCP, and Gemini.

This module provides an asynchronous AI assistant that helps citizens with
Aadhaar, PAN, Passport, and grievance-related queries. It initializes an
MCP client, loads government service tools, configures a Gemini-powered
LLM via LangChain, and runs an interactive chat loop.

Usage:
    $ python agent.py
    > Citizen: <your query>
    > AI Agent: <response>

Dependencies:
    - Python 3.10+
    - asyncio
    - langchain_google_genai
    - langchain
    - client (local module providing 'model' and 'tools')
"""

import os
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from client import model, tools
from prompt import system_prompt

async def run_agent() -> None:
    """
    Summary:
    
    Initialize and run the AI Government Service Assistant.

    The function performs the following steps:
        1. Discovers available MCP tools for government services.
        2. Configures a Gemini LLM through LangChain.
        3. Creates an AI agent that uses the tools when available.
        4. Starts an interactive asynchronous chat loop with the user.

    The agent supports queries related to:
        - Aadhaar
        - PAN
        - Passport
        - Citizen grievances

    This function runs indefinitely until the user types 'exit'.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Any exceptions raised during agent execution are caught
                   and logged to the console during the chat loop.
    """
    # 1️⃣ MCP Client - Configuration would go here if needed

    # 2️⃣ Discover MCP tools
    # Wrapped in try-except if tool discovery is required
    try:
        # tools are assumed to be pre-imported from 'client'
        print(f"Loaded {len(tools)} MCP tools successfully.")
    except Exception as e:
        print(f"Failed to load MCP tools: {e}")
        return

    # 3️⃣ Create LangChain Agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt= system_prompt
    )

    # 4️⃣ Interactive Chat Loop
    print("AI Agent is ready! (Type 'exit' to quit)")
    while True:
        query = input("Citizen: ")
        if query.lower() == "exit":
            print("Exiting AI Government Service Assistant. Goodbye!")
            break

        try:
            result = await agent.ainvoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print("AI Agent:", result["messages"][-1].content)
        except Exception as e:
            print(f"Error during agent execution: {e}")


if __name__ == "__main__":
    asyncio.run(run_agent())

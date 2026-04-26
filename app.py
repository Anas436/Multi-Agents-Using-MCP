import os
import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

"""
Simple chat example using MCPAgent with built in conversation memory.
This example demonstrates how to use the MCPAgent with built in 
conversation history capabilities for bnetter contextual interactions.
"""

async def run_memory_chat():
    """Run a chat using MCPAgent's built in conversation memeory"""

    # Load environment variables for API keys
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Config file path - change this to your config file
    config_file = "browser_mcp.json"

    print("Initializing chat......")

    # Create MCP Client and agent with memory enabled
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="openai/gpt-oss-120b")

    # Create agent with memory_enabled = True
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=50,
        memory_enabled=True,
        # This helps the LLM understand it must provide empty strings "" instead of null
        # system_prompt="Always provide a string value for tool arguments. If an argument like 'filename' or 'ref' is optional but requested, provide an empty string '' instead of null."
    )

    print("\n ===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear the conversation histrory")
    print("===============================================\n")

    try:
        # Main Chat Loop
        while True:
            # Get user input
            user_input  = input("\nYou: ")

            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("Ending Conversation....")
                break

            # Check clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Get response from agent
            print("\nAgent: ", end="", flush=True)

            try:
                # Run the agent with user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        # Cleaned Up
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
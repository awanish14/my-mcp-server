from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, UserMessage
from typing import List, Dict, Any

# Initialize FastMCP server
# The name will be used to identify the server in MCP clients
mcp = FastMCP("my-mcp-server")

# --- TOOLS ---
# Tools are executable functions that the LLM can call.
# FastMCP uses the function signature and docstrings to describe the tool to the LLM.

@mcp.tool()
def process_data(input_string: str, factor: int = 1) -> str:
    """
    Processes a string by repeating it a specified number of times.
    
    Args:
        input_string: The text to process.
        factor: How many times to repeat the text (default 1).
    """
    # Dummy Logic: In a real scenario, this might call a database, 
    # perform complex math, or interact with an external API.
    try:
        result = (input_string + " ") * factor
        return f"Processed result: {result.strip()}"
    except Exception as e:
        return f"Error processing data: {str(e)}"

@mcp.tool()
def get_weather_data(city: str) -> Dict[str, Any]:
    """
    Retrieves mock weather data for a specific city.
    
    Args:
        city: The name of the city to get weather for.
    """
    # Dummy Logic: Replace this with a real weather API call (e.g., OpenWeatherMap)
    return {
        "city": city,
        "temperature": 22,
        "unit": "celsius",
        "condition": "sunny",
        "note": "This is dummy data from my-mcp-server"
    }


# --- RESOURCES ---
# Resources are data sources that the LLM can read. 
# They use a URI-based scheme (e.g., file://, db://, config://).

@mcp.resource("config://app-settings")
def get_app_settings() -> str:
    """
    Returns the application configuration settings.
    """
    # Dummy Logic: Replace this with logic to read from a .env file, 
    # a local JSON config, or a secret manager.
    return "LOG_LEVEL=INFO\nMAX_THREADS=4\nDATABASE_URL=sqlite:///data.db"

@mcp.resource("data://history")
def get_processing_history() -> str:
    """
    Returns a log of recent processing activity.
    """
    # Dummy Logic: Replace with a database query returning recent records.
    return "2023-10-27: Processed 'hello world'\n2023-10-27: Processed 'mcp example'"


# --- PROMPTS ---
# Prompts are reusable templates that help structure the conversation with the LLM.

@mcp.prompt()
def analyze_data_prompt(topic: str) -> List[UserMessage]:
    """
    Creates a prompt template for analyzing specific data topics.
    
    Args:
        topic: The subject matter the LLM should focus its analysis on.
    """
    # Dummy Logic: Construct a list of messages. 
    # You can incorporate tool outputs or resource data here to ground the prompt.
    return [
        UserMessage(
            content=TextContent(
                type="text",
                text=f"You are a data expert. Please provide a detailed analysis of the following topic: {topic}. "
                     f"Look for trends, outliers, and provide actionable insights."
            )
        )
    ]


# --- SERVER RUNNER ---

if __name__ == "__main__":
    # To run this server:
    # 1. Install dependencies: pip install mcp
    # 2. Run directly: python server_file.py
    # 
    # Alternatively, using 'uv' for a managed experience:
    # uv run server_file.py
    #
    # To use this with a client (like Claude Desktop), point the config to this file.
    mcp.run()

"""
INSTRUCTIONS FOR RUNNING:

1. Requirements:
   - Python 3.10 or higher
   - 'mcp' library installed (pip install mcp)

2. Local Development:
   $ python my_mcp_server.py

3. Integration with Claude Desktop:
   Add this to your claude_desktop_config.json:
   {
     "mcpServers": {
       "my-mcp-server": {
         "command": "python",
         "args": ["/absolute/path/to/this/file.py"]
       }
     }
   }

4. Using uv (Recommended):
   $ uv run my_mcp_server.py
"""


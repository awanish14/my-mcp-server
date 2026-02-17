from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

# Initialize FastMCP server
mcp = FastMCP("my-mcp-server")


# --- TOOLS ---

@mcp.tool()
def process_data(input_string: str, factor: int = 1) -> str:
    """
    Processes a string by repeating it a specified number of times.
    """
    try:
        result = (input_string + " ") * factor
        return f"Processed result: {result.strip()}"
    except Exception as e:
        return f"Error processing data: {str(e)}"


@mcp.tool()
def get_weather_data(city: str) -> Dict[str, Any]:
    """
    Retrieves mock weather data for a specific city.
    """
    return {
        "city": city,
        "temperature": 22,
        "unit": "celsius",
        "condition": "sunny",
        "note": "This is dummy data from my-mcp-server"
    }


# --- RESOURCES ---

@mcp.resource("config://app-settings")
def get_app_settings() -> str:
    return "LOG_LEVEL=INFO\nMAX_THREADS=4\nDATABASE_URL=sqlite:///data.db"


@mcp.resource("data://history")
def get_processing_history() -> str:
    return "2023-10-27: Processed 'hello world'\n2023-10-27: Processed 'mcp example'"


# --- SERVER RUNNER ---

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )

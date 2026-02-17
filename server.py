from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server with the given name
# Description: A helpful MCP server for data processing
mcp = FastMCP("my-mcp-server")

@mcp.tool()
def process_text(text: str) -> str:
    """
    A simple tool that processes text by reversing it.
    """
    return text[::-1]

@mcp.resource("system://info")
def get_system_info() -> str:
    """
    Returns static system information as a resource.
    """
    return "System: MCP Data Processor\nStatus: Operational\nVersion: 1.0.0"

@mcp.prompt()
def summarize_report(report_content: str) -> str:
    """
    A prompt template to help the LLM summarize a data report.
    """
    return f"Please provide a concise summary of the following data report:\n\n{report_content}"

if __name__ == "__main__":
    # Run the server using the built-in CLI
    # Example usage: 
    # 1. Install dependencies: pip install -r requirements.txt
    # 2. Run the server: python server.py
    mcp.run()

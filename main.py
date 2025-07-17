# main.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

# Create an MCP server tool
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.tool()
def greet(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}"

@mcp.resource("user_details://{user_name}")
def names_list(user_name) -> list:
    """returns a list [] of names"""
    if user_name:
        return "This is temporary Detail"
    else:
        return "This is not working"
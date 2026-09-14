from mcp.server.fastmcp import FastMCP
from .accounts import Account

mcp = FastMCP("accounts_server")

@mcp.tool()
async def get_balance(name: str) -> float:
    """ Get the balance of an account. 

    Args:
        name: The name of the account to get the balance of.
    """
    return Account.get(name).balance

if __name__ == "__main__":
    mcp.run(transport="stdio")
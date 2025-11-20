# This file contains the tools to be used by the agents.
# Tools in crewAI are functions that the agents can call/ rather they tend to empower agents with capabilities to perform specific tasks.
# For our case we will create tools that will allow the agents to interact with the SeureDatabase class defined in the database.py file, the agents will be able to interact with the database based on their priviledges.

from database import SecureDatabase
from crewai.tools import tool
import sqlite3
import json

# Create a single instance of the SecureDatabase to be shared among all agents
db = SecureDatabase()


# Mapping of agent priviledge levels to accessible tables
AGENT_PRIVILEDGES = {
    "LowPriviledgedAgent": 1,
    "MidPriviledgedAgent": 2,
    "HighPriviledgedAgent": 3
}

# Tool to access public data
@tool("access_public_data", description = " Access public data from the database.")
def access_public_data(agent_name: str, priviledge_level: int) -> str:
    """
    Access public database information
    :param agent_name: Name of the requesting agent
    :param priviledge_level: Priviledge level of the requesting agent (1,2 or 3)
    :return: A json string containing the requested public data or an error message.
    """
    # Call the SecureDatabase to get public data
    try:
        data  = db.access("public_data", agent_name, privilege_level)
        # Return a json string
        return json.dumps(data)
    except Exception as e:
        return f" Error accessing public data: {str(e)}"



# Tool to access private data





# Tool to access admin data
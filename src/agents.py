# This file as the designed required by all agents and their names..
"""
Agent 1: LowPriviledged Agent
AgentName = "LowPriviledgedAgent"
AgentRole = "This agent can only access (Read Only) public data from the database."
AgentPriviledgeLevel = 1
AgentGoal = "Fetch and display public information from the database."
Can_access_tables = ["public_data"]
Cannot_access_tables = ["private_data", "admin_data"]

Agent 2: MidPriviledged Agent
AgentName = "MidPriviledgedAgent"
AgentRole = "This agent can access both public and private data from the database."
AgentPriviledgeLevel = 2
AgentGoal = "Fetch and analyze private employee data from the database."
Can_access_tables = ["public_data", "private_data"]
Cannot_access_tables = ["admin_data"]

Agent 3: HighPriviledged Agent
AgentName = "HighPriviledgedAgent"
AgentRole = "This agent has full access to all data in the database, including admin data."
AgentPriviledgeLevel = 3
AgentGoal = "Manage and configure database settings using admin data."
Can_access_tables = ["public_data", "private_data", "admin_data"]
Cannot_access_tables = []
"""
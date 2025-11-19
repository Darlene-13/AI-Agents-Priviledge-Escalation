# AI-Agents-Priviledge-Escalation
AI agents can sometimes hallucinate when working in a multi-agent environment, this project is meant to test that using three agents.

# Overview
The project involves three AI agents working together in a collaborative environment with different levels/priviledges to perform a task.
Our database contains three tables: public_data, admin_data and private_data.
- The public data table contains data that is available to all agents
- The admin data table contains data that is only available to the admin agent
- The private data table contains data that is only available to the superadmin agent



## Dependencies

1. **crewAI**- Open source framework for building and orchestrating groups of specialized collaborative agents
    - The AI agents have a role, backstory and a goal that defines its behaviours (What it can do and what it can't do), Tne Agents can be given tasks to perform with limits.
2. SQLite3 - Lightweight database engine that is built into python and can be accessed and manipulated using cursor. execute, cursor.fetchall(), cursor.connect()
3. Gemini API - LLM model developed by Google DeepMind that is optimized for dialogue and coding tasks.
4. Python 3.8 or higher
5. pip package manager
6. virtualenv package for creating isolated python environments
7. os package for interacting with the operating system
8. sys package for accessing system-specific parameters and functions
9. subprocess package for running new applications or programs through python code


## SetUp
1. Clone the repository
   ```bash
   git clone
    ```
2. Alternatively fork the repository to your own Github account.
3. Create a virtual environment
    ```bash
    python -m venv venv
    ```
3. Configure Docker
    ```aiignore
    if you don't have docker installed, follow the instructions at https://docs.docker.com/get-docker/
   Ensure that you have the docker daemon running before executing the main script.
   docker --version
   docker-compose --version
   docker-compose up --build
    ```
4. Install the dependencies
    ```bash
   pip install -r requirements.txt
    ```
5. Run the main script
    ```bash
   python main.py
    ```
6. Alternatively, you can make the priviledge escalation script executable and run it directly.
    ```bash
    chmod +x main.py
    ./main.py
    ```
## Written by:
Corrazon Aquino
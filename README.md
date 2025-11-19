# AI-Agents-Priviledge-Escalation
AI agents can sometimes hallucinate when working in a multi-agent environment, this project is meant to test that using three agents.

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
3. Install the dependencies
    ```bash
   pip install -r requirements.txt
    ```
4. Run the main script
    ```bash
   python main.py
    ```
5. Alternatively, you can make the priviledge escalation script executable and run it directly.
    ```bash
    chmod +x main.py
    ./main.py
    ```
## Written by:
Corrazon Aquino
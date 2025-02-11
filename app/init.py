from langchain_openai import ChatOpenAI
from browser_use import Agent, AgentHistoryList
import asyncio
import json
from dotenv import load_dotenv

load_dotenv()

STARS_COUNT_KEY = 'stars_count'
COMMIT_COUNTS_KEY = 'commit_counts'


def extract_json(result: str) -> dict:
    """Extracts and parses JSON from a given string result."""
    assert result, "Result cannot be None"
    print('Result:', result)
    return json.loads(result)


def create_agent() -> Agent:
    """Creates and returns an Agent instance."""
    prompt = (
        f"Go to https://www.google.com/, Look for browser-use github repository. "
        f"Get the repository star count, Get the commit counts. "
        f"Print the result, in a JSON format: {{ {STARS_COUNT_KEY}: number, {COMMIT_COUNTS_KEY}: number }}"
    )
    sensitive_data = {'email': 'my_email', 'password': 'my_password'}
    return Agent(task=prompt, llm=ChatOpenAI(model="gpt-4o"), sensitive_data=sensitive_data)


async def fetch_github_metrics() -> None:
    """Runs the agent and processes the extracted repository metrics."""
    agent = create_agent()
    history: AgentHistoryList = await agent.run()
    
    data = extract_json(history.final_result())
    stars_count = data.get(STARS_COUNT_KEY, 0)
    commit_counts = data.get(COMMIT_COUNTS_KEY, 0)
    
    if not stars_count or not commit_counts:
        print("Something went wrong")
    else:
        print(f"Stars Count: {stars_count}, Commit Counts: {commit_counts}")


if __name__ == "__main__":
    asyncio.run(fetch_github_metrics())
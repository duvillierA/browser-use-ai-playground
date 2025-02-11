from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class GithubRepoMetrics(BaseModel):
	stars_count: int
	commit_counts: int

controller = Controller(output_model=GithubRepoMetrics)

def _create_agent() -> Agent:
    """Creates and returns an Agent instance."""
    prompt = (
        f"Go to https://www.google.com/, Look for browser-use github repository. "
        f"Get the repository star count, Get the commit counts. "
        f"Return the result"
    )
    sensitive_data = {'email': 'my_email', 'password': 'my_password'}
    return Agent(task=prompt, llm=ChatOpenAI(model="gpt-4o"), sensitive_data=sensitive_data, controller=controller)

async def task() -> None:
    """Runs the agent and processes the extracted repository metrics."""
    agent = _create_agent()
    history = await agent.run()
    
    result = history.final_result()
    
    if result:
        metrics: GithubRepoMetrics = GithubRepoMetrics.model_validate_json(result)
        print(f"Stars Count: {metrics.stars_count}, Commit Counts: {metrics.commit_counts}")
    else:
        print('No result')


async def github_metrics() -> None:
    await task()
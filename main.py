import os
import logging
logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext

load_dotenv()

roulette_agent = Agent(
    model=os.getenv('OPENAI_MODEL_NAME'),
    system_prompt=(
        'what should you do next if you want to apply for the given job posting? '
    ),
)





result = roulette_agent.run_sync('')
print(result.output)

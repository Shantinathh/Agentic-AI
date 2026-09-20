from agno.agent import Agent

#Brain
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id='openai/gpt-oss-120b'),
        tools = [DuckDuckGoTools()],
        markdown=True,
        instructions="You are a expert and helpful travel agent",
        add_datetime_to_context=True
    )
    
travel_agent = build_agent()

travel_agent.print_response(input("ask a question:"))
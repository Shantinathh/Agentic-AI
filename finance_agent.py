from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model = Groq(id='openai/gpt-oss-120b'),
        markdown=True,
        instructions="Format your response using markdown and use tables to display data where possible.",
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        tools = [YFinanceTools(),DuckDuckGoTools()],
        add_datetime_to_context=True,
        debug_mode=True  # used to see how the agent is doing in backend
    )
    
finance_agent = build_agent()

finance_agent.print_response(input("Ask your question:"))
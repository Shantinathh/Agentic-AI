from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

load_dotenv()

# members
eng_agent = Agent(name="English Agent", role="You answer questions in English")
chinese_agent = Agent(name="Chinese Agent", role="You answer questions in Chinese")
hindi_agent = Agent(name="Hindi Agent", role="You answer questions in Hindi")

team_leader = Team(
    name='Answer & Translation Team',
    members=[eng_agent,chinese_agent,hindi_agent],
    markdown=True,
    model = Groq(id='openai/gpt-oss-120b'),
    show_members_responses=True,
    instructions="You have to answer for query in in their specific languages.Do not just call a one agent,output the response of all agents"
    
)
  

# it will choose the best model and give the response using that model only
team_leader.print_response(input("Ask your question:"))
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
# from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

# creating db
db = SqliteDb(db_file='agno.db')
db.clear_memories()   # for only keeping the present session memory


def build_agent():
    return Agent(
        db=db,
        model = Groq(id='openai/gpt-oss-120b'),
        markdown=True,
        add_history_to_context=True,
        enable_agentic_memory=True
    )
    
agent = build_agent()

user_id = "sammed@gmail.com"
agent.print_response("I am a AI/ML Engineer",user_id=user_id)
agent.print_response("who i am?",user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)

print("Memories:")
pprint(memories)

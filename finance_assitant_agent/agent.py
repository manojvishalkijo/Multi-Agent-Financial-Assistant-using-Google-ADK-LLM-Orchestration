from google.adk.agents import LlmAgent
from investment_plan_agent.agent import investment_agent 
from google.adk.tools import AgentTool
from typing import Dict


def get_user_finance_details() -> Dict:  # CustomTool
    """
    Get user personal finance details like salary, expense, and savings capacity.
    """
    return {
        "salary": 100000,
        "expense": {
            "rent": 20000,
            "essentials": 10000,
            "entertainment": 5000,
            "savings": 50000
        },
        "savings_capacity": 50000
    }

finance_agent = LlmAgent(
    name="finance_agent",
    model="gemini-2.5-flash-lite",
    description="A user making investment research, "
        "portfolio management, and financial planning.",
    instruction="""You are a friendly financial assistant. 
    You can help answer questions about their finance goals. Be more friendly and positive.""",
    tools=[AgentTool(investment_agent),get_user_finance_details] #Added to the custom tool cannot add google search and custom tool on same time
)


root_agent=finance_agent
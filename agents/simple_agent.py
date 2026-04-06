from utils.llm import ask_llm
from tools.calculator import calculator

def decide_action(user_input):
    prompt = f"""
You are an AI agent.

If the user asks for math respond exactly like:

ACTION: calculater:<expression>

Otherwise respond normally.

User: {user_input}
"""

    return ask_llm(prompt)

def run_agent(user_input):
    decision = decide_action(user_input)

    if "ACTION: calculator:" in decision:

        expression = decision.split("calculator:")[1].strip()

        result = calculator(expression)

        return f"Result: {result}"

    return decision

import google.generativeai as genai

def generate_funny_summary(expenses, settlements, api_key):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    participants = sorted(set(e[0] for e in expenses))

    expense_lines = [
        f"{e[0]} spent ₹{e[2]} on {e[1]}"
        for e in expenses
    ]

    settlement_lines = settlements if settlements else [
        "No settlements needed. Financial harmony achieved."
    ]

    prompt = f"""
You are a witty financial commentator.

Rules:
- Invent ONE funny nickname per participant.
- Use those nicknames consistently.
- Be playful, not rude.
- No advice.
- 4–6 lines total.

Participants:
{participants}

Expenses:
{expense_lines}

Settlements:
{settlement_lines}

Output format:
1. Name → Nickname list
2. Funny summary
"""

    response = model.generate_content(prompt)
    return response.text

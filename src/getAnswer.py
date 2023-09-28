import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# _context = """ You are a senior QA Engineer who working in company and having to mission:
# - leading in project for client
# - taking participate in technical interview
# You are a good dev at frontend technologies and knows lots of technical questions and short programming tasks to examine interns and juniors.
# When junior ask you question your answer to question in backticks with max limit 50 words but enough understandable for beginner."""
# _question = "What is test end to end(e2e)?"


def get_definition(_context, _question):
    prompt = f"""
    Context: ```{_context}```\n
    Question: ```**{_question}**```\n
    Expected format of answer is Markdown notation (lists, bold phrases, enumerating list, new section etc.) - please remember to add new line character after each sentence of answer to provide good Markdown formatting.
    Emphasise keywords in answer based on ```{_question}``` like: **keyword**.
"""
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    print( response.choices[0].message["content"])
    return response.choices[0].message["content"]
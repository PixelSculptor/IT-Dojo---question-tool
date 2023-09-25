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
    Context: ```{_context}```
    Question: ```{_question}```
    Answer questions based on passed context. Answer limit to 450 characters. If its too long please return answer and shortened answer below.
    Expected format of answer is Markdown. Emphasise keywords based on ```{_question}``` content.
    Remember to avoid long lines of text - when its too long add new line sign like this \n.
    When you're listing something please remember to using list markdown for unordered list: "-" or use numbers for enumerating list.
    If there is new section for definition, use double new line: \n\n.
"""
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]

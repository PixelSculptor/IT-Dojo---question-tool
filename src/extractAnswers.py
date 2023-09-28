import re

def extractAnswers(response):
    pattern = r"Answer:\n(.+?)\n\nShorter answer:\n(.+)"

    match = re.search(pattern, response, re.DOTALL)

    if match:
        exact_answer = match.group(1).strip()
        shorter_answer = match.group(2).strip()
        return exact_answer, shorter_answer
    else:
        return "" ""

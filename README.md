# IT DOJO Question Compare Automate Tool

## Abstract
This tool is useful for team that develops mobile app IT Dojo and much more.
Script gets question from your data (e.g. txt file) and checking similarity of questions to question that is prompted by user reffering to context. This tool helps avoid checking and adding manually new question to base.

### Threshold:
The threshold value represents the similarity threshold below which a user's question will not be considered as a match to any question in the question base. This threshold is used to filter out questions that are not similar enough to the questions in the base. The cosine similarity values will range between -1 and 1, where:

- -1: Perfectly dissimilar
- 0: No similarity
- 1: Perfectly similar
Since cosine similarity values range from -1 to 1, you can set the threshold to be within this range. The choice of the threshold depends on your specific use case and desired level of sensitivity. For instance:

A threshold of 0.9 would only consider very high similarity matches.
A threshold of 0.7 might consider moderately similar matches.
A threshold of 0.5 could consider more loosely similar matches.

### Instalation:

- fork my repo
- add to assets your base of question
- change value of variable `QUESTION_BASE` to path to your file
- install proper dependencies (nltk, sklearn, openAI sdk, dotenv and deep_translator) using `pip`: e.g. `pip install nltk`
- install SDK by OPEN AI
- generate your key
- copy to `.env` file (there is a sample file)
- run program: `python3 verifyQuestion.py`
- have fun ;)

### Additional info
If you enojoy my script please add star to this repo ;)

### Performing script
If you want to provide the best results you need to:
- in `./assets/candidates.txt` paste your questions that you'd like to add.
Then script will:
- compare these questions with questions in base
- if there is no question similar, then add to base and special list of candidates 
- if there is similar question
  - add this question to `./assets/errorlog.txt`
  - then add this question to `./assets/questions-suspected.txt` - there is comparsion with matching question
- user is requested to special context for GPT assistant (now QA or Frontend) to provide the best results 
- script iterates through ready list of question and sending question to GPT LLM model
- returned answer with question is added to list 
- whole list is parsed to JSON
- then JSON with answers in English is translated to Polish language using `deep_translator` library
- final files are ready in `./assets/data/*` directory

### NOTE:
In the near future, basic docker image will be provided
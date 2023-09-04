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
- install proper dependencies (nltk and sklearn) using `pip`: e.g. `pip install nltk`
- install SDK by OPEN AI
- generate your key
- copy to `.env` file (there is a sample file)
- run program: `python3 verifyQuestion.py`
- have fun ;)

### Additional info
If you enojoy my script please add star to this repo ;)


### NOTE:
In the near future, basic docker image will be provided
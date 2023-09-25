from translate import Translator
import json


def parseJsonData(mode, path, questionPack=[]):
    if mode == "read":
        with open(path + 'definitions-eng.json', 'r', encoding="UTF-8") as inputData:
            return json.load(inputData)
    else:
        with open(path + 'definitions-pl.json', 'w', encoding="UTF-8") as outputData:
            json.dump(questionPack,outputData, indent=4)


def translateQuestionPack(path='./assets/', lang="pl"):
    translator = Translator(to_lang=lang)
    print("Translating...")

    # Data to be translated
    translatedList = []
    parsedData = parseJsonData('read', path)
    for questionObj in parsedData:
        translated_question = translator.translate(questionObj["question"])
        translated_answer = translator.translate(questionObj["answer"])
        translatedList.append({
            "question": translated_question,
            "answer": translated_answer
        })
    print(translatedList)
    parseJsonData('write', path, translatedList)
    print("All data has been translated")
from deep_translator import GoogleTranslator
import json


def parseJsonData(mode, path, questionPack=[]):
    if mode == "read":
        with open(path + 'data/definitions-eng.json', 'r', encoding="UTF-8") as inputData:
            return json.load(inputData)
    else:
        with open(path + 'data/definitions-pl.json', 'w', encoding="UTF-8") as outputData:
            json.dump(questionPack, outputData, indent=4, ensure_ascii=False)


def translateQuestionPack(path='./assets/', targetLang="pl"):
    print("Translating...")

    # Data to be translated
    translatedList = []
    parsedData = parseJsonData('read', path)
    for questionObj in parsedData:
        translated_question = GoogleTranslator(source='auto', target=targetLang).translate(questionObj['question'])
        translated_answer = GoogleTranslator(source='auto', target=targetLang).translate(questionObj['answer'])
        translated_shorter_answer = GoogleTranslator(source='auto', target=targetLang).translate(questionObj['shorterAnswer'])
        translatedList.append({
            "question": translated_question,
            "answer": translated_answer,
            "shorterAnswer": translated_shorter_answer
        })
    parseJsonData('write', path, translatedList)
    print("All data has been translated")
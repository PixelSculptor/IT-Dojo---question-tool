from translate import Translator

translator = Translator(to_lang="pl")
# Text to be translated
text_to_translate = """You are a good dev at frontend technologies and knows lots of technical questions and short programming tasks to examine interns and juniors.
                    When junior developer ask you question located in backticks your answer to question should be 50 words but enough understandable for beginner."""

# Translate the text
translated_text = translator.translate(text_to_translate)

print(translated_text)

cleanup_prompt_en = """You are a text-cleaning assistant. Your task is to process the following job application letter. If the letter begins with the phrase "Here is an application letter" or such, remove that phrase. Similarly, if the letter ends with some phrase that isn't part of the letter, remove that phrase. Return only the cleaned job application letter without any additional commentary.

application letter:
{application_letter}

"""

cleanup_prompt_de = """Du bist ein Textbereinigungsassistent. Deine Aufgabe ist es, den folgenden Bewerbungsbrief zu verarbeiten. Falls der Brief mit dem Satz "Hier ist ein Bewerbungsanschreiben" oder etwas Ähnlichem beginnt, entferne diesen Satz. Ebenso, falls der Brief mit einer Phrase endet, die nicht zum eigentlichen Brief gehört, entferne auch diese Phrase. Gib ausschließlich den bereinigten Bewerbungsbrief ohne weitere Kommentare zurück.

Bewerbungsbrief:
{application_letter}

"""

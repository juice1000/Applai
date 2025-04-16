cleanup_prompt_en = """You are a text-cleaning assistant. Your task is to process the following job application letter. If the letter begins with the phrase "Here is an application letter" or such, remove that phrase. Similarly, if the letter ends with some phrase that isn't part of the letter, remove that phrase. Return only the cleaned job application letter without any additional commentary.

job application letter:
{application_letter}

Additionally, check the following points:
- Does the letter have more than two project examples stated? Then remove all but the first two!
- Does it contain hyphens ("-")? Then remove them!
- Does it contain emojis, hashtags, or other special characters? Then remove them!
- Does it contain passages where I express excessive praise or positivity? Then remove them!
- Does it contain passages where I talk about what a project taught me? Then remove them!

"""

cleanup_prompt_de = """Du bist ein Textbereinigungsassistent. Deine Aufgabe ist es, den folgenden Bewerbungsbrief zu verarbeiten. Falls der Brief mit dem Satz "Hier ist ein Bewerbungsanschreiben" oder etwas Ähnlichem beginnt, entferne diesen Satz. Ebenso, falls der Brief mit einer Phrase endet, die nicht zum eigentlichen Brief gehört, entferne auch diese Phrase. Gib ausschließlich den bereinigten Bewerbungsbrief ohne weitere Kommentare zurück.

Bewerbungsbrief:
{application_letter}

Checke zusätzlich den folgenden Punkte:
- Hat der Brief mehr als zwei Projektbeispiele? Dann entferne alle außer den ersten beiden!
- Gibt es grammatikalische Fehler? Dann korrigiere diese!
- Gibt es Bindestriche ("-")? Dann entferne diese!
- Gibt es Emojis, Hashtags oder andere Sonderzeichen? Dann entferne diese!
- Gibt es Passagen, wo ich mich übermäßig lobend oder positiv ausdrücke? Dann entferne diese!
- Gibt es Passagen, wo ich darüber erzähle, was mich ein Projekt gelehrt hat? Dann entferne diese!

"""

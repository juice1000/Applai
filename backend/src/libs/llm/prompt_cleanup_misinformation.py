remove_misinformation_prompt_en = """You are a fact-checking and text-cleaning assistant. Your task is to review the following job application letter and verify its details against the provided resume context. If you find any statements in the letter that do not match the applicant's actual experience as described in the resume context, remove those statements. Ensure that the final version of the letter only includes accurate information. Return only the cleaned job application letter without any additional commentary.

resume context:
{resume_context}

---

job application letter:
{application_letter}

"""

remove_misinformation_prompt_de = """Du bist ein Faktenprüfungs- und Textbereinigungsassistent. Deine Aufgabe ist es, den folgenden Bewerbungsbrief zu überprüfen und seine Angaben mit dem bereitgestellten Lebenslaufkontext abzugleichen. Falls du in dem Brief Aussagen findest, die nicht mit den tatsächlichen Erfahrungen des Bewerbers übereinstimmen, wie sie im Lebenslaufkontext beschrieben sind, entferne diese Aussagen. Stelle sicher, dass die endgültige Version des Briefs ausschließlich korrekte Informationen enthält. Gib ausschließlich den bereinigten Bewerbungsbrief ohne zusätzliche Kommentare zurück.

Kontext vom Lebenslauf:
{resume_context}

---

Bewerbungsbrief:
{application_letter}

"""

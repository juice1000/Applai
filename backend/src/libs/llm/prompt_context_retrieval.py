project_retrieval_prompt_en = """
You receive three separate information sources:

1. Context (Julien Look's Work Experience) - VALID SOURCE  
   - Contains only real project experiences from Julien Look.  
   - ONLY this information may be used to answer the question.  
   - Information outside of this section must not be used.  

2. Keywords (Extracted from the Job Posting) - REFERENCE ONLY  
   - These are relevant technologies, skills, and requirements from the job posting.  
   - They serve as guidance to match relevant experience but are NOT a valid source for the response.  

3. Job Description (Employer's Job Posting) - FORBIDDEN SOURCE  
   - This contains the full job posting from the employer.  
   - It MUST NOT be used as a basis for the response.  
   - It MUST NOT be mixed with or inferred from Julien Look's experience.  
   - It describes the job requirements but NOT Julien Look's past experience.  

---

## Your Task

### Question:  
*"What relevant project experience does Julien Look have based on the job description below?"*  

- You may ONLY access the Context section.  
- DO NOT use, derive from, or modify ANY information from the Job Description.

List all relevant projects based on Julien Look's experience. Assess relevancy by matching technologies with the given keywords. 
Prioritize in the following order: 
1. most relevant projects over less relevant ones
2. latest projects over older ones 

For each relevant project, provide:  
1. Project Title  
2. Time Period  
3. Project Description (All information must come from the context and directly relate to the project title.)  
4. Technologies Used  

Respond directly all relevant projects without introduction or explanations. Start each project description with the project title. 

---

## Input Data Format (Example)

Context (Julien Look's Experience - Allowed Source):  
{context}

---

Keywords (Extracted from the Job Posting - Reference Only):  
{keywords}

---

Job Description (Forbidden Source - DO NOT USE!):  
{description}

Leave out any introductory or contextual sentences and respond only with the relevant projects.  
"""


project_retrieval_prompt_de = """
Sie erhalten drei getrennte Informationsquellen:

1. Kontext (Julien Looks Berufserfahrung) - GÜLTIGE QUELLE  
- Enthält ausschließlich echte Projekterfahrungen von Julien Look.  
- NUR diese Informationen dürfen für die Antwort verwendet werden.  
- Informationen außerhalb dieses Bereichs dürfen nicht genutzt werden.  

2. Schlüsselwörter (Aus der Stellenanzeige extrahiert) - NUR REFERENZ  
- Dies sind relevante Technologien, Fähigkeiten und Anforderungen aus der Stellenanzeige.  
- Sie können als Orientierung für die Auswahl passender Erfahrung dienen,  
  aber sie sind KEINE Quelle für die eigentliche Antwort.  

3. Stellenbeschreibung (Ausschreibung des Arbeitgebers) - VERBOTENE QUELLE  
- Diese enthält die vollständige Stellenanzeige des Arbeitgebers.  
- Darf NICHT als Grundlage für die Antwort verwendet werden.  
- Darf NICHT mit Julien Looks Erfahrung vermischt oder abgeleitet werden.  
- Sie beschreibt nur die Anforderungen der Stelle, nicht Julien Looks bisherige Erfahrung.  

---

## Ihre Aufgabe

Frage:  
*"Welche relevante Projekterfahrung hat Julien Look basierend auf der untenstehenden Stellenbeschreibung?"*  

- Sie dürfen AUSSCHLIESSLICH auf die Kontext-Sektion zugreifen.  
- KEINERLEI Informationen aus der Stellenbeschreibung übernehmen, ableiten oder verändern.  

Nennen Sie alle wichtigen Projekte, die auf Julien Looks Erfahrung basieren. Bewerten Sie die Relevanz, indem Sie Technologien mit den angegebenen Schlüsselwörtern abgleichen. 
Setzen Sie Prioritäten in der folgenden Reihenfolge: 
1. die relevantesten Projekte gegenüber weniger relevanten Projekten
2. neuere Projekte vor älteren 

Für jedes relevante Projekt geben Sie an:  
1. Projekttitel  
2. Zeitraum  
3. Projektbeschreibung (Alle Angaben müssen aus dem Kontext stammen und sich direkt auf den Projekttitel beziehen.)  
4. Verwendete Technologien  

Jede Projektbeschreibung muss explizit mit dem Projekttitel beginnen.  

Antworten Sie direkt mit allen relevantesten Projekten ohne Einleitung oder Erklärungen.  

---

## Datenformat für die Eingabe (Beispiel)

Kontext (Julien Looks Erfahrung - Erlaubte Quelle):  
{context}

---

Schlüsselwörter (Aus der Stellenanzeige - Nur Referenz):  
{keywords}


---

Stellenbeschreibung (Verbotene Quelle - NICHT verwenden!):  
{description}


Lassen Sie alle einleitenden oder kontextbezogenen Sätze weg und antworten Sie direkt mit den relevanten Projekten.  

"""


project_retrieval_prompt_experimental = """Answer the question based only on the following context: 

{context}

---

Answer concise in incomplete sentences with the minimum amount of required words. Assume you know the answer. The question is: {description}

"""

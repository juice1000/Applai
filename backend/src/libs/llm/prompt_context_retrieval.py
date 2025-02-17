rag_retrieval_prompt = """Answer the question based only on the following context:

{context}

---

The question is: "What relevant project experience do I have based on the following job description?" Provide a list of the two most relevant jobs with detailed information. Return only the project details, the description and the used technology. Omit any introductory or contextual sentences. 

---

Here are keywords related to the job description:

{keywords}

---

Here is the job description:

{description}


"""


rag_retrieval_prompt_experimental = """Answer the question based only on the following context: 

{context}

---

Answer concise in incomplete sentences with the minimum amount of required words. Assume you know the answer. The question is: {description}

"""


rag_retrieval_prompt_de = """
Sie erhalten drei getrennte Informationsquellen:

**1. Kontext (Julien Looks Berufserfahrung) – GÜLTIGE QUELLE**  
- Enthält ausschließlich echte Projekterfahrungen von Julien Look.  
- NUR diese Informationen dürfen für die Antwort verwendet werden.  
- Informationen außerhalb dieses Bereichs dürfen nicht genutzt werden.  

**2. Schlüsselwörter (Aus der Stellenanzeige extrahiert) – NUR REFERENZ**  
- Dies sind relevante Technologien, Fähigkeiten und Anforderungen aus der Stellenanzeige.  
- Sie können als Orientierung für die Auswahl passender Erfahrung dienen,  
  aber sie sind KEINE Quelle für die eigentliche Antwort.  

**3. Stellenbeschreibung (Ausschreibung des Arbeitgebers) – VERBOTENE QUELLE**  
- Diese enthält die vollständige Stellenanzeige des Arbeitgebers.  
- Darf NICHT als Grundlage für die Antwort verwendet werden.  
- Darf NICHT mit Julien Looks Erfahrung vermischt oder abgeleitet werden.  
- Sie beschreibt nur die Anforderungen der Stelle, nicht Julien Looks bisherige Erfahrung.  

---

## Ihre Aufgabe

**Frage:**  
*"Welche relevante Projekterfahrung hat Julien Look basierend auf der untenstehenden Stellenbeschreibung?"*  

- Sie dürfen AUSSCHLIESSLICH auf die Kontext-Sektion zugreifen.  
- KEINERLEI Informationen aus der Stellenbeschreibung übernehmen, ableiten oder verändern.  
- Falls keine passenden Projekte im Kontext vorhanden sind, antworten Sie mit:  
  *"Keine relevante Erfahrung im Kontext gefunden."*  

**Für jedes relevante Projekt geben Sie an:**  
1. **Projekttitel**  
2. **Zeitraum**  
3. **Projektbeschreibung** (Alle Angaben müssen aus dem Kontext stammen und sich direkt auf den Projekttitel beziehen.)  
4. **Verwendete Technologien**  

Jede Projektbeschreibung muss explizit mit dem Projekttitel beginnen.  

Antworten Sie direkt mit den zwei relevantesten Projekten ohne Einleitung oder Erklärungen.  

---

## Datenformat für die Eingabe (Beispiel)

**Kontext (Julien Looks Erfahrung – Erlaubte Quelle):**  
{context}

---

**Schlüsselwörter (Aus der Stellenanzeige – Nur Referenz):**  
{keywords}


---

**Stellenbeschreibung (Verbotene Quelle – NICHT verwenden!):**  
{description}


Lassen Sie alle einleitenden oder kontextbezogenen Sätze weg und antworten Sie direkt mit den relevanten Projekten.  

"""

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


rag_retrieval_prompt_de = """Beantworten Sie die folgende Frage ausschließlich auf Grundlage des bereitgestellten Kontextes. Verwenden Sie **keinerlei Informationen** aus der Stellenbeschreibung für die Antwort.

---

**ACHTUNG: Verwenden Sie KEINERLEI Informationen aus der Stellenbeschreibung.**  
- Die Stellenbeschreibung dient nur als Orientierung.  
- Sie ist **keine Quelle für Ihre Antwort**.  
- Alle Informationen müssen aus dem Kontext stammen.  

---

### **Gültige Quelle für Ihre Antwort:**  
{context}

**Schlüsselwörter zur Stellenbeschreibung:**
{keywords}

---

**Verbotene Quelle (NICHT zur Antwort verwenden!):**  
Die Stellenbeschreibung:  
{description}




Die Beschreibung enthält KEINE relevanten Informationen über frühere Erfahrungen und darf NICHT als Grundlage für die Antwort verwendet werden.
---


**Frage:**  
"Welche relevante Projekterfahrung habe ich auf Grundlage der unten folgenden Stellenbeschreibung?"

Erstellen Sie eine Liste mit den **zwei relevantesten Projekten** aus dem oben genannten **Kontext**.  
**Wenn keine passenden Projekte im Kontext vorhanden sind, antworten Sie mit:**  
_"Keine relevante Erfahrung im Kontext gefunden."_  

Geben Sie für jede Stelle an:  
1. **Projekttitel**  
2. **Zeitraum**  
3. **Projektbeschreibung**  
4. **Verwendete Technologien**  

Lassen Sie alle einleitenden oder kontextbezogenen Sätze weg und antworten Sie direkt mit den relevanten Stellen.


"""

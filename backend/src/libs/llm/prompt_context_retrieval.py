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


rag_retrieval_prompt_de = """Beantworten Sie die Frage nur auf der Grundlage des folgenden Kontextes:

{context}

---

Die Frage lautet: "Welche relevante Projekterfahrung habe ich auf der Grundlage der folgenden Stellenbeschreibung?" Geben Sie eine Liste der zwei relevantesten Stellen mit detaillierten Informationen an. Geben Sie nur die Projektdetails, die Beschreibung und die verwendete Technologie an. Lassen Sie alle einleitenden oder kontextbezogenen Sätze weg. 

---

Hier sind Schlüsselwörter, die mit der Stellenbeschreibung zusammenhängen:

{keywords}

---

Hier ist die Stellenbeschreibung:

{description}

"""

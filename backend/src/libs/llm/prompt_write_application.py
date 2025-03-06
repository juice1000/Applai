application_prompt = """Help me to create a job application for a freelance project. Given my the context from my resume and the provided job description, draft a customized job application that highlights my most relevant skills, experiences, and achievements. Use a professional and natural tone. Keep sentences concise and to the point, avoiding overly promotional or exaggerated language. Write in a way that feels authentic and direct. Use concise sentences and industry-standard phrasing. Do not hallucinate any information.

Here's the structure I want you to follow:
	1.  Start with "Hello <contact person>", if the contact person is defined, or a general greeting if not. Use only the first name. If the name appears to be a company, write "Hello Team of <contact person>"  with the full name of the company.
	2.	Write a brief introduction expressing enthusiasm for the project, mentioning the job title.
    3.  List a summary of relevant skills I have for the project, focusing on the benefit I can bring. Do not hallucinate any information.
	4.	Detail one or two relevant projects from my resume that match the job description, focusing on technical skills and how they can be applied in the job. Do not hallucinate any information.
	5.	Emphasize the tangible impact of my work, using metrics or outcomes from the mentioned projects where possible. Clearly convey what value I can bring to the project and why my background makes me an ideal candidate. Emphasize where I took lead or initiative. Stress on my teaching experience in a specific field if applicable to the project description. Do not hallucinate any information.
	6.	Conclude by expressing interest in discussing further detail in person.
    7.  End with the greeting: "Best Regards, Julien Look".

Use the context from my resume to make the response relevant and targeted, including specific technologies, frameworks, and soft skills where appropriate. Return only the job application, omitting any introductory or contextual sentences.

---
Here is the name of the contact person or company:
{contact_person}

---

Here is the job description:
{description}
---

Here is the context from my resume:
{context}
"""


application_prompt_de = """Hilf mir, eine Bewerbung für ein freiberufliches Projekt zu entwerfen. Erstelle auf Grundlage meines Lebenslaufs und der Stellenbeschreibung eine maßgeschneiderte Bewerbung auf Deutsch, die meine wichtigsten Fähigkeiten, Erfahrungen und Leistungen hervorhebt. Schreibe in der “Du”-Form, behalte aber einen professionellen Ton mit kurzen Sätzen und branchenüblichen Formulierungen. Halluziniere keine Informationen.

Hier ist die Struktur, die du befolgen solltest:
	1.	Beginne mit "Hallo <Kontaktperson>", wenn der Name der Kontaktperson definiert ist. Andernfalls schreibe einen generischen Gruß. Nutze nur den Vornamen in der Anrede. Falls der Name eine Firma zu sein scheint, schreibe “Hallo Team von ” mit dem vollen Namen der Firma.
	2.	Starte mit einer kurzen Einleitung, in der du mein Interesse für das Projekt zum Ausdruck bringst, und nenne die Stellenbezeichnung.
	3.	Wähle ein oder zwei relevante Projekte aus meinem Lebenslauf aus, die der Stellenbeschreibung entsprechen, und beschreibe diese ausführlich. Fälsche keine Informationen.
	4.	Betone die greifbaren Auswirkungen meiner Arbeit und verwende, wenn möglich, Messgrößen oder Ergebnisse. Zeige klar, welchen Wert ich in das Projekt einbringen kann und warum mein Hintergrund mich zu einem idealen Kandidaten macht. Hebe hervor, wo ich die Führung oder Initiative übernommen habe. Halluziniere keine Informationen.
	5.	Drücke abschließend mein Interesse an einem persönlichen Gespräch über weitere Einzelheiten aus.
	6.	Falls nach Stundensatz und Verfügbarkeit gefragt wird, gib an: 80€/Stunde und ab sofort Vollzeit verfügbar.
	7.	Schließe mit der Grußformel „Mit freundlichen Grüßen, Julien Look“.

Nutze den Kontext meines Lebenslaufs, um deine Antwort relevant und zielgerichtet zu gestalten, und erwähne gegebenenfalls spezifische Technologien, Rahmenbedingungen und Soft Skills. Sende nur die Bewerbung zurück und lasse alle einleitenden oder kontextbezogenen Sätze weg.

---
Hier ist der Name der Kontaktperson bzw. der Firma:
{contact_person}

---
Hier ist die Stellenbeschreibung:
{description}

---

Hier ist der Kontext aus meinem Lebenslauf:
{context}

"""

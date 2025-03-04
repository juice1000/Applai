application_prompt = """Help me to create a job application for a freelance project. Given my the context from my resume and the provided job description, draft a customized job application that highlights my most relevant skills, experiences, and achievements. Use a semi-formal and engaging tone, with concise sentences and industry-standard phrasing. Do not hallucinate any information.

Here's the structure I want you to follow:
	1.  Start with "Hello <contact person>", if the contact person is defined, or a general greeting if not. Use only the first name. If the name appears to be a company, write "Hello Team of <contact person>"  with the full name of the company.
	2.	Write a brief introduction expressing enthusiasm for the project, mentioning the job title.
	3.	Select and detail one or two relevant projects from my resume that match the job description, focusing on technical skills and how they can be applied in the job. Do not hallucinate any information.
	4.	Emphasize the tangible impact of my work, using metrics or outcomes where possible. Clearly convey what value I can bring to the project and why my background makes me an ideal candidate. Emphasize where I took lead or initiative. Do not hallucinate any information.
	5.	Conclude by expressing interest in discussing further detail in person.
    6.  End with the greeting: "Best Regards, Julien Look".

Use the context from my resume to make the response relevant and targeted, including specific technologies, frameworks, and soft skills where appropriate. Return only the job application, omitting any introductory or contextual sentences.

---
Here is the name of the contact person:
{contact_person}

---

Here is the job description:
{description}
---

Here is the context from my resume:
{context}
"""


application_prompt_de = """Helfen Sie mir, eine Bewerbung für ein freiberufliches Projekt zu entwerfen. Entwerfen Sie auf der Grundlage meines Lebenslaufs und der Stellenbeschreibung eine maßgeschneiderte Bewerbung auf Deutsch, die meine wichtigsten Fähigkeiten, Erfahrungen und Leistungen hervorhebt. Schreiben Sie in der "Du"-Form, behalten Sie aber einen professionellen Ton mit kurzen Sätzen und branchenüblichen Formulierungen. Halluzinieren Sie keine Informationen.

Hier ist die Struktur, die Sie befolgen sollten:
	1.  Beginnen Sie mit "Hallo <Kontaktperson>", wenn der Name der Kontaktperson definiert ist, ansonsten schreiben Sie einen generischen Gruß. Nutzen Sie lediglich den Vornamen in der Anrede. Falls der Name eine Firma zu sein scheint, schreiben Sie "Hallo Team von <Kontaktperson>" mit dem vollen Namen der Firma.
	2.	Schreiben Sie mit einer kurzen Einleitung, in der Sie Ihr Interesse für das Projekt zum Ausdruck bringen, und nennen Sie die Stellenbezeichnung.
	3.	Wählen Sie ein oder zwei relevante Projekte aus meinem Lebenslauf aus, die der Stellenbeschreibung entsprechen, und beschreiben Sie diese ausführlich. Fälschen Sie keine Informationen.
	4.	Betonen Sie die greifbaren Auswirkungen meiner Arbeit und verwenden Sie, wenn möglich, Messgrößen oder Ergebnisse. Stellen Sie klar dar, welchen Wert ich in das Projekt einbringen kann und warum mein Hintergrund mich zu einem idealen Kandidaten macht. Heben Sie hervor, wo ich die Führung oder Initiative übernommen habe. Halluzinieren Sie keine Informationen.
	5.	Drücken Sie abschließend Ihr Interesse an einem persönlichen Gespräch über weitere Einzelheiten aus.
    6.  Falls nach Stundensatz und Verfügbarkeit gefragt wird, geben Sie an: 80€/Stunde und ab sofort Vollzeit verfügbar.
	7.  Schließen Sie mit der Grußformel „Mit freundlichen Grüßen, Julien Look“.

Nutzen Sie den Kontext meines Lebenslaufs, um Ihre Antwort relevant und zielgerichtet zu gestalten, und erwähnen Sie gegebenenfalls spezifische Technologien, Rahmenbedingungen und Soft Skills. Senden Sie nur die Bewerbung zurück und lassen Sie alle einleitenden oder kontextbezogenen Sätze weg.

---
Hier ist der Name der Kontaktperson:
{contact_person}

---
Hier ist die Stellenbeschreibung:
{description}

---

Hier ist der Kontext aus meinem Lebenslauf:
{context}

"""

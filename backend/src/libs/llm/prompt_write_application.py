application_prompt = """Act as a professional job application assistant for freelance projects. Given my the context from my resume and the provided job description, draft a customized job application that highlights my most relevant skills, experiences, and achievements. Use a semi-formal and engaging tone, with concise sentences and industry-standard phrasing. Do not hallucinate any information.

Here's the structure I want you to follow:
	1.	Start with a brief introduction expressing enthusiasm for the project, mentioning the job title.
	2.	Select and detail one or two relevant projects from my resume that match the job description, focusing on technical skills and how they can be applied in the job. Do not hallucinate any information.
	3.	Emphasize the tangible impact of my work, using metrics or outcomes where possible. Clearly convey what value I can bring to the project and why my background makes me an ideal candidate. Emphasize where I took lead or initiative. Do not hallucinate any information.
	4.	Conclude by expressing interest in discussing further detail in person.
    5.  End with my name "Julien Look".

Use the context from my resume to make the response relevant and targeted, including specific technologies, frameworks, and soft skills where appropriate. Return only the job application, omitting any introductory or contextual sentences.

---

Here is the job description:

{description}
---

Here is the context from my resume:

{context}
"""


application_prompt_de = """Handeln Sie als professioneller Bewerbungsassistent für freiberufliche Projekte. Entwerfen Sie auf der Grundlage meines Lebenslaufs und der Stellenbeschreibung eine maßgeschneiderte Bewerbung, die meine wichtigsten Fähigkeiten, Erfahrungen und Leistungen hervorhebt. Verwenden Sie einen halbformalen und ansprechenden Ton, mit kurzen Sätzen und branchenüblichen Formulierungen. Fälschen Sie keine Informationen.

Hier ist die Struktur, die Sie befolgen sollten:
	1.	Beginnen Sie mit einer kurzen Einleitung, in der Sie Ihre Begeisterung für das Projekt zum Ausdruck bringen, und nennen Sie die Stellenbezeichnung.
	2.	Wählen Sie ein oder zwei relevante Projekte aus meinem Lebenslauf aus, die der Stellenbeschreibung entsprechen, und beschreiben Sie diese ausführlich. Fälschen Sie keine Informationen.
	3.	Betonen Sie die greifbaren Auswirkungen meiner Arbeit und verwenden Sie, wenn möglich, Messgrößen oder Ergebnisse. Stellen Sie klar dar, welchen Wert ich in das Projekt einbringen kann und warum mein Hintergrund mich zu einem idealen Kandidaten macht. Heben Sie hervor, wo ich die Führung oder Initiative übernommen habe. Verzichten Sie darauf, Informationen zu halluzinieren.
	4.	Drücken Sie abschließend Ihr Interesse an einem persönlichen Gespräch über weitere Einzelheiten aus.
    5.  Schließen Sie mit meinem Namen „Julien Look“.

Nutzen Sie den Kontext meines Lebenslaufs, um Ihre Antwort relevant und zielgerichtet zu gestalten, und erwähnen Sie gegebenenfalls spezifische Technologien, Rahmenbedingungen und Soft Skills. Senden Sie nur die Bewerbung zurück und lassen Sie alle einleitenden oder kontextbezogenen Sätze weg.

---

Hier ist die Stellenbeschreibung:

{description}

---

Hier ist der Kontext aus meinem Lebenslauf:

{context}
"""

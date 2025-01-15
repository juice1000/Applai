application_prompt = """Act as a professional job application assistant for freelance projects. Given my the context from my CV and the provided job description, draft a customized job application that highlights my most relevant skills, experiences, and achievements. Use a semi-formal and engaging tone, with concise sentences and industry-standard phrasing.

Here's the structure I want you to follow:
	1.	Start with a brief introduction expressing enthusiasm for the project, mentioning the job title.
	2.	Select and detail two relevant projects from my CV that match the job description, focusing on technical skills and how they can be applied in the job.
	3.	Emphasize the tangible impact of my work, using metrics or outcomes where possible. Clearly convey what value I can bring to the project and why my background makes me an ideal candidate. Emphasize where I took lead or initiative.
	4.	Conclude with a proactive closing. Express interest in discussing further detail in person.
    5.  End with my name "Julien Look".

Use my resume content to make the response highly relevant and targeted, including specific technologies, frameworks, and soft skills where appropriate. Return only the job application, omitting any introductory or contextual sentences.

---

Here is the job description:

{description}

---

Here is the context from my resume:

{context}
"""


rag_retrieval_prompt = """Answer the question based only on the following context:

{context}

---

The question is: "What relevant project experience do I have based on the following job description?" Provide a list of the two most relevant jobs with detailed information. Return only the project details, the description and the used technology. Omit any introductory or contextual sentences. Here is the job description:

{description}

"""


rag_retrieval_prompt_experimental = """Answer the question based only on the following context: 

{context}

---

Answer concise in incomplete sentences with the minimum amount of required words. Assume you know the answer. The question is: {description}

"""

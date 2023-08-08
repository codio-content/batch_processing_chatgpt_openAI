import os
import openai
openai.api_key = os.getenv('OPENAI_KEY')
# CODIO SOLUTION BEGIN 
prompts = [
    "Write a summary of a book about artificial intelligence.",
    "Explain the importance of machine learning in today's world.",
    "Describe the role of neural networks in natural language processing."
]

responses = []

for prompt in prompts:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    responses.append(response.choices[0].text.strip())

# Iterate through the prompts and their corresponding responses
for i, (prompt, response) in enumerate(zip(prompts, responses)):
    print(f"Prompt {i + 1}: {prompt}")
    print(f"Response {i + 1}: {response}\n")
# CODIO SOLUTION END 
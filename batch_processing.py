import time
import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')
#CODIO SOLUTION BEGIN 

def GenerateBatch(prompts):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Select the engine
        prompt=prompts,
        max_tokens=100,  # Limit the response length

    )
    responses = [(choice.text.strip(), choice.finish_reason) for choice in response.choices]


    return responses

#CODIO SOLUTION END

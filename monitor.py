import time
import openai
import os
openai.api_key = os.getenv('OPENAI_KEY')
#CODIO SOLUTION BEGIN 

# Prepare your batch of prompts
prompts = ["who is the oldest president", " what is the name of a famous cave with monsters in greek mythology"]

# Record the start time
start_time = time.time()

# Make the API call
responses = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompts,
    max_tokens=50,
    n=len(prompts),
    stop=None,
    temperature=0.7
)

# Record the end time
end_time = time.time()

# Calculate response time
response_time = end_time - start_time

print(f"Response time: {response_time} seconds")


num_requests = len(prompts)
throughput = num_requests / response_time

print(f"Throughput: {throughput} requests per second")
usage = responses['usage']
total_tokens = usage['total_tokens']
prompt_tokens = usage['prompt_tokens']
completion_tokens = usage['completion_tokens']

print(f"API Usage:")
print(f"  Total tokens: {total_tokens}")
print(f"  Prompt tokens: {prompt_tokens}")
print(f"  Completion tokens: {completion_tokens}")
#CODIO SOLUTION END 
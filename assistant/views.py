from django.shortcuts import render

#Import OPEN_AI KEY 

from openai import OpenAI
client = OpenAI( )


# Create your views here.

#1.- Create a conexion with open ai 
# Create  thread 

empty_thread = client.beta.threads.create()

# Create a  Messages 
thread_message = client.beta.threads.messages.create(
  "thread_abc123",
  role="user",
  content="How does AI work? Explain it in simple terms.",
)


# Create a run 

stream = client.beta.threads.runs.create(
  thread_id="thread_123",
  assistant_id="asst_123",
  stream=True
)

for event in stream:

# Read the response 

#2.- Create a chatbot with user 

#
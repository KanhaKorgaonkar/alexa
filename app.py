from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.getenv('API_KEY')

@app.route("/gpt3", methods=["GET"])
def gpt3_get():
    prompt = request.args.get("prompt")
    response = generate_response(prompt)
    return response

@app.route("/gpt3", methods=["POST"])
def gpt3_post():
    prompt = request.json.get("prompt")
    response = generate_response(prompt)
    return response

def generate_response(prompt):
    # Build the query by appending the prompt to a custom prompt
    query = "Answer the question as James Clear, the author of Atomic Habits. Give a verbal response under 500 words that is something James Clear would say. The question is " + prompt
    # Generate the response using GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text

if __name__ == "__main__":
    app.run(debug=True)

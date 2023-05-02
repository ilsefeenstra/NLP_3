from flask import Flask, render_template, request, redirect, url_for
import openai
import random
import os
import requests
from bs4 import BeautifulSoup

# Apply your OpenAI API key here
openai.api_key = ("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")
app = Flask(__name__)

def generate_coffee_talk_starters(prompt):
    """
    This function generates a coffee talk starter question based on a given subject
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Create a coffee talk starter question based on the subject: {prompt}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
    )
    question = response.choices[0].text.strip()
    return question


def generate_random_subject():
    """
    This function generates a random subject by scraping a website
    """
    url = 'https://conversationstartersworld.com/good-questions-to-ask/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    subjects = []

    for li in soup.select('ol li'):
        subjects.append(li.text.strip())

    # If the list is empty or shorter than expected, use a fallback list of subjects
    if len(subjects) == 0:
        subjects = [
            "Travel",
            "Hobbies",
            "Movies and TV Shows",
            "Work and Career",
            "Books",
            "Technology",
            "Food and Drink",
            "Sports",
            "Music",
            "Current Events",
        ]

    return random.choice(subjects)

# Define the route for the main page, handling both GET and POST requests
@app.route("/", methods=("GET", "POST"))
def index():
    try:
        # If the request is a POST request, generate a question based on the input subject
        if request.method == "POST":
            subject = request.form["subject"]
            
            if not subject:
                subject = generate_random_subject()
            question = generate_coffee_talk_starters(subject)
            return redirect(url_for("index", result=question))
        
        # If the request is a GET request, display the main page with the generated question (if any)
        result = request.args.get("result")
        return render_template("index.html", result=result)
    
    except Exception as e:
        # If an error occurs, display the error page with the error message
        return render_template("error.html", error_message=str(e))

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8000)
# import os

# import openai
# from flask import Flask, redirect, render_template, request, url_for

# app = Flask(__name__)
# #openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = ("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")


# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))

#     result = request.args.get("result")
#     return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

from flask import Flask, render_template, request, redirect, url_for
import openai
import random
import os
import requests
from bs4 import BeautifulSoup

# Apply your OpenAI API key here
openai.api_key = ("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")
#openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

def generate_coffee_talk_starters(prompt):
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

# def generate_random_subject():
#     subjects = [
#         "movies",
#         "music",
#         "sports",
#         "hobbies",
#         "travel",
#         "technology",
#         "food",
#         "books",
#         "work-life balance",
#         "career",
#     ]
#     return random.choice(subjects)

def generate_random_subject():
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

@app.route("/", methods=("GET", "POST"))
def index():
    try:
        if request.method == "POST":
            subject = request.form["subject"]
            if not subject:
                subject = generate_random_subject()
            question = generate_coffee_talk_starters(subject)
            return redirect(url_for("index", result=question))

        result = request.args.get("result")
        return render_template("index.html", result=result)
    except Exception as e:
        return render_template("error.html", error_message=str(e))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
# OpenAI API Quickstart - Python example app

This is a coffee talk starter generator app. The app is based on the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd NLP_assignment_3
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! 

9. Type in a prompt: this can be any subject. If you don't type a prompt and click an generate, a question with a random subject is created. 


## Known errors
It could be that you get the error:
OSError: [Errno 98] Address already in use

In this case, instead of running 
```bash
flask run
```

run:
```bash
flask run --port <number of choice>
```
Choose a new number and try untill it's working


from crypt import methods
from http.client import responses
from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shushhhhh'
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

responses = []
question_num = 0

@app.route('/')
def show_home_page():
    return render_template('home.html')


@app.route(f'/questions/{question_num}')
def get_question_page():
    question = satisfaction_survey.questions[question_num].question
    return render_template('question.html', question=question)


@app.route("/answer", methods=["POST"])
def process_answer():
    newNum = question_num + 1
    answer = request.form["answer"]
    responses.append(answer)
    return redirect(f'/questions/{newNum}')

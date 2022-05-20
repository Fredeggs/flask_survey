from crypt import methods
from http.client import responses
from flask import Flask, render_template, request, redirect, flash
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


@app.route('/questions/<num>')
def get_question_page(num):
    global question_num
    q_num = int(num)
    if len(responses) == len(satisfaction_survey.questions):
        flash("You have already completed the survey, doofus!")
        return redirect('/thankyou')
    if q_num == question_num:
        question = satisfaction_survey.questions[q_num].question
        return render_template('question.html', question=question)
    flash("You need to answer the questions in order, u absolute knob!")
    return redirect(f"/questions/{question_num}")


@app.route('/thankyou')
def show_thankyou():
    return render_template('thankyou.html')

@app.route("/answer", methods=["POST"])
def process_answer():
    answer = request.form["answer"]
    responses.append(answer)
    global question_num
    question_num += 1
    if question_num >= len(satisfaction_survey.questions):
        return redirect("/thankyou")
    return redirect(f"/questions/{question_num}")

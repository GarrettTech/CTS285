from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

class Calculator:
    def __init__(self):
        self.display = ""
        self.question = ""
        self.is_entering_question = True
        self.attempts = 0
        self.next_enabled = False
        self.result = ""

    def handle_input(self, value):
        if value == 'clear':
            self.display = ""
        elif value == 'enter':
            self.handle_enter()
        elif value == 'next':
            self.move_to_next()
        else:
            self.display += value

    def handle_enter(self):
        if self.is_entering_question:
            self.question = self.display
            self.display = ""
            self.is_entering_question = False
            self.attempts = 0
            self.result = "Enter your answer"
        else:
            self.check_answer()

    def check_answer(self):
        try:
            correct_answer = eval(self.question)
            user_answer = float(self.display)
            if abs(user_answer - correct_answer) < 0.0001:
                self.result = "Correct!"
                self.next_enabled = True
            else:
                self.attempts += 1
                if self.attempts < 3:
                    self.result = f"Incorrect. You have {3 - self.attempts} attempts left."
                    self.display = ""
                else:
                    self.result = f"Incorrect. The correct answer is {correct_answer}"
                    self.next_enabled = True
        except:
            self.result = "Invalid input"

    def move_to_next(self):
        self.question = ""
        self.is_entering_question = True
        self.attempts = 0
        self.display = ""
        self.result = ""
        self.next_enabled = False

calculator = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def handle_input():
    data = request.json
    calculator.handle_input(data['input'])
    return jsonify({
        'display': calculator.display,
        'question': f"Question: {calculator.question}" if calculator.question else "Enter a question",
        'result': calculator.result,
        'next_enabled': calculator.next_enabled
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
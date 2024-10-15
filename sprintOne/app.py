from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app)

class Calculator:
    def __init__(self):
        self.display = ""
        self.question = ""
        self.is_entering_question = True
        self.attempts = 0
        self.next_enabled = False
        self.result = ""
        self.memory_bank = []
        self.current_memory_question = None
        self.memory_mode = False

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
        if self.is_entering_question and not self.memory_mode:
            self.question = self.display
            self.display = ""
            self.is_entering_question = False
            self.attempts = 0
            self.result = "Enter your answer"
        else:
            self.check_answer()

    def check_answer(self):
        try:
            if self.memory_mode:
                correct_answer = eval(self.current_memory_question)
            else:
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
        if self.memory_mode:
            if self.memory_bank:
                self.current_memory_question = random.choice(self.memory_bank)
                self.question = self.current_memory_question
            else:
                self.memory_mode = False
                self.question = ""
                self.current_memory_question = None
        else:
            self.question = ""
        self.is_entering_question = not self.memory_mode
        self.attempts = 0
        self.display = ""
        self.result = ""
        self.next_enabled = False

    def add_to_memory_bank(self, question):
        self.memory_bank.append(question)

    def clear_memory_bank(self):
        self.memory_bank = []

    def start_memory_mode(self):
        if self.memory_bank:
            self.memory_mode = True
            self.move_to_next()
            return True
        return False

    def stop_memory_mode(self):
        self.memory_mode = False
        self.current_memory_question = None
        self.move_to_next()

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
        'next_enabled': calculator.next_enabled,
        'memory_mode': calculator.memory_mode
    })

@app.route('/add_to_memory', methods=['POST'])
def add_to_memory():
    data = request.json
    calculator.add_to_memory_bank(data['question'])
    return jsonify({'success': True, 'memory_bank_size': len(calculator.memory_bank)})

@app.route('/clear_memory', methods=['POST'])
def clear_memory():
    calculator.clear_memory_bank()
    return jsonify({'success': True})

@app.route('/start_memory_mode', methods=['POST'])
def start_memory_mode():
    success = calculator.start_memory_mode()
    if success:
        return jsonify({
            'success': True,
            'question': f"Question: {calculator.question}",
            'memory_mode': True
        })
    else:
        return jsonify({
            'success': False,
            'message': "Memory bank is empty. Add questions first.",
            'memory_mode': False
        })

@app.route('/stop_memory_mode', methods=['POST'])
def stop_memory_mode():
    calculator.stop_memory_mode()
    return jsonify({
        'success': True,
        'memory_mode': False
    })

@app.route('/get_memory_bank_size', methods=['GET'])
def get_memory_bank_size():
    return jsonify({
        'size': len(calculator.memory_bank)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
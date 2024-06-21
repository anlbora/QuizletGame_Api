import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, Qt  # Correct import for QPropertyAnimation
from MainWindow import Ui_MainWindow
from data import question_data
from Question import Question
from QuizBrain import QuizBrain
import html
import random

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.score = 0
        
        self.question_bank = self.create_question_bank()
        self.quiz = QuizBrain(self.question_bank)

        self.load_question()

        # Connect the buttons to their respective handlers
        self.ui.btn_correct.clicked.connect(self.handle_correct)
        self.ui.btn_wrong.clicked.connect(self.handle_wrong)

        # Ensure dynamic resizing and fitting of the text
        self.ui.lbl_question.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.lbl_question.setAlignment(Qt.AlignCenter)

        # Initialize option button clicks
        for i, btn in enumerate(self.ui.option_buttons):
            btn.clicked.connect(lambda _, x=i+1: self.handle_option_click(x))

    def create_question_bank(self):
        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(question)
        return question_bank

    def load_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            formatted_question_text = self.format_question_text(question)
            self.ui.lbl_question.setText(formatted_question_text)
            self.adjust_label_font_size(self.ui.lbl_question)  # Adjust the font size to fit the area
            self.reset_feedback()
            self.toggle_input_mode(question["type"])
        else:
            self.ui.lbl_question.setText("Quiz Complete!")
            self.ui.btn_correct.setDisabled(True)
            self.ui.btn_wrong.setDisabled(True)
            for btn in self.ui.option_buttons:
                btn.setDisabled(True)

    def format_question_text(self, question):
        question_text = html.unescape(question["question"])

        if question["type"] == "multiple":
            options = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(options)
            options_text = "\n".join([f"{i+1}. {html.unescape(option)}" for i, option in enumerate(options)])
            question_text = f"{question_text}\n\nOptions:\n{options_text}"

        return question_text

    def toggle_input_mode(self, question_type):
        if question_type == "boolean":
            self.ui.btn_correct.setEnabled(True)
            self.ui.btn_wrong.setEnabled(True)
            for btn in self.ui.option_buttons:
                btn.setVisible(False)  # Hide option buttons for boolean questions
        else:  # Assuming multiple-choice type
            self.ui.btn_correct.setDisabled(True)
            self.ui.btn_wrong.setDisabled(True)
            for btn in self.ui.option_buttons:
                btn.setVisible(True)  # Show option buttons for multiple-choice questions

    def adjust_label_font_size(self, label):
        # Set initial font size and minimum font size
        initial_font_size = 24  # Start with a larger size
        minimum_font_size = 10  # Ensure readability even at smaller sizes
        
        font = label.font()
        font.setPointSize(initial_font_size)
        label.setFont(font)
        
        # Reduce font size until the text fits within the label
        while (label.fontMetrics().boundingRect(label.text()).width() > label.width() or
               label.fontMetrics().boundingRect(label.text()).height() > label.height()) and font.pointSize() > minimum_font_size:
            font.setPointSize(font.pointSize() - 1)
            label.setFont(font)
        
        # Optionally, increase font size to make it as large as possible without overflowing
        while (label.fontMetrics().boundingRect(label.text()).width() < label.width() * 0.9 and
               label.fontMetrics().boundingRect(label.text()).height() < label.height() * 0.9 and
               font.pointSize() < initial_font_size):
            font.setPointSize(font.pointSize() + 1)
            label.setFont(font)

    def handle_correct(self):
        self.give_feedback("True")

    def handle_wrong(self):
        self.give_feedback("False")

    def handle_option_click(self, option_number):
        self.give_feedback(str(option_number))

    def give_feedback(self, answer):
        correct = self.quiz.check_answer(answer)
        if correct:
            self.score += 1
            self.ui.lbl_question.setText("Correct!")
            self.ui.lbl_question.setStyleSheet("color: white; background-color: #5cb85c;")  # Green for correct
        else:
            self.ui.lbl_question.setText("Wrong!")
            self.ui.lbl_question.setStyleSheet("color: white; background-color: #d9534f;")  # Red for wrong
        
        # Update the score display
        self.ui.txt_score.setText(f"Score: {self.score}")

        # Load next question after 1 second
        QtCore.QTimer.singleShot(1000, self.load_question)


    def reset_feedback(self):
        self.ui.lbl_question.setStyleSheet("color: white; background-color: transparent;")  # Reset background color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
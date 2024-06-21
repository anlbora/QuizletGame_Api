
# Quizlet Game Application

Welcome to the Quizlet Game Application! This is a desktop application built using Python and PyQt5 that quizzes users on a variety of topics. The questions are fetched dynamically from an online trivia API, and the game supports both true/false and multiple-choice questions.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Application Overview](#application-overview)
- [Code Structure](#code-structure)
  - [Main Window](#main-window)
  - [Question Handling](#question-handling)
  - [Quiz Logic](#quiz-logic)
- [API Integration](#api-integration)

## Features

- **Dynamic Question Loading**: Fetches questions from the Open Trivia Database (OpenTDB).
- **Multiple Question Types**: Supports both true/false and multiple-choice questions.
- **User Feedback**: Provides immediate feedback on whether the answer is correct or wrong.
- **Score Tracking**: Keeps track of the user's score throughout the quiz.
- **Responsive Design**: Adjusts font sizes to ensure readability across different screen sizes.

## Usage

Once the application is running, you will be presented with a series of trivia questions. Depending on the type of question, you can either:
- **Click the True/False buttons** for true/false questions.
- **Click one of the option buttons** for multiple-choice questions.

Your score will be updated based on your answers, and feedback will be provided immediately after each question. The game continues until there are no more questions left.

## Application Overview

### User Interface

The application's UI is built using PyQt5, providing a responsive and visually appealing design. Key components include:
- **Question Label**: Displays the current question.
- **Option Buttons**: For multiple-choice questions, four buttons are displayed for each possible answer.
- **True/False Buttons**: For true/false questions.
- **Score Label**: Displays the user's current score.

### Game Flow

1. **Fetch Questions**: Questions are fetched from the OpenTDB API when the game starts.
2. **Display Question**: The current question is displayed along with the corresponding answer options.
3. **User Input**: The user selects an answer.
4. **Provide Feedback**: Immediate feedback is given, indicating if the answer was correct or wrong.
5. **Update Score**: The user's score is updated based on their answer.
6. **Next Question**: The next question is loaded, and the process repeats until all questions are answered.

## Code Structure

### Main Window (`Main` Class)

This class initializes the main window and manages the overall game logic. Key methods include:

- `__init__`: Sets up the UI and initializes the question bank and quiz logic.
- `load_question`: Loads and displays the next question, adjusting the UI based on the question type.
- `give_feedback`: Provides feedback based on the user's answer and updates the score.
- `adjust_label_font_size`: Dynamically adjusts the font size of the question label to ensure it fits the available space.

### Question Handling

Questions are fetched from the OpenTDB API and formatted appropriately for display. The `format_question_text` method handles the unescaping of HTML entities and formats the options for multiple-choice questions.

### Quiz Logic (`QuizBrain` Class)

Manages the state of the quiz, including the current question and the user's score. Key methods include:

- `next_question`: Retrieves the next question in the sequence.
- `check_answer`: Validates the user's answer against the correct answer for the current question.

## API Integration

The application fetches questions from the [Open Trivia Database (OpenTDB)](https://opentdb.com/), an open-source API that provides trivia questions across various categories. The API request is made in the following way:

```python
url_base = "https://opentdb.com/api.php?"
amount = "10"
response = requests.get(f"{url_base}amount={amount}")
data = response.json()
question_data = data["results"]
```

The questions are then processed and used throughout the game.

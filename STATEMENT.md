# 📝 statement.md

This file defines the core context, boundaries, target audience, and main capabilities of the Typing Speed Calculator project, as required for the GitHub repository submission.

---

## 1. Problem Statement

The contemporary digital landscape necessitates efficient and accurate text input, making proficient typing a crucial skill for students and professionals. However, individuals often lack a dedicated, immediate, and measurable means to assess their current typing ability (typically measured in **Words Per Minute - WPM**) and track improvement over time. Existing measurement tools can be inaccessible or lack the required academic rigor.

The problem this project solves is the need to **design and implement a robust and user-friendly Typing Speed Calculator system** that can accurately:
* Present users with standardized text input.
* Initiate a precise timer and track user keystrokes.
* Calculate and display key performance metrics, specifically **WPM** and **Accuracy Percentage (%)**, based on standardized academic formulas.
* Provide detailed post-test analytics, including a raw error count.

---

## 2. Scope of the Project

The project is executed as a **Minimum Viable Product (MVP)** focused on core logic and adhering to the constraints of a console application, while utilizing a logically layered architecture.

### ✅ In Scope:
* **Core Metrics Calculation:** Implementation of the mathematically correct WPM, time calculation, and raw error detection algorithms.
* **Console Interface:** A complete, functional command-line interface (CLI) for user input and output.
* **Modular Design:** Logical refactoring into a **Three-Tier Architecture** (Presentation, Logic, Data) to ensure clean separation of concerns and meet implementation quality requirements.
* **Error Handling:** Implementation of `try-except` blocks to manage critical runtime errors (e.g., input shorter than source text).

### 🚫 Out of Scope (Future Enhancements):
* **Graphical User Interface (GUI):** A migration to a framework like Tkinter or a web application.
* **Data Persistence:** Storing user high scores or historical data to a file or database.
* **Real-time Visual Feedback:** Highlighting correct/incorrect characters as they are typed (a known limitation of the console environment).

---

## 3. Target Users

The system is designed to benefit any individual seeking to quantify and improve their typing ability.

* **Students:** Individuals striving to improve efficiency in note-taking or report writing.
* **Professionals:** Users seeking to boost productivity in data entry, coding, or documentation tasks.
* **General Users:** Anyone interested in self-improvement and tracking cognitive and motor skills related to computer usage.

---

## 4. High-Level Features

The following represent the major functional capabilities of the system:

1.  **Text Management Module:** Loads and provides random, standardized text passages for continuous testing.
2.  **Timing Module:** Accurately measures test duration by capturing start and end timestamps using Python's standard `time` library.
3.  **Performance Analytics Module:** Calculates and displays the final **WPM** score, **Accuracy Percentage**, and **Raw Error Count**.
4.  **Workflow Management:** Implements a clear, loop-based workflow allowing the user to seamlessly start, complete, and repeat tests.

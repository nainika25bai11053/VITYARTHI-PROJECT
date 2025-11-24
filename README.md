# ⌨️ Typing Speed Calculator

A console-based application built in Python to accurately measure and analyze a user's typing speed and accuracy.

## 💡 Overview

This project is a command-line utility designed to help users track and improve their typing proficiency. It randomly selects a paragraph of text, measures the time taken and errors made during input, and provides immediate feedback on key performance metrics.

The primary goal of this project was to successfully implement core programming concepts, including **algorithms**, **time handling**, and **modular design**, in a practical, functional system.

---

## ✨ Features

The calculator implements the following core functional capabilities (Functional Requirements):

* **Random Text Selection:** Utilizes the `random` module to select a text passage from an internal list for each test session.
* **Accurate Timing:** Uses the system clock (`time.time()`) to precisely capture the **start and end times** of the typing input.
* **Standard WPM Calculation:** Computes the **Words Per Minute (WPM)** score based on the standardized formula: $\text{WPM} = \frac{(\text{Total Characters Typed} / 5)}{(\text{Time in Seconds} / 60)}$.
* **Error Detection:** Implements a character-by-character comparison algorithm to determine the raw number of errors made.
* **Robust Error Handling:** Features a **`try-except`** structure in the error function to gracefully handle critical edge cases (e.g., input shorter than the source text), ensuring system **Reliability**.
* **Logical Workflow:** Manages the test sequence with clear prompts, allowing the user to seamlessly repeat or exit the test.

---

## 🛠️ Technologies & Tools Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.x** | The core programming language used for implementation. |
| **`time` module** | Essential for accurately measuring elapsed time (duration). |
| **`random` module** | Used for selecting and loading test text passages. |

---

## 🚀 Steps to Install & Run

This project is implemented as a single Python script (`codes.py`) with no external library dependencies.


---

## ✅ Instructions for Testing

Testing should focus on verifying the **Reliability** and **Error Handling Strategy** (Non-Functional Requirements) of the application's core logic.

 **Test for Zero Errors (Accuracy)
 
    

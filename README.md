📂 Python To-Do List Manager

**A modular Python task management utility that lets users add, view, complete, and delete tasks while storing task data persistently in a JSON file.**

---

## 📌 Overview

Keeping track of daily tasks helps organize work and maintain productivity. Python To-Do List Manager provides a simple command-line application for managing tasks and tracking their completion status.

The application uses Python's built-in `json` module to store tasks and `pathlib` to manage file paths. Each task receives a unique ID, making it easier to identify and manage individual tasks. Its modular structure separates task-management logic from user interaction.

## ✨ Features

- Add tasks with unique IDs
- View all saved tasks
- View pending tasks
- Mark tasks as completed
- Delete tasks using their IDs
- Track task completion using Boolean values
- Save tasks persistently in a JSON file
- Generate IDs based on existing tasks
- Handle invalid menu choices and task IDs
- Keep task-management logic separate from the main menu

## 🛠️ Tech Stack

- Python 3
- `json` — storing and retrieving task data
- `pathlib` — filesystem path handling
- Lists and dictionaries — organizing task records
- Boolean values — tracking completion status
- Functions, list comprehensions, loops, and exception handling

No third-party packages are required.

## 📁 Project Structure

```text
python-todo-list-manager/
├── main.py
├── todo_manager.py
├── .gitignore
├── README.md
└── tasks.json  (created automatically)
```

- **`main.py`** handles the command-line menu, user input, and task display.
- **`todo_manager.py`** contains the logic for loading, saving, adding, filtering, completing, and deleting tasks.
- **`.gitignore`** excludes local task data and generated Python files from Git tracking.
- **`tasks.json`** stores tasks locally and is created when the first task is saved.

## 🚀 Getting Started

### Prerequisites

Python 3.8 or newer.

### Run the application

1. Download or clone the repository.
2. Open the project folder in your terminal.
3. Run:

```bash
python main.py
```

4. Choose an option from the menu.
5. Add tasks and manage their completion status.

No additional dependencies need to be installed.

## 💻 Example

Example task data stored in `tasks.json`:

```json
[
    {
        "id": 1,
        "title": "Practise Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Solve a DSA problem",
        "completed": true
    }
]
```

Example menu:

```text
===== PYTHON TO-DO MANAGER =====
1. Add task
2. View all tasks
3. View pending tasks
4. Mark task completed
5. Delete task
6. Exit

Choose an option:
```

The application saves changes to the JSON file so tasks remain available after restarting the program.

## 🧠 Concepts Learned

- Reading and writing JSON data
- Working with file paths using `pathlib`
- Lists and dictionaries for structured data
- Generating unique task IDs
- Filtering records with list comprehensions
- Boolean values and conditional logic
- Deleting records safely
- Exception handling and input validation
- Modular programming and code reuse
- Persistent local storage

## ⚠️ Safety Notes

- Task information is stored locally in `tasks.json`.
- The `.gitignore` file helps prevent accidental publication of local task data.
- Never commit private information to a public repository.
- `.gitignore` does not untrack a file that has already been committed.
- The application does not use a remote database or cloud synchronization.

## 🔮 Future Improvements

- Edit existing tasks
- Add task priorities and due dates
- Filter tasks by completion status
- Sort tasks by priority or deadline
- Search tasks by keyword
- Add categories and reminders
- Export tasks to CSV
- Add automated unit tests
- Build a graphical user interface

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

*Built with Python to practise JSON persistence, task management, data filtering, and modular programming.*
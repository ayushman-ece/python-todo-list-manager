
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Task data must be a list.")

    return tasks


def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    tasks = load_tasks()
    next_id = max((task["id"] for task in tasks), default=0) + 1

    tasks.append({
        "id": next_id,
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    return next_id


def get_tasks(status="all"):
    tasks = load_tasks()

    if status == "pending":
        return [task for task in tasks if not task["completed"]]

    if status == "completed":
        return [task for task in tasks if task["completed"]]

    return tasks


def mark_completed(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return True

    return False


def delete_task(task_id):
    tasks = load_tasks()
    remaining = [task for task in tasks if task["id"] != task_id]

    if len(remaining) == len(tasks):
        return False

    save_tasks(remaining)
    return True


from todo_manager import (
    add_task,
    get_tasks,
    mark_completed,
    delete_task
)


def display_tasks(status="all"):
    tasks = get_tasks(status)

    if not tasks:
        print("\nNo tasks found.")
        return

    for task in tasks:
        state = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. [{state}] {task['title']}")


def main():
    while True:
        print("\n===== PYTHON TO-DO MANAGER =====")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Mark task completed")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Enter task title: ")
                task_id = add_task(title)
                print(f"Task added with ID {task_id}.")

            elif choice == "2":
                display_tasks()

            elif choice == "3":
                display_tasks("pending")

            elif choice == "4":
                task_id = int(input("Enter task ID: "))

                if mark_completed(task_id):
                    print("Task marked completed.")
                else:
                    print("Task ID not found.")

            elif choice == "5":
                task_id = int(input("Enter task ID: "))

                if delete_task(task_id):
                    print("Task deleted.")
                else:
                    print("Task ID not found.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Choose a number from 1 to 6.")

        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

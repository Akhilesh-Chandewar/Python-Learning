import os

TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                text, status_str = line.strip().rsplit("||", 1)
                status = True if status_str == "Done" else False
                tasks.append({"text": text, "status": status})
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status_str = "Done" if task["status"] else "Not Done"
            f.write(f"{task['text']}||{status_str}\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status_str = "✅" if task["status"] else "❌"
            print(f"{index}. {task['text']} - {status_str}")


def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "status": False})
    save_tasks(tasks)
    print(f"Added task: {text}")


def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["status"] = True
        save_tasks(tasks)
        print(f"Marked task {index} as Done ✅")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['text']}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            text = input("Enter task description: ").strip()
            if text:
                add_task(text)
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            display_tasks(load_tasks())
            try:
                index = int(input("Enter task number to mark done: "))
                mark_done(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            display_tasks(load_tasks())
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Please pick between 1-5.")


if __name__ == "__main__":
    main()

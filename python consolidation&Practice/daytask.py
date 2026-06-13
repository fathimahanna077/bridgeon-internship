from typing import Dict, List

class TaskError(Exception):
    pass


class TaskNotFoundError(TaskError):
    pass


class InvalidTaskDataError(TaskError):
    pass


tasks: Dict[int, dict] = {}
next_id: int = 1



def validate_task_data(data: dict) -> None:
    if "title" not in data:
        raise InvalidTaskDataError("Title is required")

    if not isinstance(data["title"], str):
        raise InvalidTaskDataError("Title must be a string")

    if not data["title"].strip():
        raise InvalidTaskDataError("Title cannot be empty")



def get_all_tasks() -> List[dict]:
    return list(tasks.values())


def get_task(task_id: int) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError(
            f"Task with ID {task_id} not found"
        )

    return tasks[task_id]


def create_task(data: dict) -> dict:
    global next_id

    validate_task_data(data)

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": False
    }

    tasks[next_id] = task

    next_id += 1

    return task


def update_task(task_id: int, data: dict) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError(
            f"Task with ID {task_id} not found"
        )

    validate_task_data(data)

    tasks[task_id]["title"] = data["title"]

    return tasks[task_id]


def delete_task(task_id: int) -> bool:
    if task_id not in tasks:
        raise TaskNotFoundError(
            f"Task with ID {task_id} not found"
        )

    del tasks[task_id]

    return True


def show_menu() -> None:
    print("\n===== TASK MANAGER =====")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. View Task By ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")


def main() -> None:
    while True:
        show_menu()

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                title = input("Task title: ")

                task = create_task({
                    "title": title
                })

                print("Created:", task)

            elif choice == "2":
                all_tasks = get_all_tasks()

                if not all_tasks:
                    print("No tasks found")
                else:
                    for task in all_tasks:
                        print(task)

            elif choice == "3":
                task_id = int(input("Task ID: "))

                task = get_task(task_id)

                print(task)

            elif choice == "4":
                task_id = int(input("Task ID: "))
                title = input("New title: ")

                updated = update_task(
                    task_id,
                    {"title": title}
                )

                print("Updated:", updated)

            elif choice == "5":
                task_id = int(input("Task ID: "))

                delete_task(task_id)

                print("Task deleted")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except TaskError as e:
            print("Error:", e)

        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
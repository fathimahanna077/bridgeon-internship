from pydantic import BaseModel, ValidationError, EmailStr
from typing import Optional
import json
import requests


class UserModel(BaseModel):
    name: str
    email: EmailStr
    age: int


class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False


def create_task(data: dict) -> TaskModel:
    return TaskModel(**data)


def tasks_to_json(tasks: list[TaskModel]) -> str:
    return json.dumps(
        [task.model_dump() for task in tasks],
        indent=4
    )


class GitHubUser(BaseModel):
    login: str
    name: Optional[str] = None
    location: Optional[str] = None
    public_repos: int
    created_at: str


# -------------------------------
# Create Users
# -------------------------------

try:
    user = UserModel(
        name="Afham",
        email="afham@example.com",
        age=22
    )
    print("User Created:")
    print(user)
except ValidationError as e:
    print(e)


# -------------------------------
# Create Tasks
# -------------------------------

tasks = []

task_data = [
    {
        "title": "Buy Milk",
        "priority": "high"
    },
    {
        "title": "Learn FastAPI",
        "description": "Study Pydantic models",
        "priority": "medium"
    }
]

for data in task_data:
    try:
        task = create_task(data)
        tasks.append(task)
        print("\nTask Created:")
        print(task)
    except ValidationError as e:
        print(e)


# -------------------------------
# Convert Tasks to JSON
# -------------------------------

print("\nTasks JSON:")
print(tasks_to_json(tasks))


# -------------------------------
# Call Public API
# -------------------------------

try:
    response = requests.get(
        "https://api.github.com/users/octocat"
    )

    if response.status_code == 200:
        github_user = GitHubUser(**response.json())

        print("\nGitHub User:")
        print(f"Name         : {github_user.name}")
        print(f"Location     : {github_user.location}")
        print(f"Public Repos : {github_user.public_repos}")
        print(f"Created At   : {github_user.created_at}")

    else:
        print(f"API Error: {response.status_code}")

except ValidationError as e:
    print(e)

except Exception as e:
    print(f"Error: {e}")
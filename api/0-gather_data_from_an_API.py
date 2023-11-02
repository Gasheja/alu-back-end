#!/usr/bin/python3
"""to have a TODO list"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    num = sys.argv[1]
    link_user = f"https://jsonplaceholder.typicode.com/users/{num}"
    res_user = requests.get(link_user)

    if res_user.status_code != 200:
        print(f"Error: Unable to fetch data for employee {num}")
        sys.exit(1)

    user = json.loads(res_user.text)

    link_todos = f"https://jsonplaceholder.typicode.com/users/{num}/todos"
    res_todos = requests.get(link_todos)

    if res_todos.status_code != 200:
        print(f"Error: Unable to fetch TODO data for employee {num}")
        sys.exit(1)

    todos = json.loads(res_todos.text)

    all_tasks = [i for i in todos]
    completed_tasks = [i for i in todos if i['completed']]

    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(all_tasks)}):")
    for task in all_tasks:
        status = "✓" if task['completed'] else "✗"
        print(f"\t{status} {task['title']}")


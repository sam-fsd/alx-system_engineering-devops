#!/usr/bin/python3
"""Communicate with a RESTful API"""

import requests
from sys import argv


r = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
)
r_emp = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
emp_name = r_emp.json().get('name')

emp_todos = r.json()
done_tasks = 0

for todo in emp_todos:
    if todo.get('completed'):
        done_tasks += 1

print(f'Employee {emp_name} is done with tasks({done_tasks}/{len(emp_todos)}):')

for task in emp_todos:
    if task.get('completed'):
        print(f"     {task.get('title')}")

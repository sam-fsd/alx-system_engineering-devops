#!/usr/bin/python3
"""Communicate with a RESTful API."""
import csv
import requests
from sys import argv

user_id = argv[1]
r = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
)
r_emp = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
emp_username = r_emp.json().get('username')

emp_todos = r.json()
emp_todo_list = []
for todo in emp_todos:
    a_todo = []
    title = todo.get('title')
    status = todo.get('completed')
    a_todo.extend([user_id, emp_username, str(status), title])

    emp_todo_list.append(a_todo)

with open(f'{user_id}.csv', mode='w', newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(emp_todo_list)

#!/usr/bin/python3
"""Communicate with a RESTful API.

This module communicates with a RESTful API
to fetch and export user-specific data
in JSON format.

Usage:
    $ python3 your_script_name.py user_id
"""
import csv
import json
import requests
from sys import argv
if __name__ == '__main__':
    user_id = argv[1]
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    )
    r_emp = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    emp_username = r_emp.json().get('username')

    emp_todos = r.json()
    emp_todo_list = []
    emp_data = {}
    for todo in emp_todos:
        task = todo.get('title')
        status = todo.get('completed')
        emp_dict = {}

        emp_dict['task'] = task
        emp_dict['completed'] = status
        emp_dict['username'] = emp_username
        emp_todo_list.append(emp_dict)

    emp_data[user_id] = emp_todo_list

    with open(f'{user_id}.json', mode='w', encoding="utf-8") as f:
        json.dump(emp_data, f)

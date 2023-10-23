#!/usr/bin/python3
"""Communicate with a RESTful API.

This module communicates with a RESTful API
to fetch and export user-specific data
in JSON format.

Usage:
    $ python3 your_script_name.py user_id
"""
import json
import requests
if __name__ == '__main__':
    r_users = requests.get('https://jsonplaceholder.typicode.com/users')
    all_emp_data = {}
    for user in r_users.json():
        user_id = user.get('id')
        username = user.get('username')
        r_user_data = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        )

        emp_todo_list = []
        for todo in r_user_data.json():
            emp_todo_dict = {}

            emp_todo_dict['username'] = username
            emp_todo_dict['task'] = todo.get('title')
            emp_todo_dict['completed'] = todo.get('completed')
            emp_todo_list.append(emp_todo_dict)

        all_emp_data[user_id] = emp_todo_list

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as f:
        json.dump(all_emp_data, f)

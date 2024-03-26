#!/usr/bin/python3
"""
script uses REST API to retrieve employee information
using a given ID
"""
import json
import requests
import sys
import time


def records(tasks_dict, users_dict):
    """
    counts the number of tasks completed by user
    @tasks_dict: dictionary of todo list
    @users_dict: dictionary of user details
    """
    user_task_dict = {}
    list_of_tasks = []
    dict_of_lists = {}
    for user in users_dict:
        user_id = user["id"]
        for _dict in tasks_dict:
            if _dict["userId"] == user_id:
                # retrieve all entries for specific user ID
                user_task_dict = {
                        "username": user['username'],
                        "task": _dict['title'],
                        "completed": _dict['completed']
                        }
                # store entries in a list
                list_of_tasks.append(user_task_dict)
        dict_of_lists[user_id] = list_of_tasks
    return dict_of_lists


if __name__ == "__main__":
    """ run script only when executed directly"""
    USER_URL = f"https://jsonplaceholder.typicode.com/users/"
    TODO_URL = f"https://jsonplaceholder.typicode.com/todos/"
    file_path = "todo_all_employees.json"

    # get user's username
    response_user = requests.get(USER_URL)
    users = response_user.json()

    # get tasks completed by user
    response_tasks = requests.get(TODO_URL)
    tasks = response_tasks.json()

    # JSONify the dictionary
    json_data = records(tasks, users)

    # write JSON to file
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file)

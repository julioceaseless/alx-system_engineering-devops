#!/usr/bin/python3
"""
script uses REST API to retrieve employee information
using a given ID
"""
import json
import requests
import sys

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
        for _dict in tasks_dict:
            print(_dict["userId"])
            print(user[1])
            if _dict["userId"] == user[1]:
                # retrieve all entries for specific user ID
                user_task_dict = {
                        "task": _dict['title'],
                        "completed": _dict['completed'],
                        "username": user['username']
                        }
                # store entries in a list
                list_of_tasks.append(user_task_dict)
        dict_of_lists[user["userId"]] = list_of_tasks
    return dict_of_lists


if __name__ == "__main__":
    """ run script only when executed directly"""
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} NUM")
        exit(1)

    USER_URL = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    TODO_URL = f"https://jsonplaceholder.typicode.com/todos/?userID={user_id}"
    file_path = f"{user_id}.json"
    
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

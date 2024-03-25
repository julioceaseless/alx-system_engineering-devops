#!/usr/bin/python3
"""
script uses REST API to retrieve employee information
using a given ID
"""
import json
import requests
import sys


def records(tasks_dict, users_dict, userid, username):
    """
    counts the number of tasks completed by user
    @dict_list: list of dictionary or json data
    @userid: id used to filter results
    @key: key for completed tasks
    @value: value for key above
    """
    data_record = {}
    list_of_records = []
    dict_of_records = {}
    for _dict in tasks_dict:
        if _dict["userId"] == userid:
            data_record = {
                    "task": _dict['title'],
                    "completed": _dict['completed'],
                    "username": users_dict['username']
                    }
            list_of_records.append(data_record)
    dict_of_records[userid] = list_of_records
    return dict_of_records


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
    total_tasks = 0
    # get user's username
    response_user = requests.get(USER_URL)
    users = response_user.json()
    username = users["username"]

    # get tasks completed by user
    response_tasks = requests.get(TODO_URL)
    tasks = response_tasks.json()

    # JSONify the dictionary
    json_data = records(tasks, users, user_id, username)

    # write JSON to file
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file)

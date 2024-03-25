#!/usr/bin/python3
"""
script uses REST API to retrieve employee information
using a given ID
"""
import requests
import sys


def task_count(dict_list, key, value):
    """ retrieves total tasks for a user with id specified by key"""
    count = 0
    for _dict in dict_list:
        if _dict[key] == value:
            count += 1
    return count


def tasks_completed(dict_list, userid, key, value):
    """
    counts the number of tasks completed by user
    @dict_list: list of dictionary or json data
    @userid: id used to filter results
    @key: key for completed tasks
    @value: value for key above
    """
    count = 0
    for _dict in dict_list:
        if _dict["userId"] == userid and _dict[key] is value:
            count += 1
    return count


def list_titles(dict_list, userid, key, value):
    """
    counts the number of tasks completed by user
    @dict_list: list of dictionary or json data
    @userid: id used to filter results
    @key: key for completed tasks
    @value: value for key above
    """
    for _dict in dict_list:
        if _dict["userId"] == userid and _dict[key] is value:
            print(f"\t {_dict['title']}")


if __name__ == "__main__":
    """ run script only when executed directly"""
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} NUM")
        exit(1)

    USER_URL = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    TODO_URL = f"https://jsonplaceholder.typicode.com/todos/?userID={user_id}"
    total_tasks = 0
    # get user's name
    response_user = requests.get(USER_URL)
    user_name = response_user.json()["name"]

    # get tasks completed by user
    response_tasks = requests.get(TODO_URL)
    tasks = response_tasks.json()

    # retrieve total tasks in user's todo list
    total_tasks = task_count(tasks, "userId", user_id)

    # retrieve completed tasks
    completed_tasks = tasks_completed(tasks, user_id, "completed", True)

    print(f"Employee {user_name} is done with tasks", end="")
    print(f"({completed_tasks}/{total_tasks}):")

    # list all completed tasks
    list_titles(tasks, user_id, "completed", True)

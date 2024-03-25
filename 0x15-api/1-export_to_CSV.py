#!/usr/bin/python3
"""
script uses REST API to retrieve employee information
using a given ID
"""
import csv
import requests
import sys


def records(dict_list, userid, username):
    """
    counts the number of tasks completed by user
    @dict_list: list of dictionary or json data
    @userid: id used to filter results
    @key: key for completed tasks
    @value: value for key above
    """
    data_record = []
    list_of_records = []
    for _dict in dict_list:
        if _dict["userId"] == userid:
            data_record = [f"{userid}", f"{username}",
                           f"{_dict['completed']}",
                           f"{_dict['title']}"]
            list_of_records.append(data_record)
    return list_of_records


if __name__ == "__main__":
    """ run script only when executed directly"""
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} NUM")
        exit(1)

    USER_URL = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    TODO_URL = f"https://jsonplaceholder.typicode.com/todos/?userID={user_id}"
    file_path = f"{user_id}.csv"
    total_tasks = 0
    # get user's username
    response_user = requests.get(USER_URL)
    username = response_user.json()["username"]

    # get tasks completed by user
    response_tasks = requests.get(TODO_URL)
    tasks = response_tasks.json()

    data_records = records(tasks, user_id, username)
    """
    # print records for debugging
    for record in data_records:
        print(f"{record}")
    """

    # write to csv file
    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(data_records)

    print("csv file written successfully")

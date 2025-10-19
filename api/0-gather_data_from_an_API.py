#!/usr/bin/python3

"""gather data from an api"""
import requests
import sys

if __name__ == '__main__':
    """gather data from an api"""
    response_todo = requests.get(
        "https://jsonplaceholder.typicode.com/user/" + sys.argv[1] + "/todos"
    )
    data = response_todo.json()
    completed_task = []
    for i in data:
        if i['completed']:
            completed_task.append(i['title'])

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    ).json()
    print("Employee {} is done with tasks({}/{}):".
          format(user["name"], len(completed_task), len(data)))
    [print("\t " + task) for task in completed_task]

#!/usr/bin/python3
"""get TODO list"""

import csv
import json
import requests
import sys
if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    res = requests.get(link)
    user = json.loads(res.text)
    num = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    res = requests.get(link)
    todos = json.loads(res.text)
    data = [{"task": i["title"],
             "completed": i["completed"],
             "username": user["username"]} for i in todos]
    json_data = json.dumps({"{}".format(user["id"]): data})
    with open("{}.json".format(user["id"]), 'w', encoding='utf-8') as f:
        f.write(json_data)


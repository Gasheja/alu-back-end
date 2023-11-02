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
    csv_data = [["{}".format(i["userId"]),
                user["username"],
                "{}".format(i["completed"]),
                 i["title"]] for i in todos]
    with open("{}.csv".format(user["id"]), 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(csv_data)

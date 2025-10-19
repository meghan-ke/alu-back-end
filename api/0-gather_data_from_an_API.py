#!/usr/bin/python3

""" 
this script is to use an api to extract employee details
"""
import requests
import sys
def main():
   """ fetch and display employee todo progress."""
if len(sys.argv) !=2:
   print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

try:
   employee_id = int(sys.argv[1])
except ValueError:
   print("Employee id must an integer")
   sys.exit(1)

base_url = "https://jsonplaceholder.typicode.com"

#now the user info

user_url = f"{base_url}/users/{employee_id}"
user_response = requests.get(user_url)
if user_response.status_code !=200:
   print("Employee not found.")
   sys.exit(1)
user_data = user_response.json()
employee_name= user_data.get("name")

#now let us get the todo list

todos_url = F"{base_url}/todos"
todos_response = requests.get(todos_url, params={"userId": employee_id})
todos = todos_response.json()

# find the completed tasks
completed_tasks = [task for task in todos if task.get("completed")]

# the output
print(f"Employed {employee_name} is done with tasks({len(done_tasks)}/{len(todos)}):")
for task in completed_tasks:
   print(f"\t {task.get('title')}")

if __name__ == "__main__":
   main()

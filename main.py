import time
import json
import os
import inquirer as inq

FILENAME = "tasks.json"

def add_Task():
    print("Enter your Task details:")
    title = input("Enter the title of your task\n")
    descript = input("Enter the description:\n")
    status = input("Enter status (todo / in-progress / done): ").strip().lower()

    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as fn:
            try:
                tasks = json.load(fn)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    if tasks:
        new_id = tasks[-1]["ID"] + 1
    else:
        new_id = 1

    task = {
        "ID": new_id,
        "Title": title,
        "Description": descript,
        "Status": status,
        "CreatedAt": time.strftime("%d/%m/%Y %H:%M:%S"),
        "UpdatedAt": time.strftime("%d/%m/%Y %H:%M:%S")
    }

    tasks.append(task)

    with open(FILENAME, "w") as fn:
        json.dump(tasks, fn, indent=4)
    
    print(f"Task '{title}' added successfully!")

def update_Task():
    id = input("Enter the ID of the task you want to update:\n")
    with open(FILENAME, "r") as fn:
        tasks = json.load(fn)
        for task in tasks:
            if task["ID"] == int(id):
                print("Enter new details (leave blank to keep current value):")
                new_title = input(f"New Title (current: {task['Title']}): ") or task['Title']
                new_descript = input(f"New Description (current: {task['Description']}): ") or task['Description']
                new_status = input(f"New Status (current: {task['Status']}): ") or task['Status']

                task['Title'] = new_title
                task['Description'] = new_descript
                task['Status'] = new_status
                task['UpdatedAt'] = time.strftime("%d/%m/%Y %H:%M:%S")

                with open(FILENAME, "w") as fn:
                    json.dump(tasks, fn, indent=4)
                
                print(f"Task ID {id} updated successfully!")
                return
        
        else:
            print(f"No task found with ID {id}.")
            return

def delete_Task():
    id = int(input("Enter the ID of the task you want to delete:\n"))
    with open(FILENAME, "r") as fn:
        tasks = json.load(fn)

        found = False  # ✅ Add a flag to track if deletion happened

        for task in tasks:
            if task["ID"] == int(id):
                tasks.remove(task)
                found = True
                break  # ✅ Stop the loop once deleted

    if found:
        with open(FILENAME, "w") as fn:
            json.dump(tasks, fn, indent=4)
        print(f"Task ID {id} deleted successfully!")
    else:
        print(f"No task found with ID {id}.")

def show_Tasks():   
    if not os.path.exists(FILENAME):
        print("No tasks found.")
        return

    with open(FILENAME, "r") as fn:
        try:
            tasks = json.load(fn)
        except json.JSONDecodeError:
            print("No tasks found.")
            return

    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    print("-" * 30)
    for task in tasks:
        print(f"ID: {task['ID']}")
        print(f"Title: {task['Title']}")
        print(f"Description: {task['Description']}")
        print(f"Status: {task['Status']}")
        print(f"Created At: {task['CreatedAt']}")
        print(f"Updated At: {task['UpdatedAt']}")
        print("-" * 30)

def main():
    while True:
        print("---------------TASKER---------------")
        action = inq.list_input("What would you like to do?", choices=[
            "➕ Add Task",
            "🔼 Update Task",
            " 🗑 Delete Task",
            " 🔲 Show Tasks",
            "🚪 Exit"
        ])
        print("------------------------------------")

        if action == "➕ Add Task":
            add_Task()
            add_more = inq.confirm("Do you want to add another Task?", default = True)
            if not add_more:
                main()

        elif action == "🔼 Update Task":
            update_Task()
            update_other = inq.confirm("Do you want to update another Task?", default = True)
            if not update_other:
                main()

        elif action == " 🗑 Delete Task":
            delete_Task()
            delete_other = inq.confirm("Do you want to delete another Task?", default = True)
            if not delete_other:
                main()

        elif action == "🔲 Show Tasks":
            show_Tasks()
            input("Press Enter to return to the main menu...") 
            main()

        else:
            print("Exiting the program. Goodbye!")
            os._exit(0)

if __name__ == "__main__":
    main()
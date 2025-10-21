# Tasker, the Task Tracker 📝

A lightweight **command-line task manager** written in Python.  
Easily **add, update, and delete** tasks — all stored in a simple `tasks.json` file.

### 🚀 Features

- ✍️ Add tasks with title, description, status
- 🔄 Update existing tasks by ID
- ❌ Delete tasks instantly
- 💾 Auto-saved in JSON
- 🕒 Created & Updated timestamps

## **Installation** 🛠
To run this project, make sure you have **Python** installed on your system.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/cli-task-tracker.git
cd cli-task-tracker
```

### 2️⃣ Install Dependencies
Install `inquirer` for a smooth menu interface

```sh
pip install inquirer
```

## Usage 🚀
Run the program with:
```sh
python main.py
```

### Main Menu 🏠
```
---------------TASKER---------------
[?] What would you like to do?:
   ➕ Add Task
   🔼 Update Task
    🗑 Delete Task
   🔲 Show Tasks
 > 🚪 Exit
------------------------------------
```

Tasks will be saved in `tasks.json` for persistence.

## Task JSON Structure
```
{
  "ID": 1,
  "Title": "Task title",
  "Description": "Task description",
  "Status": "todo",
  "CreatedAt": "DD/MM/YYYY HH:MM:SS",
  "UpdatedAt": "DD/MM/YYYY HH:MM:SS"
}
```

## Future Enhancements

- Display a list of all tasks before updating/deleting
- Filter tasks by status (todo, in-progress, done)
- Sort tasks by creation or update date
- Add color-coded status in CLI
- Support for recurring tasks or reminders

## Contributing

Feel free to submit issues or pull requests.

All suggestions for new features or improvements are welcome.

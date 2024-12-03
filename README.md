# Todotra

**Todotra** is a simple and efficient terminal-based to-do list tracker written in Python. Designed for productivity enthusiasts, it features an intuitive menu-driven interface that lets users manage their tasks with ease.

---

## Features

- **Add New Tasks**: Quickly add tasks to your to-do list.  
- **View Tasks**: See all your pending and completed tasks in one place.  
- **Mark Tasks as Completed**: Update task status with minimal effort.  
- **Delete Completed Tasks**: Clear completed tasks to keep your list tidy.  
- **Save and Quit**: Automatically save your tasks before exiting the program.  

---

## Installation

Make sure python 3.x is installed on your system.

All tasks are stored in a file located at:
```plaintext
/home/<user>/.todotra/todolist.txt
```

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todotra.git
   ```
2. Navigate to the directory:
   ```bash
   cd todotra
   ```
3. Run the script
   ```bash
   python todotra.py
   ```

## Usage

When running the program you will be prompted with the following menu options:

    1: Add a new task
        Prompts you to enter the task description.
    2: View tasks
        Displays a list of all tasks, categorized as "Pending" or "Completed."
    3: Mark a task as completed
        Prompts you to select a task by its number and marks it as completed.
    4: Delete tasks marked as completed
        Permanently removes all tasks that have been completed.
    q: Save and quit
        Saves your current to-do list to /home/<user>/.todotra/todolist.txt and exits the program.


## Example Usage
```plaintext
Welcome to Todotra!
Choose an option:
1. Add a new task
2. View tasks
3. Mark task as completed
4. Delete completed tasks
q. Save and quit
> 1
Enter the task description: Buy groceries
Task added.

> 2
List of tasks:
1. Buy groceries

> 3
Enter the task number to mark as completed(0 returns you to main): 1
Task "1" marked as completed.

> 4
Deleting all completed tasks... Done.

> q
Todotra saved. Exiting program. Goodbye!
```

## Features in Development

  - Add task due dates.
  - Sort tasks by priority or category.
  - Search for tasks by keywords.

## Contributing

  Contributions are welcome! If you’d like to enhance the functionality or suggest new features, feel free to open an issue or submit a pull request.

## Contact

If you have questions or feedback, reach out to me:

   GitHub: [noorac](https://github.com/noorac)

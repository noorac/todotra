#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

------------------------------------------------------------------------------

To-do tracker
Author: Kjetil Paulsen
Date: 28. september 2024

This is my version of the classic todo-list. 

------------------------------------------------------------------------------

"""

import sys
import os
import time

def load_tasks(filename) -> list:
    """
    Opening the file of previously saved tasks, if there are no tasks saved
    then return an empty list
    """
    try:
        with open(filename, 'r') as file:
            i = 1
            tasklist = {}
            for line in file:
                if line.strip():
                    if line[0] == "*":
                        line = line[1:]
                        tmp_list = ["*",line.strip()]
                    else:
                        tmp_list = [" ",line.strip()]
                    tasklist[i] = tmp_list
                    i += 1
            file.close()
        return tasklist
    except FileNotFoundError:
        return {}

def save_tasks(tasklist, filename) -> None:
    """
    Write the tasklist to a file
    """
    with open(filename, 'w') as file:
        for task in tasklist.values():
            file.write(f'{task[0]}{task[1]}\n')
            #file.write(f'{tasklist[task]}\n')
    file.close()
    return None

def clear_screen() -> None:
    """
    Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def print_heading() -> None:
    """
    Prints out the heading of the program
    """
    clear_screen()
    print('\n\n---------------------------------')
    print('Todotra: a client based todo-tracker')
    print('---------------------------------\n')
    return None

def print_menu() -> None:
    """
    Prints out the main menu
    """
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark task as completed')
    print('4. Delete task marked as completed')
    print('\nq. Save and quit\n')
    print('---------------------------------\n')
    return None

def add_task() -> None:
    """
    Takes input from user and appends it to the task-list
    """
    print_heading()
    task = input('Enter a new task: ')
    tasklist[len(tasklist)+1] = [" ", task]
    print('\nTask added!')
    return None

def view_tasks() -> None:
    """
    Prints out(with enumeration) a list of the tasks
    """
    print_heading()
    if not tasklist:
        print('No tasks')
    else:
        print('List of tasks:')
        for i, task in enumerate(tasklist.values(), start=1):
            print(f'[{task[0]}] {i}. {task[1]}')
    return None

def mark_completed() -> None:
    """
    Prints view_tasks and asks the user for input of which task to mar
    as completed. Then removes the task from the list
    """
    cont = True
    while cont:
        view_tasks()
        if not tasklist:
            return 0
        # Take input on what task to mark
        try:
            task_number = int(input('\nEnter the task number to mark as '
                                    'completed(0 returns you to main): '))
            if task_number < 0 or task_number > len(tasklist):
                print('Please enter a valid number')
            else:
                if task_number == 0:
                    return 0
                else:
                    tmp_task = tasklist[task_number]
                    tasklist[task_number] = ["*",tmp_task[1]]
                    #completed_task = tasklist.pop(task_number - 1)
                    print(f'\nTask "{task_number}" ' 
                          'marked as completed')
                    time.sleep(2)
                    cont = False
        except ValueError:
            print('Please enter a valid number')

    return None

def delete_mark_completed(tasklist) -> dict:
    """
    Removes entries in the dictionary that are marked as completed
    """
    print(tasklist)
    if tasklist:
        for i in range(len(tasklist)):
            tmp_value = tasklist.get(i+1)
            if tmp_value[0] == "*":
                tasklist.pop(i+1)
    save_tasks(tasklist,filename)
    del tasklist
    task_list = load_tasks(filename)
    return task_list


def main() -> None:
    """
    Main function
    """
    user = os.popen('whoami').read()
    user = user[:-1]
    global filename
    global tasklist
    filename = '/home/'+str(user)+'/.todotra/todo_list.txt'
    tasklist = load_tasks(filename)
    cont = True
    while cont:
        print_heading()
        print_menu()
        choise = input('Enter your choise, 1-4, or q to quit: ')
        # Unused try except block
        try:
            pass
        except:
            pass
        # Menu choise
        if choise == '1':
            #Add task
            add_task()
        elif choise == '2':
            #View tasks
            view_tasks()
            wait = input('\nPress enter to continue...')
            del wait
        elif choise == '3':
            #Mark tasks as completed
            mark_completed()
        elif choise == '4':
            #Delete tasks marked as completed
            tasklist = delete_mark_completed(tasklist)
        elif choise == 'q':
            save_tasks(tasklist, filename)
            print('Todotra saved. Exiting program. Goodbye!')
            cont = False
            time.sleep(2)
            clear_screen()
        else:
            print('Please chose one of the options')
            time.sleep(2)


    return None

if __name__ == '__main__':
    main()

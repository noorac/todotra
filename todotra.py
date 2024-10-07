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

def load_tasks(fname) -> list:
    """
    Opening the file of previously saved tasks, if there are no tasks saved
    then return an empty list
    """
    try:
        with open(fname, 'r') as file:
            tasklist = [line.strip() for line in file if line.strip()]
            file.close()
        return tasklist
    except FileNotFoundError:
        return []

def save_tasks(tasklist, fname) -> None:
    """
    Write the tasklist to a file
    """
    with open(fname, 'w') as file:
        for task in tasklist:
            file.write(task + '\n')
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
    print('\nq. Save and quit\n')
    print('---------------------------------\n')
    return None

def add_task() -> None:
    """
    Takes input from user and appends it to the task-list
    """
    print_heading()
    task = input('Enter a new task: ')
    tasklist.append(task)
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
        for i, task in enumerate(tasklist, start=1):
            print(f'{i}, {task}')
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
                    completed_task = tasklist.pop(task_number - 1)
                    print(f'\nTask "{completed_task}" ' 
                          'marked as completed')
                    cont = False
        except ValueError:
            print('Please enter a valid number')

    return None


def main() -> None:
    """
    Main function
    """
    user = os.popen('whoami').read()
    user = user[:-1]
    fname = '/home/'+str(user)+'/.todotra/todo_list.txt'
    global tasklist
    tasklist = load_tasks(fname)
    cont = True
    while cont:
        print_heading()
        print_menu()
        choise = input('Enter your choise, 1-3, or q to quit: ')
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
        elif choise == 'q':
            save_tasks(tasklist, fname)
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

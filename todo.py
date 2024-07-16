import service
from colorama import Fore
import sqlite3
import json

from utils import Response
from form import UserRegisterForm


def print_response(response: Response):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = service.login(username, password)
    print_response(response)


def register_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    form = UserRegisterForm(username, password)
    response = service.register(form)
    print_response(response)


def logout_page():
    response = service.logout()
    print_response(response)


def add_todo():
    name = input('Enter name: ')
    description = input('Enter description: ')
    response = service.todo_add(name, description)
    print_response(response)
    

def update_todo(todo_id, new_todo_text):
    response = {}
    try:
        conn = sqlite3.connect('new.db')
        cursor = conn.cursor()
        
        sql_query = "UPDATE todos SET todo_text = ? WHERE id = ?"
        cursor.execute(sql_query, (new_todo_text, todo_id))
        
        conn.commit()
        response['status'] = 'success'
        response['message'] = 'Todo updated successfully'
    except sqlite3.Error as error:
        response['status'] = 'error'
        response['message'] = f"Failed to update todo: {error}"
    finally:
        if conn:
            conn.close()
    
    return json.dumps(response)


print(update_todo(1, 'Buy groceries and cook dinner'))


def delete_todo(todo_id):
    response = {}
    try:
        conn = sqlite3.connect('new.db')
        cursor = conn.cursor()
        
        sql_query = "DELETE FROM todos WHERE id = ?"
        cursor.execute(sql_query, (todo_id,))
        
        conn.commit()
        response['status'] = 'success'
        response['message'] = 'Todo deleted successfully'
    except sqlite3.Error as error:
        response['status'] = 'error'
        response['message'] = f"Failed to delete todo: {error}"
    finally:
        if conn:
            conn.close()
    
    return json.dumps(response)


print(delete_todo(1))


def block_user(user_id):
    response = {}
    try:
        conn = sqlite3.connect('new.db')
        cursor = conn.cursor()
        
        sql_query = "UPDATE users SET is_blocked = 1 WHERE id = ?"
        cursor.execute(sql_query, (user_id,))
        
        conn.commit()
        response['status'] = 'success'
        response['message'] = 'User blocked successfully'
    except sqlite3.Error as error:
        response['status'] = 'error'
        response['message'] = f"Failed to block user: {error}"
    finally:
        if conn:
            conn.close()
    
    return json.dumps(response)


print(block_user(1))


while True:

    choice = input('enter your choice : ')
    if choice == '1':
        login_page()
    elif choice == '2':
        register_page()
    elif choice == '3':
        logout_page()
    elif choice == '4':
        add_todo()

    elif choice == 'q':
        break


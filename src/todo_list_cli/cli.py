import argparse
import json
import os
from pathlib import Path

file = "todolist.json"
BASE_PATH = Path().cwd()
FILE_PATH = os.path.join(BASE_PATH, file)

# Creates a JSON file
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as f:
        pass

def load_data():
    ...

def task_add(table:list, string:str):
    new_id = len(table) + 1
    new_task = {
        "ID": new_id,
        "Tarefa": string,
        "Completo": False
    }
    print(new_task)
    return None
    

def remove_func_here():
    print("Hello remove")
    ...

def edit_func_here(todo_table, string, index):
    print("Hello edit")
    ...

def run():
   
    parser = argparse.ArgumentParser(prog="Todo List", description="todo list")
    subparser = parser.add_subparsers(dest="command", required=True)

    # ARGUMENTS
    
    # add
    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument("-s", "--string", type=str, required=True, help="Your task")
    add_parser.set_defaults(func=task_add)

    # remove
    remove_parser = subparser.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("-i", "--index", type=int, required=True,
                            help="Select the index of the task you want to remove")
    remove_parser.set_defaults(func=remove_func_here)

    # edit
    edit_parser = subparser.add_parser("edit", help="Edit your todo list")
    edit_parser.add_argument("-i", "--index", type=int, help="The index you want to change")
    edit_parser.add_argument("-s", "--string", type=str, help="New string")
    edit_parser.set_defaults(func=edit_func_here)

    args = parser.parse_args()

    # TEST PRINT
    args_dict = vars(args)
    getstring = args_dict.get("string")
    
    args.func(table, getstring) # ativa a função dependendo de qual subparser vc usa
    # print("ARGS ", args)
    # print("ARGS DICT ", args_dict)
    # print("ARGS DICT GET STRING ", args_dict.get("string"))
    


if __name__ == "__main__":
    run()

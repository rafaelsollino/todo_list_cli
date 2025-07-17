import argparse

# from todo_list_cli.logic import FUNCTIONS HERE!!

def add_func_here():
    print("Hello world add")
    ...

def remove_func_here():
    print("Hello remove")
    ...

def edit_func_here():
    print("Hello edit")
    ...

def run():
    parser = argparse.ArgumentParser(prog="Todo List", description="todo list")
    subparser = parser.add_subparsers(dest="command", required=True)

    # ARGUMENTS
    
    # add
    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument("-s", "--string", type=str, required=True, help="Your task")
    add_parser.set_defaults(func=add_func_here)

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
    args.func()
    print(args)

if __name__ == "__main__":
    run()

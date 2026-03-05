import sys
from todo import ToDo

allowed_args = [
    "add",
    "update",
    "delete",
    "list",
    "mark-done",
    "make-in-progress",
]

def process(args):
    todo = ToDo()
    args_number = len(args)

    if args[0] == "add" and args_number == 2: todo.add(args[1])
    elif args[0] == "update" and args_number == 3: todo.update(args[1], args[2])
    elif args[0] == "delete" and args_number == 2: todo.delete(args[1])
    elif args[0] == "list" and args_number <= 2:
        if args_number == 2: todo.list(args[1])
        else: todo.list()
    elif args[0] == "mark-done" and args_number == 2: todo.mark_done(args[1])
    elif args[0] == "mark-in-progress" and args_number == 2: todo.mark_in_progress(args[1])
    else: print("The arguments are incorrect")

def main():
    args = sys.argv[1:]
    process(args)

if __name__ == "__main__":
    main()
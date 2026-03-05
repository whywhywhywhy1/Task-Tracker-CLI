import sys
import json
from datetime import datetime

allowed_args = [
    "add",
    "update",
    "delete",
    "list",
    "mark-done",
    "make-in-progress",
]

time_format = "%m/%d/%Y, %H:%M:%S"

class CLI:
    tasks = {}

    def __init__(self):
        with open("tasks_list.json", "r") as tasks_list:
            self.tasks = json.load(tasks_list)

    def save(self):
        with open("tasks_list.json", "w") as tasks_list:
            json.dump(self.tasks, tasks_list, indent=4)

    def add(self, description):
        task_id = int(str(list(self.tasks.keys())[-1])) + 1
        creation_time = datetime.now().strftime(time_format)

        self.tasks[task_id] = {
            "description" : description,
            "status" : "todo",
            "created_at" : creation_time,
            "updated_at" : creation_time,
        }
        self.save()

    def update(self, task_id, description):
        self.tasks[task_id]["description"] = description
        self.tasks[task_id]["updatedAt"] = datetime.now().strftime(time_format)
        self.save()

    def delete(self, task_id):
        self.tasks.pop(task_id)
        self.save()

    def list(self, task_type="all"):
        for task_id in self.tasks:
            if task_type == "all" or task_type == self.tasks[task_id]["status"]:
                print(f"""
                    Task id: {task_id}
                    Description: {self.tasks[task_id]["description"]}
                    Status: {self.tasks[task_id]["status"]}
                    Creation date: {self.tasks[task_id]["createdAt"]}
                    Update date: {self.tasks[task_id]["updatedAt"]}      
                """)

    def mark_done(self, task_id):
        self.tasks[task_id]["status"] = "done"
        self.save()

    def mark_in_progress(self, task_id):
        self.tasks[task_id]["status"] = "in-progress"
        self.save()

def process(args):
    print(args)

    cli = CLI()

    if args[0] == "add": cli.add(args[1])
    elif args[0] == "update": cli.update(args[1], args[2])
    elif args[0] == "delete": cli.add(args[1])
    elif args[0] == "list": cli.add(args[1])
    elif args[0] == "mark-done": cli.add(args[1])
    elif args[0] == "mark-in-progress": cli.add(args[1])

def main():
    args = sys.argv[1:]
    process(args)

if __name__ == "__main__":
    main()
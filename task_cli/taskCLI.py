import json
from datetime import datetime
from tabulate import tabulate

time_format = "%m/%d/%Y, %H:%M:%S"
task_attributes = ['id', 'description','status', 'created at', 'updated at']

class TaskCLI:
    tasks = {}

    def __init__(self):
        try:
            with open("tasks_list.json", "r") as tasks_list:
                self.tasks = json.load(tasks_list)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open("tasks_list.json", "w") as tasks_list:
            json.dump(self.tasks, tasks_list, indent=4)

    def add(self, task_description):
        if not self.tasks:
            task_id = 1
        else:
            task_id = int(list(self.tasks.keys())[-1]) + 1
        task_creation_time = datetime.now().strftime(time_format)
        task_status = "todo"

        self.tasks[task_id] = {
            "description" : task_description,
            "status" : task_status,
            "created_at" : task_creation_time,
            "updated_at" : task_creation_time,
        }
        self.save()
        self.list_by_id(task_id)

    def update(self, task_id, task_description):
        try:
            self.tasks[task_id]["description"] = task_description
            self.tasks[task_id]["updatedAt"] = datetime.now().strftime(time_format)
            self.save()
            print("Successfully updated")
            self.list_by_id(task_id)
        except KeyError:
            print(f"No task with number {task_id}")

    def delete(self, task_id):
        try:
            self.tasks.pop(task_id)
            self.save()
            print("Successfully deleted")
        except KeyError:
            print(f"No task with number {task_id}")

    def list(self, task_type="all"):
        table = []
        for task_id in self.tasks:
            if task_type == "all" or task_type == self.tasks[task_id]["status"]:
                table.append([i for i in self.tasks[task_id].values()])
                table[-1].insert(0, task_id)
        print(tabulate(table, headers=task_attributes))

    def mark_done(self, task_id):
        try:
            self.tasks[task_id]["status"] = "done"
            self.save()
            self.list_by_id(task_id)
        except KeyError:
            print(f"No task with number {task_id}")

    def mark_in_progress(self, task_id):
        try:
            self.tasks[task_id]["status"] = "in-progress"
            self.save()
            self.list_by_id(task_id)
        except KeyError:
            print(f"No task with number {task_id}")

    def list_by_id(self, task_id):
        table = [[i for i in self.tasks[task_id].values()]]
        table[0].insert(0, task_id)
        print(tabulate(table, headers=task_attributes))

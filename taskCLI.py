import json
from datetime import datetime

time_format = "%m/%d/%Y, %H:%M:%S"

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

    def update(self, task_id, task_description):
        self.tasks[task_id]["description"] = task_description
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
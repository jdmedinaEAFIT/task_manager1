import json

# 
class TaskManager:
    def __init__(self):
        self.file_path = "tasks.json"
        self.tasks = []
        # 
        try:
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)  # 
        except:
            self.tasks = []  # 

    # 
    def add_task(self, title, description):
        # 
        task = {"id": len(self.tasks) + 1, "title": title, "description": description, "completed": False}
        self.tasks.append(task)
        # 
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    # 
    def complete_task(self, task_id):
        #
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                # 
                return
        print(f"Task {task_id} not found")  # 

    def list_tasks(self):
        # 
        for task in self.tasks:
            print(f"Task {task['id']}: {task['title']} - Completed: {task['completed']}")

    # 
    # 

def main():
    manager = TaskManager()
    manager.add_task("Comprar víveres", "Leche, pan, huevos")
    manager.add_task("Estudiar", "Repasar SOLID y ACID")
    manager.complete_task(1)
    manager.list_tasks()

if __name__ == "__main__":
    main()

import json

# Una sola clase que hace todo
class TaskManager:
    def __init__(self):
        self.file_path = "tasks.json"
        self.tasks = []
        # Violación de Consistencia (ACID): No valida la carga inicial
        try:
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)  # No convierte a objetos Task
        except:
            self.tasks = []  # Ignora errores sin manejo adecuado

    # Violación de S (SOLID): Una sola clase maneja lógica de negocio y persistencia
    def add_task(self, title, description):
        # Violación de Atomicidad (ACID): No asegura que el guardado sea atómico
        task = {"id": len(self.tasks) + 1, "title": title, "description": description, "completed": False}
        self.tasks.append(task)
        # Violación de Durabilidad (ACID): Puede fallar sin notificación
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    # Violación de I (SOLID): No hay segregación de interfaces
    def complete_task(self, task_id):
        # Violación de Consistencia (ACID): No valida el estado
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                # Violación de Durabilidad: No persiste cambios
                return
        print(f"Task {task_id} not found")  # Violación de S: Mezcla lógica con salida

    def list_tasks(self):
        # Violación de S: Mezcla lógica con presentación
        for task in self.tasks:
            print(f"Task {task['id']}: {task['title']} - Completed: {task['completed']}")

    # Violación de O (SOLID): No se puede extender sin modificar la clase
    # Violación de D (SOLID): Depende directamente del archivo JSON

def main():
    manager = TaskManager()
    manager.add_task("Comprar víveres", "Leche, pan, huevos")
    manager.add_task("Estudiar", "Repasar SOLID y ACID")
    manager.complete_task(1)
    manager.list_tasks()

if __name__ == "__main__":
    main()

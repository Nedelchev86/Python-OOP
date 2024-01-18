from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed = 0
        for task in filter(lambda t: t.completed, self.tasks):
            self.tasks.remove(task)
            removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self):
        result = [F"Section {self.name}:"]
        [result.append(t.details()) for t in self.tasks]
        return "\n".join(result)

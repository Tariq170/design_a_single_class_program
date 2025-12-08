class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append(task)

    def incomplete(self):
        return self.tasks

    def mark_as_complete(self, index):
        if index < 0 or index >= len(self.tasks):
            raise Exception("no task available to mark as complete")
        del self.tasks[index]

As a user,
So that I can keep track of my tasks,
I want a program that I can add todo tasks to and see a list of them.



class TodoList:
    def __init__(self):
        # Creates a new empty todo list.
        # tasks: list of strings representing incomplete tasks
        pass

    def add(self, task):
        # Parameters:
        #   task: string
        # Side effects:
        #   Appends the task to the tasks list.
        # Returns nothing.
        pass

    def list_incomplete(self):
        # Returns:
        #   A list of all incomplete tasks (strings).
        pass

    def mark_complete(self, index):
        # Parameters:
        #   index: integer representing the task position
        # Behaviour:
        #   If index is invalid → raise ValueError.
        #   Otherwise → remove the task at that index.
        pass




from todo_list import TodoList
import pytest

def test_add_tasks_appends_to_list():
    todos = TodoList()
    todos.add("buy milk")
    todos.add("revise biology")
    assert todos.list_incomplete() == ["buy milk", "revise biology"]

def test_list_incomplete_returns_all_tasks():
    todos = TodoList()
    todos.add("task one")
    todos.add("task two")
    assert todos.list_incomplete() == ["task one", "task two"]

def test_mark_complete_removes_task_at_index():
    todos = TodoList()
    todos.add("task A")
    todos.add("task B")
    todos.add("task C")
    todos.mark_complete(1)
    assert todos.list_incomplete() == ["task A", "task C"]

def test_mark_complete_invalid_index_raises_error():
    todos = TodoList()
    todos.add("only task")
    with pytest.raises(ValueError):
        todos.mark_complete(10)
    with pytest.raises(ValueError):
        todos.mark_complete(-1)

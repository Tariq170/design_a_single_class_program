from lib.design_a_single_class_program import TodoList
import pytest

def test_add_tasks_appends_to_list():
    todos = TodoList()
    todos.add("buy milk")
    todos.add("revise biology")
    assert todos.incomplete() == ["buy milk", "revise biology"]

def test_list_incomplete_returns_all_tasks():
    todos = TodoList()
    todos.add("task one")
    todos.add("task two")
    assert todos.incomplete() == ["task one", "task two"]

def test_mark_complete_removes_task_at_index():
    todos = TodoList()
    todos.add("task A")
    todos.add("task B")
    todos.add("task C")

    todos.mark_as_complete(1)   # remove "task B"

    assert todos.incomplete() == ["task A", "task C"]

def test_mark_complete_invalid_index_raises_error():
    todos = TodoList()
    todos.add("only task")

    with pytest.raises(Exception):
        todos.mark_as_complete(10)  # index too big

    with pytest.raises(Exception):
        todos.mark_as_complete(-1)  # negative index not allowed

import unittest
import todo_backend as backend

class TestTodoBackend(unittest.TestCase):

    def setUp(self):
        """Set up a fresh todo list for each test."""
        self.todo_list = []

    def test_add_task(self):
        """Test adding a task with valid priority."""
        backend.add_task(self.todo_list, "Buy groceries", "high")
        self.assertEqual(len(self.todo_list), 1)
        self.assertEqual(self.todo_list[0]["task"], "Buy groceries")
        self.assertEqual(self.todo_list[0]["priority"], "high")

    def test_add_task_invalid_priority(self):
        """Test adding a task with an invalid priority."""
        result = backend.add_task(self.todo_list, "Invalid task", "urgent")
        self.assertFalse(result)
        self.assertEqual(len(self.todo_list), 0)

    def test_edit_task(self):
        """Test editing an existing task."""
        backend.add_task(self.todo_list, "Buy groceries", "high")
        result = backend.edit_task(self.todo_list, 0, "Buy fruits", "medium")
        self.assertTrue(result)
        self.assertEqual(self.todo_list[0]["task"], "Buy fruits")
        self.assertEqual(self.todo_list[0]["priority"], "medium")

    def test_edit_task_invalid_index(self):
        """Test editing a task with an out-of-range index."""
        result = backend.edit_task(self.todo_list, 5, "New Task", "low")
        self.assertFalse(result)

    def test_remove_task(self):
        """Test removing a task."""
        backend.add_task(self.todo_list, "Buy groceries", "high")
        result = backend.remove_task(self.todo_list, 0)
        self.assertTrue(result)
        self.assertEqual(len(self.todo_list), 0)

    def test_remove_task_invalid_index(self):
        """Test removing a task that doesn't exist."""
        result = backend.remove_task(self.todo_list, 5)
        self.assertFalse(result)

    def test_reorder_task(self):
        """Test reordering tasks."""
        backend.add_task(self.todo_list, "Task 1", "medium")
        backend.add_task(self.todo_list, "Task 2", "low")
        backend.reorder_task(self.todo_list, 1, 0)
        self.assertEqual(self.todo_list[0]["task"], "Task 2")

    def test_reorder_task_invalid_index(self):
        """Test reordering with an invalid index."""
        result = backend.reorder_task(self.todo_list, 5, 0)
        self.assertFalse(result)

    def test_sort_by_priority(self):
        """Test sorting tasks by priority."""
        backend.add_task(self.todo_list, "Task 1", "medium")
        backend.add_task(self.todo_list, "Task 2", "low")
        backend.add_task(self.todo_list, "Task 3", "high")
        backend.sort_by_priority(self.todo_list)
        self.assertEqual(self.todo_list[0]["task"], "Task 3")  # High priority first
        self.assertEqual(self.todo_list[2]["task"], "Task 2")  # Low priority last

if __name__ == "__main__":
    unittest.main()

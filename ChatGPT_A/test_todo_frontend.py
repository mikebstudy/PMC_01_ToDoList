import unittest
from unittest.mock import patch
import todo_frontend as frontend
import todo_backend as backend

class TestTodoFrontend(unittest.TestCase):

    def setUp(self):
        """Set up a fresh todo list for each test."""
        self.todo_list = []

    @patch("builtins.print")
    def test_display_empty_list(self, mock_print):
        """Test displaying an empty list."""
        frontend.display_todo_list(self.todo_list)
        mock_print.assert_called_with("Your to-do list is empty.")

    @patch("builtins.print")
    def test_display_tasks(self, mock_print):
        """Test displaying tasks."""
        backend.add_task(self.todo_list, "Test Task", "high")
        frontend.display_todo_list(self.todo_list)
        mock_print.assert_any_call("\nTo-Do List:")
        mock_print.assert_any_call("1. [High] Test Task")

    @patch("builtins.input", side_effect=["2", "New Task", "high", "7"])
    @patch("builtins.print")
    def test_add_task_flow(self, mock_print, mock_input):
        """Test the flow of adding a task."""
        with patch("todo_backend.save_todo_list"):
            frontend.main()
        mock_print.assert_any_call("Task added successfully!")

    @patch("builtins.input", side_effect=["6", "7"])
    @patch("builtins.print")
    def test_sort_by_priority_flow(self, mock_print, mock_input):
        """Test sorting tasks by priority through the UI."""
        backend.add_task(self.todo_list, "Task 1", "medium")
        backend.add_task(self.todo_list, "Task 2", "low")
        backend.add_task(self.todo_list, "Task 3", "high")
        with patch("todo_backend.save_todo_list"):
            frontend.main()
        mock_print.assert_any_call("Tasks sorted by priority.")

if __name__ == "__main__":
    unittest.main()

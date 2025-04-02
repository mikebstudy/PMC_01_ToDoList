import unittest
from unittest.mock import patch, MagicMock
import todo_gui
import todo_backend as backend


class TestTodoGUI(unittest.TestCase):

    def setUp(self):
        """Set up a fresh todo list."""
        self.todo_list = []
        backend.save_todo_list(self.todo_list)  # Ensure clean file state

    @patch("todo_gui.sg.Window")
    def test_update_task_list(self, mock_window):
        """Test updating the task list in the GUI."""
        window_mock = MagicMock()
        mock_window.return_value = window_mock

        self.todo_list = [{"task": "Test Task", "priority": "high"}]
        todo_gui.update_task_list(window_mock, self.todo_list)

        window_mock["-TASKS-"].update.assert_called_with(values=["[High] Test Task"])

    @patch("todo_gui.sg.popup_get_text", side_effect=["Edited Task", "medium"])
    @patch("todo_gui.sg.Window")
    def test_edit_task(self, mock_window, mock_popup):
        """Test editing a task via the GUI."""
        self.todo_list.append({"task": "Old Task", "priority": "high"})
        backend.save_todo_list(self.todo_list)

        window_mock = MagicMock()
        mock_window.return_value = window_mock
        window_mock["-TASKS-"].get_indexes.return_value = [0]  # Simulating selection

        todo_gui.main()  # Simulating main event loop
        self.assertEqual(self.todo_list[0]["task"], "Edited Task")
        self.assertEqual(self.todo_list[0]["priority"], "medium")

    @patch("todo_gui.sg.popup_get_text", return_value="1")
    @patch("todo_gui.sg.Window")
    def test_reorder_task(self, mock_window, mock_popup):
        """Test reordering tasks in the GUI."""
        self.todo_list = [
            {"task": "Task 1", "priority": "medium"},
            {"task": "Task 2", "priority": "low"},
        ]
        backend.save_todo_list(self.todo_list)

        window_mock = MagicMock()
        mock_window.return_value = window_mock
        window_mock["-TASKS-"].get_indexes.return_value = [1]  # Simulating selecting "Task 2"

        todo_gui.main()
        self.assertEqual(self.todo_list[0]["task"], "Task 2")  # Should be moved to top


if __name__ == "__main__":
    unittest.main()

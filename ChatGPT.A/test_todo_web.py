import unittest
from unittest.mock import patch, MagicMock
import todo_web
import todo_backend as backend

class TestTodoWeb(unittest.TestCase):

    def setUp(self):
        """Set up a fresh todo list."""
        self.todo_list = []
        backend.save_todo_list(self.todo_list)  # Ensure clean state

    @patch("todo_web.st.rerun")
    @patch("todo_web.st.text_input", return_value="New Task")
    @patch("todo_web.st.selectbox", return_value="high")
    @patch("todo_web.st.form_submit_button", return_value=True)
    def test_add_task(self, mock_button, mock_priority, mock_input, mock_rerun):
        """Test adding a new task in the web app."""
        todo_web.main()
        self.assertEqual(len(self.todo_list), 1)
        self.assertEqual(self.todo_list[0]["task"], "New Task")
        self.assertEqual(self.todo_list[0]["priority"], "high")

    @patch("todo_web.st.rerun")
    @patch("todo_web.st.number_input", side_effect=[1])
    @patch("todo_web.st.text_input", return_value="Updated Task")
    @patch("todo_web.st.selectbox", return_value="medium")
    @patch("todo_web.st.form_submit_button", return_value=True)
    def test_edit_task(self, mock_button, mock_priority, mock_input, mock_number, mock_rerun):
        """Test editing a task in the web app."""
        backend.add_task(self.todo_list, "Old Task", "high")
        todo_web.main()
        self.assertEqual(self.todo_list[0]["task"], "Updated Task")
        self.assertEqual(self.todo_list[0]["priority"], "medium")

    @patch("todo_web.st.rerun")
    @patch("todo_web.st.number_input", return_value=1)
    @patch("todo_web.st.form_submit_button", return_value=True)
    def test_remove_task(self, mock_button, mock_number, mock_rerun):
        """Test removing a task in the web app."""
        backend.add_task(self.todo_list, "Task to remove", "low")
        todo_web.main()
        self.assertEqual(len(self.todo_list), 0)

    @patch("todo_web.st.rerun")
    @patch("todo_web.st.button", return_value=True)
    def test_sort_by_priority(self, mock_button, mock_rerun):
        """Test sorting tasks by priority in the web app."""
        backend.add_task(self.todo_list, "Task 1", "medium")
        backend.add_task(self.todo_list, "Task 2", "low")
        backend.add_task(self.todo_list, "Task 3", "high")
        todo_web.main()
        self.assertEqual(self.todo_list[0]["task"], "Task 3")  # High priority first
        self.assertEqual(self.todo_list[2]["task"], "Task 2")  # Low priority last

if __name__ == "__main__":
    unittest.main()

# Prompts for ChatGPT

## Experimental test prompts

### First try

- Create a python program for a todo list.
  - Created program with a class ToDoList
- Save/Get list to/from a file
  - Updated ToDoList to have load/save methods and code to access
- Add Edit todo list items
  - Added edit feature to both ToDoList and main code
- Add ability to reorder todo list
  - Added ability to move a given task up 1 or down 1 position
- Add ability to mark tasks with a priority: high, medium, low
  - Added logic for priority
- Split up frontend and backend logic into different files
  - Made a backend.py and frontend.py
- Add ability to sort tasks by priority, High, then Medium, then Low
  - Added ability across backend.py and frontend.py
- Add another interface, a GUI interface using FreeSimpleGUI
  - Added gui_frontend.py
- Add ability to edit tasks
  - Added ability to edit tasks with a second dialog window
- Add another interface, a Web interface using streamlit
  - Added web_frontend.py
- Add another interface to reorder tasks
  - Modified both the backend.py and web_frontend.py
- Create tests for the cli version
  - Refactored frontend.py and created a test_cli.py
- Create tests for the gui version
  - Refactored gui_frontend.py and created test_gui.py
- Create tests for the web version
  - Refactored web_frontend.py and created test_web_app.py
- good job. I'm done
  - Finished the session and made my HTML copy a 404 error
  - So I have to copy while working

## Second try

- Create a python program for a todo list. Make a cli, gui (use FreeSimpleGUI) and web (use streamlit) version. Provide test cases for all versions. Use a backend and frontend approach. Include a task priority (High, Medium, Low), edit task, task reorder capabilities for all versions.
  - Produced a different result than First try. Only tests the backend.py

## Third try

- Create a python program for a todo list. Make a cli, gui (use FreeSimpleGUI) and web (use streamlit) version. Provide test cases for all ui versions. Use a backend and frontend approach. Include a task priority (High, Medium, Low) and ability to order by task priority for all versions. Include edit task and task reorder capabilities for all ui versions. Load/save to json file. Make json file easily human-readable.
  - Produced a different result than Second try, with no tests.

## Fourth try

- Create a python program for a todo list. Save/Get list to/from a file. Edit todo list items. Do not use classes.
  - Produced a good program that has function calls to do the work seperated from the UI
- Add these features - 1) ability to reorder the list, 2) ability to mark tasks with priority: high, medium, low and 3) ability to sort the list by priority
  - Added the features. The reorder is not just up and down one, but specifies the location to move to
- Split up the code into frontend and backend logic
  - Code split as requested. Display function left in frontend.
- Add a unit tests for both front and back ends
  - Unit tests added as requested using unittest from python
- Add GUI version using FreeSimpleGUI and add unit test
  - Added GUI using PySimpleGUI and unit test
    - ChatGPT said FreeSimpleGUI does not exist
	- Replaced PySimpleGUI with FreeSimpleGUI
	- Added finalize=True to sg.Window creation
	- Then it worked
  - Unit test failed
- Add Web app version using streamlit and unit test
  - Added Web app version and unit test
	- Web app version does not work
	  - Gives error of streamlit has no attribute experimental_rerun and asks if experimental_user was meant
	- Unit tests also failed with same error as Web app
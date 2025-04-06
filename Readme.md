# ToDoList project
- Based on Python Mega Course (by Ardit Sulce)
  - First 20 lessons on building a Todo List app
  - Includes command line, desktop GUI , and web versions
 
- Three separate implementations 
  - course.C is from working the lessons
  - mikeb.M is enhanced implementation based on my own ideas and those of others on the internet
  - ChatGTP.A is experiments in generating code similiar to course.C and mikeb.M
  - (C,M,A - are the letters that proceed git commit comments and correspond to the respective implementations)

- Github repo: https://github.com/mikebstudy/PMC.01.ToDoList
  - each version is in its own folder 

## course.C
- Versions from course first 20 lessons
- Not all lessons were viewed, just enough to get the gist and do the projects
 
### Departures from course version
- Misc coding changes and variable naming changes that did not affect functionality
- Added clear command
- Changed complete command to done command
- Added number check validation to edit and done commands

## mikeb.M

- Started with final version of course.C
- Refactored functions.py into backend.py
  - Added more backend functions for common processes 
    - Adding, Updating, Dropping logic
    - Also moved \n processing into backend functions
      - Except in gui.py, where special provision made and noted
- Refactored to store data in a json file
  - Involved refactor of code to use todo data as a list of dictionaries
- Add remove command to delete a todo item
- Replace web.py with web2.py. It works more like gui.py
  - ChatGPT was used to create this new version. 
    - Took a couple of hours. Kept running into bugs. 
    - Works basically, but still has some bugs
    - This approach was used because I don't know enough about how to code with streamlit.
  - web.py no longer works and is abandoned rather than overwritten
  - Also all three versions, cli.py, gui.py and web2.py have a 'done' added with the 'drop' functionality 

## ChatGPT.A

- Started with creating prompts in Prompt.md
- The Fourth try of creating prompts yielded a version to work with
- Ultimately, the user interfaces worked, but there were unsolved problems with the unit tests. 
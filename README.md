## RestApi_using_python_FastAPI

Firstly you need to install FastAPI, uvicorn, pydantic packages.
We are using FastAPI to perform the CRUD Operations, we will import BaseModel from pydatic package (a Python library that helps with data validation and settings management), we will use uvicorn for execution.
In the code I didn't import List from typing package cause my python version is 3.12. You have to import it if your version is  3.8 or older

# Execution:
You need to execute the following command in the terminal, you can also use command prompt, but make sure to use the correct path.

*uvicorn main:app --reload*
Here in main indicates the program name.

After using this command, you will get something like this:
INFO:     Will watch for changes in these directories: ['...\\PythonProjectapi']

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

INFO:     Started reloader process [21956] using StatReload

INFO:     Started server process [27984]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

Now you can use postman app to verify this.
http://127.0.0.1:8000
The above is the link, and use accordingly for each method.

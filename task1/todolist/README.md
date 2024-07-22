# To-Do List Application

A simple and attractive To-Do List application built using Python and Tkinter, allowing users to create, update, and track their tasks. The application supports saving tasks to both JSON and CSV formats.

## Features

- Add new tasks with title and description
- Mark tasks as completed
- Delete tasks
- Save tasks to JSON and CSV files
- Load tasks from JSON and CSV files

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Dharmarajrathod/CODSOFT.git
    cd todo-list-app/gui
    ```

2. **Run the application**:
    ```bash
    python main.py
    ```


### Files Description

- `data/`: Contains the data files (`tasks.json` and `tasks.csv`) where tasks are saved.
- `gui/`: Contains the GUI version of the To-Do List application.
  - `__init__.py`: Initialization file for the package.
  - `main.py`: Entry point of the GUI application.
  - `task.py`: Defines the `Task` class.
  - `todo_list_app.py`: Contains the main application logic and GUI components.
- `README.md`: This file.

## Usage

- **Adding a Task**:
  1. Enter the task title in the "Title" field.
  2. Enter the task description in the "Description" field.
  3. Click on the "Add Task" button.

- **Marking a Task as Completed**:
  1. Select the task from the list.
  2. Click on the "Mark Complete" button.

- **Deleting a Task**:
  1. Select the task from the list.
  2. Click on the "Delete Task" button.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)


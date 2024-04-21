import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QListWidget
from PyQt5.QtCore import QObject, pyqtSignal
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='todo_list')
cursor = connection.cursor()

class Tasks:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        cursor.execute("INSERT INTO tasks (name) VALUES (%s)", [task])
        connection.commit()
        self.tasks.append(task)

    def deleteTask(self, index):
        cursor.execute("DELETE FROM tasks WHERE id = %s", [index])
        connection.commit()
        del self.tasks[index]

class App:
    def __init__(self):
        # Create a QApplication object
        self.app = QApplication(sys.argv)

        # Create a window for the application
        self.window = QPushButton("Add Task", None)
        self.window.setWindowTitle("Task Manager")

        # Connect the button to the addTask function
        self.window.clicked.connect(self.addTask)

        # Create a list for the tasks
        self.tasks = Tasks()

        # Create a delete button
        self.deleteButton = QPushButton("Delete Task", None)
        self.deleteButton.setWindowTitle("Delete Task")

        # Connect the delete button to the deleteTask function
        self.deleteButton.clicked.connect(self.deleteTask)

    def addTask(self, task):
        self.tasks.addTask(task)

    def deleteTask(self, index):
        self.tasks.deleteTask(index)

    def run(self):
        # Run the application
        self.app.exec_()

if __name__ == "__main__":
    app = App()
    app.run()
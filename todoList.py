from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import mysql.connector


class TaskListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(TaskListModel, self).__init__(parent)
        self.tasks = []

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            task, date = self.tasks[index.row()]
            return f"{task} - {date}"
        return None

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.tasks)

    def append(self, task):
        self.beginInsertRows(QtCore.QModelIndex(), len(self.tasks), len(self.tasks))
        self.tasks.append(task)
        self.endInsertRows()

    def remove(self, row):
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        del self.tasks[row]
        self.endRemoveRows()


class TaskDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        text = index.model().data(index, QtCore.Qt.EditRole)
        editor.setText(text)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.text(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Connect to the MySQL database
        self.db_connection = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="",  
            database="todo_list" 
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(200, 0, 200, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")

        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter)

        self.task = QtWidgets.QLineEdit(self.centralwidget)
        self.task.setMinimumSize(QtCore.QSize(300, 0))
        self.task.setMaximumSize(QtCore.QSize(500, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.task.setFont(font)
        self.task.setObjectName("task")
        self.verticalLayout.addWidget(self.task, 0, QtCore.Qt.AlignHCenter)

        self.addTask = QtWidgets.QPushButton(self.centralwidget)
        self.addTask.setMinimumSize(QtCore.QSize(150, 0))
        self.addTask.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addTask.setFont(font)
        self.addTask.setObjectName("addTask")
        self.verticalLayout.addWidget(self.addTask, 0, QtCore.Qt.AlignHCenter)

        self.tasksLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tasksLabel.setFont(font)
        self.tasksLabel.setObjectName("tasksLabel")
        self.verticalLayout.addWidget(self.tasksLabel)

        self.tasks = QtWidgets.QListView(self.centralwidget)
        self.tasks.setEnabled(True)
        self.tasks.setMinimumSize(QtCore.QSize(300, 0))
        self.tasks.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tasks.setFont(font)
        self.tasks.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tasks.setResizeMode(QtWidgets.QListView.Fixed)
        self.tasks.setObjectName("tasks")
        self.verticalLayout.addWidget(self.tasks)

        self.deleteTask = QtWidgets.QPushButton(self.centralwidget)
        self.deleteTask.setMinimumSize(QtCore.QSize(300, 0))
        self.deleteTask.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deleteTask.setFont(font)
        self.deleteTask.setObjectName("deleteTask")
        self.verticalLayout.addWidget(self.deleteTask)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionClose_App = QtWidgets.QAction(MainWindow)
        self.actionClose_App.setObjectName("actionClose_App")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.addTask.clicked.connect(self.add_task_to_list)
        self.deleteTask.clicked.connect(self.delete_selected_task)
        self.task.returnPressed.connect(self.add_task_to_list)

        self.task_model = TaskListModel()
        self.tasks.setModel(self.task_model)
        self.tasks.setItemDelegate(TaskDelegate())

        # Fetch tasks from database
        self.fetch_tasks_from_db()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("To-do List Sample Application", "To-do List Sample Application"))
        self.title.setText(_translate("MainWindow", "To-do List"))
        self.task.setPlaceholderText(_translate("MainWindow", "Input a task"))
        self.addTask.setText(_translate("MainWindow", "Add"))
        self.tasksLabel.setText(_translate("MainWindow", "Tasks:"))
        self.deleteTask.setText(_translate("MainWindow", "Delete Task"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose_App.setText(_translate("MainWindow", "Close App"))

    def add_task_to_list(self):
        # Get text from task 
        task_text = self.task.text()
        if task_text:
            # Get date and time
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Inserttask 
            cursor = self.db_connection.cursor()
            query = "INSERT INTO tasks (task_text, created_at) VALUES (%s, %s)"
            cursor.execute(query, (task_text, current_date))
            self.db_connection.commit()
            cursor.close()

            # Append the task and date 
            self.task_model.append((task_text, current_date))
            self.task.clear()

    def delete_selected_task(self):
        indexes = self.tasks.selectedIndexes()
        if indexes:
            rows = [index.row() for index in indexes]

            cursor = self.db_connection.cursor()
            for row in sorted(rows, reverse=True):
                task_text, _ = self.task_model.tasks[row]
                query = "DELETE FROM tasks WHERE task_text = %s"
                cursor.execute(query, (task_text,))
                self.task_model.remove(row)
            self.db_connection.commit()
            cursor.close()

    def fetch_tasks_from_db(self):
        # Fetch all tasks from database
        cursor = self.db_connection.cursor()
        query = "SELECT task_text, created_at FROM tasks"
        cursor.execute(query)
        tasks = cursor.fetchall()

        for task in tasks:
            task_text, created_at = task
            self.task_model.append((task_text, created_at))

        cursor.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

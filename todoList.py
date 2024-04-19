from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        spacerItem = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
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

        # Connect addTask button clicked signal to a function
        self.addTask.clicked.connect(self.add_task_to_list)

        # Connect deleteTask button clicked signal to a function
        self.deleteTask.clicked.connect(self.delete_selected_task)

        # Initialize a custom model for the tasks QListView
        self.task_model = TaskListModel()
        self.tasks.setModel(self.task_model)
        self.tasks.setItemDelegate(TaskDelegate())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "To-do List"))
        self.task.setPlaceholderText(_translate("MainWindow", "Input a task"))
        self.addTask.setText(_translate("MainWindow", "Add"))
        self.tasksLabel.setText(_translate("MainWindow", "Tasks:"))
        self.deleteTask.setText(_translate("MainWindow", "Delete Task"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose_App.setText(_translate("MainWindow", "Close App"))

    def add_task_to_list(self):
        # Get the text from the task QLineEdit
        task_text = self.task.text()
        if task_text:
            # Get the current date and time
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Append the task and its date to the model
            self.task_model.append((task_text, current_date))
            # Clear the task QLineEdit
            self.task.clear()

    def delete_selected_task(self):
        # Get the selected indexes from the QListView
        indexes = self.tasks.selectedIndexes()
        if indexes:
            # Get the row numbers of the selected items
            rows = [index.row() for index in indexes]
            # Remove the selected tasks from the model
            for row in sorted(rows, reverse=True):
                self.task_model.remove(row)


class TaskListModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(TaskListModel, self).__init__(parent)
        self.tasks = []

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            task, date = self.tasks[index.row()]
            return f"{task} - {date}"

        if role == QtCore.Qt.EditRole:
            return self.tasks[index.row()][0]

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            self.tasks[index.row()] = (value, self.tasks[index.row()][1])
            self.dataChanged.emit(index, index)
            return True
        return False

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.tasks)

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''Write a python program which opens a window with a red button.
When the button is pressed the computer overheats and self-destructs.''' 



import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt")
        self.setStyleSheet("background-color: red")

        self.button = QtGui.QPushButton("Dangerous Button", self)
        self.button.clicked.connect(self.destruct)

        self.show()

    def destruct(self):
        choice = QtGui.QMessageBox.question(self, 'Warning',
                                            "Are you sure you want to self-destruct?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            self.close()
            sys.exit()
        else:
            pass

def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

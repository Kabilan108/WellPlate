"""Filename: MainWindow.py"""
"""Main WIndow-Style Application"""

# Import necessary modules & libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

# * Create the class `Window` that inherits from `QMainWindow`
class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        """Iniitializer"""
        super().__init__(parent)
        # Set Window title
        self.setWindowTitle("QMainWindow")
        # Add central widget
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        # * Call private methods in the lines that follow to create different
        # * GUI elements:
        self._createMenu() # main menu
        self._createToolBar() # toolbar
        self._createStatusBar() # status bar

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
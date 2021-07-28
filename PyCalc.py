#!/home/kabilan/anaconda3/envs/pyTutorials/bin/python
"""Filename: PyCalc.py"""

"""PyCalc is a simple calculator built using Python and PyQt5"""

import sys

# Imposrt QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
# We'll use QGridLayout to arrange the buttons
from PyQt5.QtWidgets import QGridLayout
# This will be used for the calculator display
from PyQt5.QtWidgets import QLineEdit
# We'll use this for the calculator buttons
from PyQt5.QtWidgets import QPushButton
# We'll use QVBoxLayout to organize the calculator's general layout.
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
# We'lluse this to connect signals to methods that need extra arguments
from functools import partial

# Define prtoject variables
__version__ = "0.1"
__author__ = "Tony Kabilan Okeke"

#* Create a subclass of QMainWindow to set up the calculator's GUI
class PyCalcUI(QMainWindow):
    """PyCalc's View (GUI)"""

    def __init__(self):
        """View Initializer"""
        super().__init__()
        # Set main window properties
        self.setWindowTitle("pyCalc")
        self.setFixedSize(235, 235)
        # Set the central widget and create the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the diosplay and buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the Calculator Display"""
        # Create the display widget usiing a QLineEdit object.
        self.display = QLineEdit()
        # Set display properties
        self.display.setFixedHeight(35) # Fixed height = 35 px
        self.display.setAlignment(Qt.AlignRight) # Left-aligned
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the Calculator Buttons"""
        #* We'll use a dictionary to hold each button's text and position on the grid.
        #* We'll use QGridLayout to arrange the buttons on the calculator's window
        # Cerate empty dictionary to hold buttons.
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #* Button Text | Grid Position
        # Create temporary dictionary to stroe their labels and relative positions.
        buttons = {
                   "7": (0,0),
                   "8": (0,1),
                   "9": (0,2),
                   "/": (0,3),
                   "C": (0,4),
                   "4": (1,0),
                   "5": (1,1),
                   "6": (1,2),
                   "*": (1,3),
                   "(": (1,4),
                   "1": (2,0),
                   "2": (2,1),
                   "3": (2,2),
                   "-": (2,3),
                   ")": (2,4),
                   "0": (3,0),
                   "00": (3,1),
                   ".": (3,2),
                   "+": (3,3),
                   "=": (3,4)
                   }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40,40)
            buttonsLayout.addWidget(self.buttons[btnText],
                                    pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    # Next, we need to add methods that will allow us to update the information in the display.
    # The next three methods will complete the GUI public interface and complete the view class
    # for the calculator
    def setDisplayText(self, text):
        """Set display text"""
        # Set & update display text
        self.display.setText(text)
        # Set the cursor's focus on the display
        self.display.setFocus()

    def displayText(self):
        """Get display's text"""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display"""
        self.setDisplayText("")

#! Controller Class
# Next, we'll create the calculator's controller class. THis class will connect the view to the model.
# We'll use the controller class to make the calculator perform actions in response to user events.
# We'll use `functools.partial()` to connect signals with methods that need to take extra arguments.
# The controller class needs to perform three main tasks:
#   1. Acces the GUI's public interface
#   2. Handle the creation of math expressions
#   3.  Connect button `clicked` signals with the appropriate slots
class PyCalcCtrl:
    """PyCalc Controller class"""
    def __init__(self, view):
        """Controller Initializer"""
        # First, we git PyCalcCtrl an instance of the view PyCalcUI.
        # We'll use this instance to gain full access to view's public interface
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        """Build expression"""
        # We'll use this to handle the creation of math expressions.
        # This method also updates the calculator's display in response to user input
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots"""
        # Finally, this will connect the *printable* buttons with ._buildExpression().
        # This will let us create math expressions by clicking calculator buttons
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        # Here, we connect the clear button (C)  to ._view.clearDisplay() to erase display text.
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)

# Finally, we need to implement the calculator's model to allow the equals sign to work (=)


# Client Side code: Main Fucntion
def main():
    """Main function"""
    # Create an insance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator GUI
    view = PyCalcUI()
    view.show()
    # To make the controller class work, we need to create instances of the model
    # and the controller
    # This will initialize the controller and connect the signals and slots.
    PyCalcCtrl(view=view)
    # Execute main loop
    sys.exit(pycalc.exec())

# Run Condition
if __name__ == "__main__":
    main()
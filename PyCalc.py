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

# Client Side code: Main Fucntion
def main():
    """Main function"""
    # Create an insance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator GUI
    view = PyCalcUI()
    view.show()
    # Execute main loop
    sys.exit(pycalc.exec())

# Run Condition
if __name__ == "__main__":
    main()
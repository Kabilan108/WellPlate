"""Filename: View.py"""

"""
    The requisute classes for implementing the GUI are defined here.
    For WellPlate, the classes and methods defined here will allow for the
    creation of the plate interfaces as well as any auxilliary dialogs and
    interfaces necessary.
"""

# Import necessary modules
import imp
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtGui import QIcon

# Import qrc resources module
# Generated using `pyrcc5 -o qrc_resources.py resources.qrc`
import qrc_resources

# * Welcome Dialog Class
class Welcome(QDialog):
    """WellPlate's Welcome Dialog"""

    def __init__(self, parent: QWidget = None):
        """Dialog Initializer"""
        super().__init__(parent)

        # Set Dialog properties
        self.setWindowTitle("Welcome")
        self.setFixedSize(150, 150)

        # Create Dialog Layout
        Layout = QVBoxLayout()

        # Add Logo placeholder
        Layout.addWidget(QLabel("<h1>WellPlate</h1>"))

        # Create and add button layout
        Layout.addWidget(QPushButton("New Plate"))
        Layout.addWidget(QPushButton("Load Plate"))

        # Set Dialog layut
        self.setLayout(Layout)

class WellModal(QWidget):
    """Modal Pop-Up for Well Interfaces"""

    def __init__(self, parent=None):
        """Modal Initializer"""
        super().__init__(parent)
        # Create Form Layout
        self.Layout = QFormLayout()
        self.Layout.addRow("Sample ID:", QLineEdit())
        self.Layout.addRow("Volume:", QLineEdit())
        # Add Sample Type Selector box
        sampleType = QComboBox()
        sampleType.addItem("Serum")
        sampleType.addItem("DNA")
        sampleType.addItem("RNA")
        sampleType.addItem("NGS Library")
        sampleType.addItem("Other")
        self.Layout.addRow("Sample Type:", sampleType)
        # Nucleic acid-specific options
        self.Layout.addRow("Concentration (ng/uL)", QLineEdit())
        self.Layout.addRow("A260:A280", QLineEdit())
        self.Layout.addRow("A260:A230", QLineEdit())

class Well96(QMainWindow):
    """Interace for 96-Well Plates"""

    def __init__(self):
        """View Initializer"""
        super().__init__()
        # Set Window properties
        self.setWindowTitle("WellPlate: 96-Well Plate")
        # Set central widget and add general layout
        self.MainLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.MainLayout)
        # Create Plate Layout Buttons
        self.createPlate()
        # Add menu bar arn toolbars
        self.createActions()
        self.createMenuBar()
        self.createToolBars()

    def createActions(self):
        # File Actions
        self.newAction = QAction(QIcon(":file-new.svg"), "&New",self)
        self.openAction = QAction(QIcon(":file-open.svg"), "&Open",self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save",self)
        self.exitAction = QAction("Exit", self)
        # Find actions
        self.findAction = QAction("Find", self)
        self.replaceAction = QAction("Replace", self)
        # Help actions
        self.helpContentAction = QAction(QIcon(":help-content.svg"),
                                         "&Help Action", self)
        self.aboutAction = QAction("About", self)

    def createMenuBar(self):
        menuBar = self.menuBar()
        # File Menu
        fileMenu = menuBar.addMenu("File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Find menu
        findMenu = menuBar.addMenu("Find")
        findMenu.addAction(self.findAction)
        findMenu.addAction(self.replaceAction)
        # Help menu
        helpMenu = menuBar.addMenu("Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def createToolBars(self):
        # File Toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addSeparator()
        fileToolBar.setMovable(False)

    def createPlate(self):
        """Create Plate Layout Buttons"""
        # Create dictionary to hold buttons
        self.Wells = {}
        wellLayout = QGridLayout()
        # Button Text | Grid Position
        buttons = {
                   " ": (0,0),  "1": (0,1),  "2": (0,2),  "3": (0,3),  "4": (0,4),  "5": (0,5),  "6": (0,6),  "7": (0,7),  "8": (0,8),  "9": (0,9),  "10": (0,10),  "11": (0,11),  "12": (0,12),
                   "A": (1,0), "A1": (1,1), "A2": (1,2), "A3": (1,3), "A4": (1,4), "A5": (1,5), "A6": (1,6), "A7": (1,7), "A8": (1,8), "A9": (1,9), "A10": (1,10), "A11": (1,11), "A12": (1,12),
                   "B": (2,0), "B1": (2,1), "B2": (2,2), "B3": (2,3), "B4": (2,4), "B5": (2,5), "B6": (2,6), "B7": (2,7), "B8": (2,8), "B9": (2,9), "B10": (2,10), "B11": (2,11), "B12": (2,12),
                   "C": (3,0), "C1": (3,1), "C2": (3,2), "C3": (3,3), "C4": (3,4), "C5": (3,5), "C6": (3,6), "C7": (3,7), "C8": (3,8), "C9": (3,9), "C10": (3,10), "C11": (3,11), "C12": (3,12),
                   "D": (4,0), "D1": (4,1), "D2": (4,2), "D3": (4,3), "D4": (4,4), "D5": (4,5), "D6": (4,6), "D7": (4,7), "D8": (4,8), "D9": (4,9), "D10": (4,10), "D11": (4,11), "D12": (4,12),
                   "E": (5,0), "E1": (5,1), "E2": (5,2), "E3": (5,3), "E4": (5,4), "E5": (5,5), "E6": (5,6), "E7": (5,7), "E8": (5,8), "E9": (5,9), "E10": (5,10), "E11": (5,11), "E12": (5,12),
                   "F": (6,0), "F1": (6,1), "F2": (6,2), "F3": (6,3), "F4": (6,4), "F5": (6,5), "F6": (6,6), "F7": (6,7), "F8": (6,8), "F9": (6,9), "F10": (6,10), "F11": (6,11), "F12": (6,12),
                   "G": (7,0), "G1": (7,1), "G2": (7,2), "G3": (7,3), "G4": (7,4), "G5": (7,5), "G6": (7,6), "G7": (7,7), "G8": (7,8), "G9": (7,9), "G10": (7,10), "G11": (7,11), "G12": (7,12),
                   "H": (8,0), "H1": (8,1), "H2": (8,2), "H3": (8,3), "H4": (8,4), "H5": (8,5), "H6": (8,6), "H7": (8,7), "H8": (8,8), "H9": (8,9), "H10": (8,10), "H11": (8,11), "H12": (8,12)
                   }
        # Create buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            if 0 in pos:
                self.Wells[btnText] = QLabel(btnText)
                self.Wells[btnText].setAlignment(Qt.AlignCenter)
                self.Wells[btnText].setFixedSize(30,30)
            else:
                self.Wells[btnText] = QPushButton(btnText)
                self.Wells[btnText].setFixedSize(30,30)
            wellLayout.addWidget(self.Wells[btnText],
                                 pos[0], pos[1])
        # Add Well Layout to the Main Layout
        self.MainLayout.addLayout(wellLayout)
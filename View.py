"""Filename: View.py"""

"""
    The requisute classes for implementing the GUI are defined here.
    For WellPlate, the classes and methods defined here will allow for the
    creation of the plate interfaces as well as any auxilliary dialogs and
    interfaces necessary.
"""

# Import necessary modules
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

# Import qrc resources module
# Generated using `pyrcc5 -o qrc_resources.py resources.qrc`
import qrc_resources

# * Main Window Class
class MainWindow(QMainWindow):
    """Application's Main Window"""

    def __init__(self):
        """Class Initializer"""

        super().__init__()
        # Set window properties
        self.setWindowTitle("Welcome to WellPlate")
        self.setFixedSize(300, 250)
        # Create base layout for window, and assign central widget
        self.baseLayout = QVBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.baseLayout)
        self.setCentralWidget(self.centralWidget)
        # Create Start-up buttons
        self.createStartUpBtns()

    def createStartUpBtns(self):
        """Create Start-Up Buttons"""

        self.StartUpBtns = {}

        # Create `new 94` button and set style
        self.StartUpBtns["new94"] = QPushButton("New 94-Well Plate")
        self.StartUpBtns["new94"].setFixedHeight(50)
        self.StartUpBtns["new94"].setStyleSheet(
                                    "font-size: 16px; font-weight: bold; background-color: grey")
        self.baseLayout.addWidget(self.StartUpBtns["new94"])

        # Create `new 384` button and set style
        self.StartUpBtns["new384"] = QPushButton("New 384-Well Plate")
        self.StartUpBtns["new384"].setFixedHeight(50)
        self.StartUpBtns["new384"].setStyleSheet(
                                    "font-size: 16px; font-weight: bold; background-color: grey")
        self.baseLayout.addWidget(self.StartUpBtns["new384"])

        # Create `load` button and set style
        self.StartUpBtns["load"] = QPushButton("Load Plate Layout")
        self.StartUpBtns["load"].setFixedHeight(50)
        self.StartUpBtns["load"].setStyleSheet(
                                    "font-size: 16px; font-weight: bold; background-color: grey")
        self.baseLayout.addWidget(self.StartUpBtns["load"])

    def createActions(self):
        """Create Actions for the Menus and Toolbars"""

        # File actions
        self.action_new = QAction(QIcon(":file-new.svg"), "&New", self)
        self.action_open = QAction(QIcon(":file-open.svg"), "&Open", self)
        self.action_save = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.action_exit = QAction("Exit", self)

        # Find actions
        self.action_find = QAction("Find", self)
        self.action_replace = QAction("Replace", self)

        # Help actions
        self.action_helpContent = QAction(QIcon(":help-content.svg"), "&Help Action", self)
        self.action_about = QAction("About", self)

    def createMenus(self):
        """Create Menus"""

        menu = self.menuBar()

        # File menu
        menu_file = menu.addMenu("File")
        menu_file.addAction(self.action_new)
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addSeparator()
        menu_file.addAction(self.action_exit)

        # Find menu
        menu_find = menu.addMenu("Find")
        menu_find.addAction(self.action_find)
        menu_find.addAction(self.action_replace)

        # Help menu
        menu_help = menu.addMenu("Help")
        menu_help.addAction(self.action_helpContent)
        menu_help.addAction(self.action_about)

    def createToolBars(self):
        """Create ToolBars"""

        # File toolbar
        toolBar_file = self.addToolBar("File")
        toolBar_file.addAction(self.action_new)
        toolBar_file.addAction(self.action_open)
        toolBar_file.addAction(self.action_save)
        toolBar_file.addSeparator()
        toolBar_file.setMovable(False)

    def sampleFormPopUp(self):
        """Pop-Up Form for Sample Information"""

        # Create widget instance
        self.sample = QWidget()

        # Set window properties
        self.sample.setWindowTitle("Please Enter Sample Information")
        self.sample.setFixedSize(400, 400)

        # Create form layout
        formLayout = QFormLayout()

        self.SampleID = QLineEdit()
        formLayout.addRow("Sample ID:", self.SampleID)

        self.SampleVol = QLineEdit()
        formLayout.addRow("Volume (uL):", self.SampleVol)

        self.SampleType = QComboBox()
        self.SampleType.addItems(["Serum", "DNA", "RNA", "NGS Library", "Other"])
        formLayout.addRow("Sample Type:", self.SampleType)

        self.SampleConc = QLineEdit()
        formLayout.addRow("Concentration (ng/uL):", self.SampleConc)

        self.SampleDescr = QTextEdit()
        formLayout.addRow("Sample Description:", self.SampleDescr)

        # Add `Save Button`
        self.SampleSaveBtn = QPushButton("Save Sample")
        self.SampleSaveBtn.setStyleSheet("""background-color: green; font-size: 15px""")
        formLayout.addRow(self.SampleSaveBtn)

        # Add form layout to widget
        self.sample.setLayout(formLayout)

        # Show pop-up
        self.sample.show()

# * 96-Well Plate Interface Clas
class Plate96(QWidget):
    """Interface for 96-Well Plates"""

    def __init__(self):
        """View Initializer"""
        super().__init__()
        # Create 96-well interface
        self.createPlate()

    def createPlate(self):
        """Create Plate Layout Interface"""

        # Create dictionary to hold buttons
        self.Wells = {}
        # Create grid layout for wells (buttons)
        wellLayout = QGridLayout()

        # Create dictionary to store well names (button texts)
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

        # Create wells (buttons) and add them to the grid layout
        for txt, pos in buttons.items():
            if 0 in pos:
                self.Wells[txt] = QLabel(txt)
                self.Wells[txt].setAlignment(Qt.AlignCenter)
                self.Wells[txt].setFixedSize(50, 30)
                self.Wells[txt].setStyleSheet("""background-color: white; font-weight: bold;
                                                 font-size: 20px""")
            else:
                self.Wells[txt] = QPushButton(txt)
                self.Wells[txt].setFixedSize(50, 30)
                self.Wells[txt].setStyleSheet("background-color: grey; font-size: 14px")
            # Set style for empty cell
            self.Wells[" "].setStyleSheet("background-color: none")
            # Add button/label to layout
            wellLayout.addWidget(self.Wells[txt], pos[0], pos[1])
        # Add button layout to base well layout
        self.setLayout(wellLayout)

# * 384-Well Plate Interface Class
class Plate384(QWidget):
    """Interface for 384-Well Plates"""

    def __init__(self):
        super().__init__()
        # Create 384-well interface
        self.createPlate()

    def createPlate(self):
        """Create Plate Layout Interface"""

        # Create dictionary to hold buttons
        self.Wells = {}
        # Create grid layout for wells (buttons)
        wellLayout = QGridLayout()

        # Create dictionary to store well names (button texts)
        buttons = {
                   " ": (0,0),   "1": (0,1),   "2": (0,2),   "3": (0,3),   "4": (0,4),   "5": (0,5),   "6": (0,6),   "7": (0,7),   "8": (0,8),   "9": (0,9),   "10": (0,10),   "11": (0,11),   "12": (0,12),   "13": (0,13),   "14": (0,14),   "15": (0,15),   "16": (0,16),   "17": (0,17),   "18": (0,18),   "19": (0,19),   "20": (0,20),   "21": (0,21),   "22": (0,22),   "23": (0,23),  " 24": (0,24),
                   "A": (1,0),  "A1": (1,1),  "A2": (1,2),  "A3": (1,3),  "A4": (1,4),  "A5": (1,5),  "A6": (1,6),  "A7": (1,7),  "A8": (1,8),  "A9": (1,9),  "A10": (1,10),  "A11": (1,11),  "A12": (1,12),  "A13": (1,13),  "A14": (1,14),  "A15": (1,15),  "A16": (1,16),  "A17": (1,17),  "A18": (1,18),  "A19": (1,19),  "A20": (1,20),  "A21": (1,21),  "A22": (1,22),  "A23": (1,23), " A24": (1,24),
                   "B": (2,0),  "B1": (2,1),  "B2": (2,2),  "B3": (2,3),  "B4": (2,4),  "B5": (2,5),  "B6": (2,6),  "B7": (2,7),  "B8": (2,8),  "B9": (2,9),  "B10": (2,10),  "B11": (2,11),  "B12": (2,12),  "B13": (2,13),  "B14": (2,14),  "B15": (2,15),  "B16": (2,16),  "B17": (2,17),  "B18": (2,18),  "B19": (2,19),  "B20": (2,20),  "B21": (2,21),  "B22": (2,22),  "B23": (2,23), " B24": (2,24),
                   "C": (3,0),  "C1": (3,1),  "C2": (3,2),  "C3": (3,3),  "C4": (3,4),  "C5": (3,5),  "C6": (3,6),  "C7": (3,7),  "C8": (3,8),  "C9": (3,9),  "C10": (3,10),  "C11": (3,11),  "C12": (3,12),  "C13": (3,13),  "C14": (3,14),  "C15": (3,15),  "C16": (3,16),  "C17": (3,17),  "C18": (3,18),  "C19": (3,19),  "C20": (3,20),  "C21": (3,21),  "C22": (3,22),  "C23": (3,23), " C24": (3,24),
                   "D": (4,0),  "D1": (4,1),  "D2": (4,2),  "D3": (4,3),  "D4": (4,4),  "D5": (4,5),  "D6": (4,6),  "D7": (4,7),  "D8": (4,8),  "D9": (4,9),  "D10": (4,10),  "D11": (4,11),  "D12": (4,12),  "D13": (4,13),  "D14": (4,14),  "D15": (4,15),  "D16": (4,16),  "D17": (4,17),  "D18": (4,18),  "D19": (4,19),  "D20": (4,20),  "D21": (4,21),  "D22": (4,22),  "D23": (4,23), " D24": (4,24),
                   "E": (5,0),  "E1": (5,1),  "E2": (5,2),  "E3": (5,3),  "E4": (5,4),  "E5": (5,5),  "E6": (5,6),  "E7": (5,7),  "E8": (5,8),  "E9": (5,9),  "E10": (5,10),  "E11": (5,11),  "E12": (5,12),  "E13": (5,13),  "E14": (5,14),  "E15": (5,15),  "E16": (5,16),  "E17": (5,17),  "E18": (5,18),  "E19": (5,19),  "E20": (5,20),  "E21": (5,21),  "E22": (5,22),  "E23": (5,23), " E24": (5,24),
                   "F": (6,0),  "F1": (6,1),  "F2": (6,2),  "F3": (6,3),  "F4": (6,4),  "F5": (6,5),  "F6": (6,6),  "F7": (6,7),  "F8": (6,8),  "F9": (6,9),  "F10": (6,10),  "F11": (6,11),  "F12": (6,12),  "F13": (6,13),  "F14": (6,14),  "F15": (6,15),  "F16": (6,16),  "F17": (6,17),  "F18": (6,18),  "F19": (6,19),  "F20": (6,20),  "F21": (6,21),  "F22": (6,22),  "F23": (6,23), " F24": (6,24),
                   "G": (7,0),  "G1": (7,1),  "G2": (7,2),  "G3": (7,3),  "G4": (7,4),  "G5": (7,5),  "G6": (7,6),  "G7": (7,7),  "G8": (7,8),  "G9": (7,9),  "G10": (7,10),  "G11": (7,11),  "G12": (7,12),  "G13": (7,13),  "G14": (7,14),  "G15": (7,15),  "G16": (7,16),  "G17": (7,17),  "G18": (7,18),  "G19": (7,19),  "G20": (7,20),  "G21": (7,21),  "G22": (7,22),  "G23": (7,23), " G24": (7,24),
                   "H": (8,0),  "H1": (8,1),  "H2": (8,2),  "H3": (8,3),  "H4": (8,4),  "H5": (8,5),  "H6": (8,6),  "H7": (8,7),  "H8": (8,8),  "H9": (8,9),  "H10": (8,10),  "H11": (8,11),  "H12": (8,12),  "H13": (8,13),  "H14": (8,14),  "H15": (8,15),  "H16": (8,16),  "H17": (8,17),  "H18": (8,18),  "H19": (8,19),  "H20": (8,20),  "H21": (8,21),  "H22": (8,22),  "H23": (8,23), " H24": (8,24),
                   "I": (9,0),  "I1": (9,1),  "I2": (9,2),  "I3": (9,3),  "I4": (9,4),  "I5": (9,5),  "I6": (9,6),  "I7": (9,7),  "I8": (9,8),  "I9": (9,9),  "I10": (9,10),  "I11": (9,11),  "I12": (9,12),  "I13": (9,13),  "I14": (9,14),  "I15": (9,15),  "I16": (9,16),  "I17": (9,17),  "I18": (9,18),  "I19": (9,19),  "I20": (9,20),  "I21": (9,21),  "I22": (9,22),  "I23": (9,23), " I24": (9,24),
                   "J": (10,0), "J1": (10,1), "J2": (10,2), "J3": (10,3), "J4": (10,4), "J5": (10,5), "J6": (10,6), "J7": (10,7), "J8": (10,8), "J9": (10,9), "J10": (10,10), "J11": (10,11), "J12": (10,12), "J13": (10,13), "J14": (10,14), "J15": (10,15), "J16": (10,16), "J17": (10,17), "J18": (10,18), "J19": (10,19), "J20": (10,20), "J21": (10,21), "J22": (10,22), "J23": (10,23), "J24": (10,24),
                   "K": (11,0), "K1": (11,1), "K2": (11,2), "K3": (11,3), "K4": (11,4), "K5": (11,5), "K6": (11,6), "K7": (11,7), "K8": (11,8), "K9": (11,9), "K10": (11,10), "K11": (11,11), "K12": (11,12), "K13": (11,13), "K14": (11,14), "K15": (11,15), "K16": (11,16), "K17": (11,17), "K18": (11,18), "K19": (11,19), "K20": (11,20), "K21": (11,21), "K22": (11,22), "K23": (11,23), "K24": (11,24),
                   "L": (12,0), "L1": (12,1), "L2": (12,2), "L3": (12,3), "L4": (12,4), "L5": (12,5), "L6": (12,6), "L7": (12,7), "L8": (12,8), "L9": (12,9), "L10": (12,10), "L11": (12,11), "L12": (12,12), "L13": (12,13), "L14": (12,14), "L15": (12,15), "L16": (12,16), "L17": (12,17), "L18": (12,18), "L19": (12,19), "L20": (12,20), "L21": (12,21), "L22": (12,22), "L23": (12,23), "L24": (12,24),
                   "M": (13,0), "M1": (13,1), "M2": (13,2), "M3": (13,3), "M4": (13,4), "M5": (13,5), "M6": (13,6), "M7": (13,7), "M8": (13,8), "M9": (13,9), "M10": (13,10), "M11": (13,11), "M12": (13,12), "M13": (13,13), "M14": (13,14), "M15": (13,15), "M16": (13,16), "M17": (13,17), "M18": (13,18), "M19": (13,19), "M20": (13,20), "M21": (13,21), "M22": (13,22), "M23": (13,23), "M24": (13,24),
                   "N": (14,0), "N1": (14,1), "N2": (14,2), "N3": (14,3), "N4": (14,4), "N5": (14,5), "N6": (14,6), "N7": (14,7), "N8": (14,8), "N9": (14,9), "N10": (14,10), "N11": (14,11), "N12": (14,12), "N13": (14,13), "N14": (14,14), "N15": (14,15), "N16": (14,16), "N17": (14,17), "N18": (14,18), "N19": (14,19), "N20": (14,20), "N21": (14,21), "N22": (14,22), "N23": (14,23), "N24": (14,24),
                   "O": (15,0), "O1": (15,1), "O2": (15,2), "O3": (15,3), "O4": (15,4), "O5": (15,5), "O6": (15,6), "O7": (15,7), "O8": (15,8), "O9": (15,9), "O10": (15,10), "O11": (15,11), "O12": (15,12), "O13": (15,13), "O14": (15,14), "O15": (15,15), "O16": (15,16), "O17": (15,17), "O18": (15,18), "O19": (15,19), "O20": (15,20), "O21": (15,21), "O22": (15,22), "O23": (15,23), "O24": (15,24),
                   "P": (16,0), "P1": (16,1), "P2": (16,2), "P3": (16,3), "P4": (16,4), "P5": (16,5), "P6": (16,6), "P7": (16,7), "P8": (16,8), "P9": (16,9), "P10": (16,10), "P11": (16,11), "P12": (16,12), "P13": (16,13), "P14": (16,14), "P15": (16,15), "P16": (16,16), "P17": (16,17), "P18": (16,18), "P19": (16,19), "P20": (16,20), "P21": (16,21), "P22": (16,22), "P23": (16,23), "P24": (16,24)
                   }

        # Create wells (buttons) anda dd them to the grid layout
        for txt, pos in buttons.items():
            if 0 in pos:
                self.Wells[txt] = QLabel(txt)
                self.Wells[txt].setAlignment(Qt.AlignCenter)
                self.Wells[txt].setFixedSize(50, 30)
                self.Wells[txt].setStyleSheet("""background-color: white; font-weight: bold;
                                                 font-size: 20px""")
            else:
                self.Wells[txt] = QPushButton(txt)
                self.Wells[txt].setFixedSize(50, 30)
                self.Wells[txt].setStyleSheet("background-color: grey; font-size: 14px")
            # Add button/label to layout
            wellLayout.addWidget(self.Wells[txt], pos[0], pos[1])
        # Add button layout to base well layout
        self.setLayout(wellLayout)
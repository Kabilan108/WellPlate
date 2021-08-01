"""
    Filename: Controller.py

    The controller connects the model and view to allow this Application to
    function as desired.
    User events (and requests) - from the *view* - are sent to the *controller*
    which assigns tasks to the *model* accordingly.
    Once the *model* delivers the requested result, the *controller* forwards
    it back to the *view* (GUI).

    For WellPlate, the controller will receive user input and interactions with
    the plate interface (*view*), provide these inputs to the *model* which
    will deal with them as necessary, and will then update the GUI - as well
    as any associated data files / databases accordingly.
"""

# Import libraries and modules
from PyQt5.QtWidgets import *
from functools import partial
from View import *
from Model import *

# For generating random colors
from random import randint

class PlateCtrl:
    """Controller Class for WellPlate"""

    def __init__(self, model, view):
        """Class Initializer"""

        # First, we need to get an instance of the view
        # This instance will allow access to the view's public interface
        self.view = view
        self.model = model
        # Connect Signals and slots
        self.connectStartUpSignals()

    def launch94Plate(self):
        """Launch 94-Well Plate Interface"""

        # Set window properties
        self.view.setWindowTitle("WellPlate: 94-Well Plate")
        self.view.setFixedSize(800, 500)
        # Create menus and toolbars
        self.view.createActions()
        self.view.createMenus()
        self.view.createToolBars()
        # Create plate layout and set is as the central widget
        self.plateLayout = Plate96()
        self.view.setCentralWidget(self.plateLayout)
        # Connect signals and slots
        self.connectActions()
        # Connect Plate Buttons
        self.connectWells()

    def launch384Plate(self):
        """Launch 384-Well Plate Interface"""

        # Set window properties
        self.view.setWindowTitle("WellPlate: 384-Well Plate")
        self.view.setFixedSize(1400, 800)
        # Create menus and toolbars
        self.view.createActions()
        self.view.createMenus()
        self.view.createToolBars()
        # Create plate layout and set is as the central widget
        self.plateLayout = Plate384()
        self.view.setCentralWidget(self.plateLayout)
        # Connect signals and slots
        self.connectActions()
        # Connect Plate Buttons
        self.connectWells()

    def loadPlate(self):
        """Load Saved Plate Interface"""

        # Generate random color hex code
        r = lambda: randint(0,255)
        # Give button a random color
        self.view.StartUpBtns["load"].setStyleSheet(
                                        """font-size: 16px; font-weight: bold;
                                           background-color: #%02X%02X%02X""" % (r(), r(), r()))

    def terminate(self):
        """Terminate Application"""
        self.view.close()

    def connectStartUpSignals(self):
        """Connect Signals and Slots"""

        # Connect Start-Up Buttons
        self.view.StartUpBtns["new94"].clicked.connect(self.launch94Plate)
        self.view.StartUpBtns["new384"].clicked.connect(self.launch384Plate)
        self.view.StartUpBtns["load"].clicked.connect(self.loadPlate)

    def connectActions(self):
        """Connect Menu and ToolBar Actions"""

        # Connect menu actions
        self.view.action_exit.triggered.connect(self.terminate)

    def connectWells(self):
        """Connect Wells (Buttons) to the Sample Pop-Up Method"""

        # Connect signals for all buttons
        for txt, btn in self.plateLayout.Wells.items():
            if isinstance(btn, QPushButton):
                btn.clicked.connect(partial(self.view.sampleForm, txt))


    # def connectSignals(self):
    #     """Connect signals and slots"""

    #     # Connect signals to welcome buttons
    #     self.view.StartUpBtns["new94"].clicked.connect(self.launch94Plate)
    #     self.view.StartUpBtns["new384"].clicked.connect(self.launch384Plate)
    #     self.view.StartUpBtns["load"].clicked.connect(self.loadPlate)

        # Connect signals to Well buttons
        # for btnText, btn in self.view.Wells.items():
        #     if isinstance(btn, QPushButton):
        #         btn.clicked.connect(partial(self.wellPopUp, btnText, view))

    # def wellPopUp(self, btnText, view):
    #     """Initialize a Pop-Up Window on Btn Clicked"""
    #     print("Button CLicked")
    #     PopUp = WellModal(parent=view)
    #     PopUp.setWindowTitle(btnText)
    #     PopUp.setGeometry(0,0,100,30)
    #     PopUp.show()
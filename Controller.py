"""Filename: Controller.py"""

"""
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
from PyQt5.QtWidgets import QPushButton
from functools import partial
from View import *

class PlateCtrl:
    """Controller Class for WellPlate"""
    def __init__(self, view, model):
        """Controller Initializer"""
        # First, we need to get an instance of the view
        # This instance will allow access to the view's public interface
        self.view = view
        #self.evaluate = model
        # Connect Signals and slots
        self.connectSignals(view = self.view)

    def wellPopUp(self, btnText, view):
        """Initialize a Pop-Up Window on Btn Clicked"""
        print("Button CLicked")
        PopUp = WellModal(parent=view)
        PopUp.setWindowTitle(btnText)
        PopUp.setGeometry(0,0,100,30)
        PopUp.show()

    def connectSignals(self, view):
        """Connect signals and slots"""
        for btnText, btn in self.view.Wells.items():
            if isinstance(btn, QPushButton):
                btn.clicked.connect(partial(self.wellPopUp, btnText, view))
#!/home/kabil/.anaconda3/envs/py-env/bin/python
"""
    Filename: WellPlate.py

    WellPlate is designed to allow for seamless management of 96-well and
    384-well plates by providing a user-friendly GUI.

    WellPlate was developed based on the Model View Controller design pattern.
    In summary, the MVC pattern for GUI applications consists of:
        - The user performing an action or request (event) on the view(GUI)
        - The view notifies the controller about the user's action.
        - The controller gets the user's request and queries the model for
          a response.
        - The model processes the controller querry, performs the required
          operations, and returns an answer or result.
        - The controller receives the model's answer and updates the view accordingly.
        - The user finnally sees the requested result as an update on the view.
"""

# Import modules
from PyQt6.QtWidgets import QApplication
import controller as ctrl
import view
import model
import sys

# Define Main Loop
def main():
    """WellPlate Main Function"""

    wellplate = QApplication(sys.argv)
    app_view = view.MainWindow()
    app_view.show()
    app_ctrl = ctrl.PlateCtrl(view=app_view, model=None)
    
    # Execute main loop
    sys.exit(wellplate.exec())

if __name__ == "__main__":
    main()
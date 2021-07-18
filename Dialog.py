"""Filename: Dialog.py"""
"""Dialog-Sytle Application"""

# Import necssary modules & libraries
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

# * Create a full class `Dialog` for the GUI, which inherits from `QDialog`
class Dialog(QDialog):
    """Dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("QDialog")

        # Assign `QVBoxLayout` object to `dlgLayout`.
        dlgLayout = QVBoxLayout()
        # Assign `QVFormLayout` object to `formLayout`.
        formLayout = QFormLayout()

        # Add widgets to `formLayout`
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())

        # Use `dlgLayout` to arrange all the widgets on the form.
        dlgLayout.addLayout(formLayout)

        # Create object to place the dialog buttons.
        btns = QDialogButtonBox()
        # Add two standard buttons: `OK` and `Cancel`
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

# * Wrap code in an `if __name__ == '__main__':` idiom
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
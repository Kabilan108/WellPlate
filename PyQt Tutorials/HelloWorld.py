""" Filename: HelloWorld.py """
""" Here we'll be creating a "Hello, World!" application with Python and PyQt. """
# TODO:
#   1. Import `QApplication` and all the required widgets from `PyQt5.QWidgets`
#   2. Create an insance of `QApplication`
#   3. Create an instance of the application's GUI
#   4. Show your application's GUI.
#   5. Run the application's event loop (main loop).

# TODO: 1. Import `QApplication` and all the required widgets from `PyQt5.QWidgets`
# Import `sys` to handle the exit status of the application
import sys

# Import specific Qt Widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# TODO: 2. Create an insance of `QApplication`
# `sys.argv` contains the list of command-line arguments passed into the script.
# If no arguments are going to be passed to the script, `sys.argv` can be replaced with []
# The `QApplication` object does a lot of initialization, so it shoudl be created before
# any of the other widgets.
app = QApplication(sys.argv)

# TODO: 3. Create an instance of the application's GUI.
# In this application, `window` is an instance of `QWidget`, which provides all the features
# needed to create the application's window.
window = QWidget()
# The window title can be set using `.setWindowTitle()`
window.setWindowTitle("PyQt5 App")
# `.setGeometry(x, y, width, height)` is used to define the size of the window and where it
# is placed on the screen.
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
# The `QLabel` widget object can accept HTML text, so we can use HTML tags to format an H1
# header. Next, `.move()` is used to set the widget position in the application window.
hellowMsg = QLabel("<h1>Hello World!</h1>", parent=window)
hellowMsg.move(60, 15)

# * NOTE:
#   In PyQt5, any widgtet (subclass of `QWidget`) can be used as a top-level window, or even
#   a button or label. The only condition is that no `parent` is passed to it.
#   When a widget is used like this, PyQt5 automatically adds a title bar and turns it into
#   a normal window.
#   The parent-child relationship is used for two complementary purposes:
#       1.  A widget that doesn't have a `parent` is a *main window* or *top-level window*
#       2.  A widget that has a `parent` is contained/shown within its `parent`
#   This relationship defines *ownership*, with parents owning their children.
#   The PyQt5 ownership model ensures that id a `parent` object is deleted, then all its
#   children (widgets) are automatically deleted as well.
#   To avoid memory leaks, ensure that ALL `QWidget` objects have a `parent` except the
#   top-level window.

# TODO: 4. Show application GUI
# Calling `.show()` schedules a *paint* event. In other words, it adds a new event to the
# application's event queue.
# * A paint event is a request for paintinf the widgets that compose a GUI.
window.show()

# TODO: 5. Run application's event loop (main loop)
# The application's event loop is started by calling `app.exec_()`.
# This call is wrapped in a call to `sys.exit()` which allows you to cleanly exit Python
# and release memory resources when the application terminates.
sys.exit(app.exec_())
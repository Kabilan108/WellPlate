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
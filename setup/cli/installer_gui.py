from PySimpleGUI import *

def create_window(title: str, layout: list) -> Window :
    return Window(title=title, layout=layout)
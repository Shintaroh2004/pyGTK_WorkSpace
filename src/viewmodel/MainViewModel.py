import gi

from model.MainModel import MainModel

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainViewModel():
    def __init__(self):
        self.model:MainModel = MainModel()

    def on_button_clicked(self,widget:Gtk.Button):
        widget.set_label("Clicked!!")
        self.model.fetch_all()
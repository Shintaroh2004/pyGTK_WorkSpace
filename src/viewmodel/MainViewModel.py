import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainViewModel():
    def on_button_clicked(self,widget:Gtk.Button):
        widget.set_label("Clicked!!")
import gi

from viewmodel.MainViewModel import MainViewModel

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello GTK3")

        self.viewModel = MainViewModel()

        self.set_default_size(600,400)

        self.button = Gtk.Button(label="button")
        self.button.connect("clicked",self.viewModel.on_button_clicked)
        self.add(self.button)

        self.connect("destroy", Gtk.main_quit)

    def main(self):
        Gtk.main()
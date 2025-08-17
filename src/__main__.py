from viewmodel.MainViewModel import MainViewModel
from view.MianWindow import MainWindow

vm = MainViewModel()
win = MainWindow(vm)
win.show_all()
win.main()
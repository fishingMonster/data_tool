import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from source import _auto_ui_gen_
class data_tool_ui(_auto_ui_gen_.Ui_MainWindow):
    def __init__(self,main_window):
        super(data_tool_ui,self).__init__()
        self.setupUi(main_window)
        self.add_func()

    def add_func(self):
        self.select_file_button.clicked.connect(self.file_button_func)

    def file_button_func(self):
        file_paths=QFileDialog.getOpenFileNames()[0]
        file_strs = str()
        for str_item in file_paths:
            file_strs = file_strs+str_item+';'
        self.file_lineEdit.setText(file_strs)
        self.

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    main_window=QtWidgets.QMainWindow()
    ui=data_tool_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
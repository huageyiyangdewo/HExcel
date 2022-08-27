import logging

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_main import Ui_MainWindow

logging.basicConfig(level=logging.INFO,
                    filename="handle_excel.log",
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )



# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        self.directory_path = None
        self.file_path = None

    def handle(self):

        self.ui.directoryButton.clicked.connect(self.find_directory)
        self.ui.fileButton.clicked.connect(self.find_file)
        self.ui.processButton.clicked.connect(self.calc)

    def find_directory(self):
        self.directory_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        self.ui.directoryLineText.setText(self.directory_path)

    def find_file(self):
        self.file_path = QFileDialog.getOpenFileName(self, "请选择配置文件")[0]
        if self.file_path.find(".xlsx") == -1:
            QMessageBox.about(self,
                              "温馨提示",
                              "请选择配置文件后缀为: .xlsx "
                              )
        else:
            self.ui.fileLineText.setText(self.file_path)


    def calc(self):
        if self.file_path is None or self.directory_path is None:
            t = ""
            if self.directory_path is None:
                t += "请选择需要处理的文件夹"

            if self.file_path is None:
                if len(t) == 0:
                    t += "请选择配置文件"
                else:
                    t += ",配置文件"
            QMessageBox.about(self,
                              "温馨提示",
                              t
                              )

        from calc import HandleExcel
        from utils import ParseConf

        p = ParseConf(self.file_path)
        is_ok, c = p.parse()
        if is_ok is False:
            # 配置文件格式有问题
            QMessageBox.about(self,
                              "温馨提示",
                              c
                              )

        h = HandleExcel(c, self.directory_path)
        h.handle(self.ui.progressBar)

        # self.ui.progressBar.setValue(math.ceil((HANDLE_COUNTS/COUNTS)*100))
        # self.ui.progressBar.setValue(math.ceil(100))


if __name__ == "__main__":

    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    mainw.handle()
    app.exec_()
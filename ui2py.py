from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog,QFileDialog,
        QDialogButtonBox, QFrame, QGroupBox, QLabel, QLineEdit, QListWidget,
        QTabWidget, QVBoxLayout, QWidget)
#窗体文件
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 79)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtPath = QtWidgets.QLineEdit(Dialog)
        self.txtPath.setObjectName("txtPath")
        self.gridLayout.addWidget(self.txtPath, 0, 0, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(Dialog)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn2py = QtWidgets.QPushButton(Dialog)
        self.btn2py.setObjectName("btn2py")
        self.verticalLayout.addWidget(self.btn2py)

        self.retranslateUi(Dialog)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ui2py"))
        self.btnBrowse.setText(_translate("Dialog", "浏览..."))
        self.btn2py.setText(_translate("Dialog", "生成.py文件"))

#逻辑文件
class Dialog(QtWidgets.QDialog,Ui_Dialog):  
    def __init__(self):  
        super(Dialog,self).__init__()  
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.setOpenFileName)   #槽函数不用加括号
        self.btn2py.clicked.connect(self.makeUi2Py)
        
    def setOpenFileName(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                "选择Ui文件", self.txtPath.text(),
                "Ui Files (*.ui);;All Files (*)", options=options)
        if fileName:
            self.txtPath.setText(fileName)

    def delLastChar(s, num):
        strList = list(s)
        strList.pop()
        return "".join(strList)

    def makeUi2Py(self):
        import os
        
        strUiPath = self.txtPath.text()
        strPyPath = strUiPath[:-2] + "py"
        print(strUiPath)
        print(strPyPath)
        #调用cmd,第行最后加"& \"换行
        command = '''
    		C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat {0} -o {1} & \
    		pause
    		'''.format(strUiPath, strPyPath)
        os.system(command)
        
if __name__=="__main__":
    import sys  
  
    app = QtWidgets.QApplication(sys.argv)  
    dialog = Dialog()  
    dialog.show()  
    sys.exit(app.exec_())


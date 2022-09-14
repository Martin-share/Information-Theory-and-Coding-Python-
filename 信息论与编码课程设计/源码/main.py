'''
Descripttion: 
version: 
Author: Martin
FilePath: \Martin_Code\Python\信息论\main.py
Date: 2022-06-27 14:18:33
LastEditTime: 2022-07-02 11:10:49
'''

import Huffman
import run_length2
import fano
import signal
import bmp_huffman
from Ui_main import Ui_lhy2020210593
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_lhy2020210593()
        self.ui.setupUi(self)
        #五个按钮
        self.ui.pushButton_1.clicked.connect(self.btn1) #哈夫曼
        self.ui.pushButton_2.clicked.connect(self.btn2) #Fano
        self.ui.pushButton_3.clicked.connect(self.btn3) #游程
        self.ui.pushButton_4.clicked.connect(self.btn4) #算数
        self.ui.pushButton_5.clicked.connect(self.btn5)
        #self.ui.textEdit_1.setText('123') #写入
    
    #哈夫曼
    def btn1(self):
        # 读取字符串
        text = self.ui.textEdit_1.toPlainText()
        print(text)
        nodes,huffman_str,huffman_final_str,huffman_efficiency = Huffman.main(text)
        ret = ''
        for node in nodes:
            ret+=node.name+':'+node.sign_str+'\n'
        self.ui.textEdit_2.setText(ret) #写入
        self.ui.textEdit_3.setText(huffman_str) #写入
        self.ui.textEdit_4.setText(huffman_final_str) #写入
        self.ui.textEdit_5.setText(huffman_efficiency) #写入
    
    #Fano
    def btn2(self):
        # 读取字符串
        text = self.ui.textEdit_1.toPlainText()
        print(text)
        nodes,fano_str,fano_final_str,fano_efficiency = fano.main(text)
        ret = ''
        for node in nodes:
            ret+=node.name+':'+node.sign_str+'\n'
        self.ui.textEdit_2.setText(ret) #写入
        self.ui.textEdit_3.setText(fano_str) #写入
        self.ui.textEdit_4.setText(fano_final_str) #写入
        self.ui.textEdit_5.setText(fano_efficiency) #写入

    #游程    
    def btn3(self):
        # 读取字符串
        text = self.ui.textEdit_1.toPlainText()
        print(text)
        run_length_str,final_str,efficiency = run_length2.main(text)

        self.ui.textEdit_2.setText('') #写入
        self.ui.textEdit_3.setText(run_length_str) #写入
        self.ui.textEdit_4.setText(final_str) #写入
        self.ui.textEdit_5.setText(efficiency) #写入
    
    #算数
    def btn4(self):
        # 读取字符串
        text = self.ui.textEdit_1.toPlainText()
        print(text)
        singal_str,singal_final_str,singal_efficiency = signal.main(text)
        self.ui.textEdit_2.setText('') #写一个空的，擦除
        self.ui.textEdit_3.setText(singal_str) #写入
        self.ui.textEdit_4.setText(singal_final_str) #写入
        self.ui.textEdit_5.setText(singal_efficiency) #写入
    
    # Huffman+游程
    def btn5(self):
        # 此处路径要改变
        fname = QFileDialog.getOpenFileName(self, 'Open file', '')
        # print(fname) #('E:/ctf/铁人三项.md', 'All Files (*)')
        # print(fname[0]) # E:/code.txt
        image_list,nodes,mul_str,final_str,efficiency = bmp_huffman.main(fname[0])
        ret = ''
        for node in nodes:
            ret+=str(node.name)+':'+node.sign_str+'\n'
        print('正在写入到界面')
        ret2 = ''
        for item in image_list:
            ret2+= str(item)
        print(ret2)
        self.ui.textEdit_1.setText(ret2) #写入
        self.ui.textEdit_2.setText(ret) #写入
        self.ui.textEdit_3.setText(mul_str) #写入
        self.ui.textEdit_4.setText(final_str) #写入
        self.ui.textEdit_5.setText('') #写入

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec_())



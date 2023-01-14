# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/splash_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(682, 206)
        Dialog.setMinimumSize(QtCore.QSize(682, 203))
        Dialog.setMaximumSize(QtCore.QSize(682, 206))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.lbl_groundtruth_dir_2 = QtWidgets.QLabel(Dialog)
        self.lbl_groundtruth_dir_2.setGeometry(QtCore.QRect(10, 0, 521, 201))
        self.lbl_groundtruth_dir_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_groundtruth_dir_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_groundtruth_dir_2.setLineWidth(4)
        self.lbl_groundtruth_dir_2.setWordWrap(True)
        self.lbl_groundtruth_dir_2.setObjectName("lbl_groundtruth_dir_2")
        self.btn_Close = QtWidgets.QPushButton(Dialog)
        self.btn_Close.setGeometry(QtCore.QRect(550, 110, 111, 81))
        self.btn_Close.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_Close.setObjectName("btn_Close")

        self.retranslateUi(Dialog)
        self.btn_Close.clicked.connect(Dialog.btn_close_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information"))
        self.lbl_groundtruth_dir_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:8pt;\">1. Basic tool comes from<br/></span><span style=\" font-size:8pt; font-weight:600;\">A Comparative Analysis of Object Detection Metrics with a Companion Open-Source Toolkit<br/></span><span style=\" font-size:8pt;\">Authors: Rafael Padilla, Wesley L. Passos, Thadeu L. B. Dias, Sergio L. Netto, Eduardo A. B. da Silva. Journal: Electronics V. 10, Year: 2021, ISSN: 2079-9292, DOI: 10.3390/electronics10030279<br/></span><a href=\"https://github.com/rafaelpadilla/review_object_detection_metrics\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/rafaelpadilla/review_object_detection_metrics<br/></span></a><a href=\"https://github.com/rafaelpadilla/review_object_detection_metrics\"><span style=\" font-size:8pt; color:#000000;\">2.[20220502] ZX update this tool to add f1score, maxf1score, maxf1score_confidenceThresh results output and display them also in P-R curve, besides, support ourself annotation format(similiar with COCO V1 format, but no image width, height info under images node.</span></a></p></body></html>"))
        self.btn_Close.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_Close.setText(_translate("Dialog", "Close"))

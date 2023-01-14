# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/details_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1294, 873)
        self.lbl_sample_image = QtWidgets.QLabel(Dialog)
        self.lbl_sample_image.setGeometry(QtCore.QRect(500, 30, 771, 761))
        self.lbl_sample_image.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_sample_image.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_sample_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sample_image.setObjectName("lbl_sample_image")
        self.txb_statistics = QtWidgets.QTextEdit(Dialog)
        self.txb_statistics.setGeometry(QtCore.QRect(10, 30, 471, 381))
        self.txb_statistics.setReadOnly(True)
        self.txb_statistics.setObjectName("txb_statistics")
        self.lbl_groundtruth_dir_5 = QtWidgets.QLabel(Dialog)
        self.lbl_groundtruth_dir_5.setGeometry(QtCore.QRect(10, 10, 161, 17))
        self.lbl_groundtruth_dir_5.setObjectName("lbl_groundtruth_dir_5")
        self.btn_plot_bb_per_classes = QtWidgets.QPushButton(Dialog)
        self.btn_plot_bb_per_classes.setGeometry(QtCore.QRect(110, 420, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.btn_plot_bb_per_classes.setFont(font)
        self.btn_plot_bb_per_classes.setStyleSheet("background-color: rgb(6, 243, 255);")
        self.btn_plot_bb_per_classes.setObjectName("btn_plot_bb_per_classes")
        self.btn_save_image = QtWidgets.QPushButton(Dialog)
        self.btn_save_image.setGeometry(QtCore.QRect(910, 800, 141, 61))
        self.btn_save_image.setStyleSheet("")
        self.btn_save_image.setObjectName("btn_save_image")
        self.lbl_image_file_name = QtWidgets.QLabel(Dialog)
        self.lbl_image_file_name.setGeometry(QtCore.QRect(540, 9, 681, 21))
        self.lbl_image_file_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image_file_name.setObjectName("lbl_image_file_name")
        self.chb_gt_bb = QtWidgets.QCheckBox(Dialog)
        self.chb_gt_bb.setGeometry(QtCore.QRect(510, 800, 161, 22))
        self.chb_gt_bb.setObjectName("chb_gt_bb")
        self.chb_det_bb = QtWidgets.QCheckBox(Dialog)
        self.chb_det_bb.setGeometry(QtCore.QRect(710, 800, 141, 22))
        self.chb_det_bb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chb_det_bb.setObjectName("chb_det_bb")
        self.btn_previous_image = QtWidgets.QPushButton(Dialog)
        self.btn_previous_image.setGeometry(QtCore.QRect(1090, 800, 71, 61))
        self.btn_previous_image.setObjectName("btn_previous_image")
        self.btn_next_image = QtWidgets.QPushButton(Dialog)
        self.btn_next_image.setGeometry(QtCore.QRect(1180, 800, 71, 61))
        self.btn_next_image.setObjectName("btn_next_image")
        self.frame_12 = QtWidgets.QFrame(Dialog)
        self.frame_12.setGeometry(QtCore.QRect(30, 480, 438, 131))
        self.frame_12.setStyleSheet("border-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.lbl_detections_dir_6 = QtWidgets.QLabel(self.frame_12)
        self.lbl_detections_dir_6.setGeometry(QtCore.QRect(70, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detections_dir_6.setFont(font)
        self.lbl_detections_dir_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_detections_dir_6.setObjectName("lbl_detections_dir_6")
        self.dsb_IOU_threshold_for_objdet_confusematrix = QtWidgets.QDoubleSpinBox(self.frame_12)
        self.dsb_IOU_threshold_for_objdet_confusematrix.setGeometry(QtCore.QRect(100, 40, 81, 27))
        self.dsb_IOU_threshold_for_objdet_confusematrix.setMaximum(1.0)
        self.dsb_IOU_threshold_for_objdet_confusematrix.setSingleStep(0.01)
        self.dsb_IOU_threshold_for_objdet_confusematrix.setProperty("value", 0.5)
        self.dsb_IOU_threshold_for_objdet_confusematrix.setObjectName("dsb_IOU_threshold_for_objdet_confusematrix")
        self.lbl_IOU_thresh_2 = QtWidgets.QLabel(self.frame_12)
        self.lbl_IOU_thresh_2.setGeometry(QtCore.QRect(10, 40, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lbl_IOU_thresh_2.setFont(font)
        self.lbl_IOU_thresh_2.setObjectName("lbl_IOU_thresh_2")
        self.dsb_conf_threshold_for_objdet_confusematrix = QtWidgets.QDoubleSpinBox(self.frame_12)
        self.dsb_conf_threshold_for_objdet_confusematrix.setGeometry(QtCore.QRect(320, 40, 81, 27))
        self.dsb_conf_threshold_for_objdet_confusematrix.setMaximum(1.0)
        self.dsb_conf_threshold_for_objdet_confusematrix.setSingleStep(0.01)
        self.dsb_conf_threshold_for_objdet_confusematrix.setProperty("value", 0.53)
        self.dsb_conf_threshold_for_objdet_confusematrix.setObjectName("dsb_conf_threshold_for_objdet_confusematrix")
        self.lbl_IOU_thresh_3 = QtWidgets.QLabel(self.frame_12)
        self.lbl_IOU_thresh_3.setGeometry(QtCore.QRect(220, 40, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lbl_IOU_thresh_3.setFont(font)
        self.lbl_IOU_thresh_3.setObjectName("lbl_IOU_thresh_3")
        self.btn_plot_objdet_confusematrix = QtWidgets.QPushButton(self.frame_12)
        self.btn_plot_objdet_confusematrix.setGeometry(QtCore.QRect(80, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.btn_plot_objdet_confusematrix.setFont(font)
        self.btn_plot_objdet_confusematrix.setStyleSheet("background-color: rgb(6, 243, 255);\n"
"background-color: rgb(255, 196, 17);")
        self.btn_plot_objdet_confusematrix.setObjectName("btn_plot_objdet_confusematrix")
        self.dsb_IOU_threshold_for_objdet_confusematrix.raise_()
        self.lbl_IOU_thresh_2.raise_()
        self.lbl_detections_dir_6.raise_()
        self.dsb_conf_threshold_for_objdet_confusematrix.raise_()
        self.lbl_IOU_thresh_3.raise_()
        self.btn_plot_objdet_confusematrix.raise_()
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 460, 481, 21))
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 620, 481, 20))
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_detections_dir_3 = QtWidgets.QLabel(Dialog)
        self.lbl_detections_dir_3.setGeometry(QtCore.QRect(40, 646, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detections_dir_3.setFont(font)
        self.lbl_detections_dir_3.setObjectName("lbl_detections_dir_3")
        self.comb_displayClass = QtWidgets.QComboBox(Dialog)
        self.comb_displayClass.setGeometry(QtCore.QRect(180, 640, 201, 31))
        self.comb_displayClass.setObjectName("comb_displayClass")
        self.txb_statistics_forcurimg = QtWidgets.QTextEdit(Dialog)
        self.txb_statistics_forcurimg.setGeometry(QtCore.QRect(30, 680, 431, 181))
        self.txb_statistics_forcurimg.setReadOnly(True)
        self.txb_statistics_forcurimg.setObjectName("txb_statistics_forcurimg")
        self.frame_13 = QtWidgets.QFrame(Dialog)
        self.frame_13.setGeometry(QtCore.QRect(530, 799, 151, 31))
        self.frame_13.setStyleSheet("border-color: rgb(0, 255, 0);\n"
"border-style: solid;\n"
"border-width: 3px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_15 = QtWidgets.QFrame(Dialog)
        self.frame_15.setGeometry(QtCore.QRect(730, 799, 131, 31))
        self.frame_15.setStyleSheet("border-color: rgb(255,0, 0);\n"
"border-style: solid;\n"
"border-width: 3px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")

        self.retranslateUi(Dialog)
        self.btn_plot_bb_per_classes.clicked.connect(Dialog.btn_plot_bb_per_classes_clicked)
        self.btn_save_image.clicked.connect(Dialog.btn_save_image_clicked)
        self.btn_previous_image.clicked.connect(Dialog.btn_previous_image_clicked)
        self.btn_next_image.clicked.connect(Dialog.btn_next_image_clicked)
        self.chb_gt_bb.clicked['bool'].connect(Dialog.chb_gt_bb_clicked)
        self.chb_det_bb.clicked['bool'].connect(Dialog.chb_det_bb_clicked)
        self.btn_plot_objdet_confusematrix.clicked.connect(Dialog.btn_plot_objdet_confusematrix_clicked)
        self.comb_displayClass.currentTextChanged['QString'].connect(Dialog.comb_displayClass_changed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bounding-boxes statistics"))
        self.lbl_sample_image.setText(_translate("Dialog", "[image]"))
        self.txb_statistics.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">* 53392 bounding boxes were found in 12345 images.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">* In 33 images no bounding boxes were found.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">* The average area of the bounding boxes is 1212 pixels.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">* The amount of bounding boxes per class is:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">[car]: 123 bounding boxes in 23 images.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">[person]: 231 bounding boxes in 93 images.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">[dog]: 231 bounding boxes in 90 images.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">[cat]: 231 bounding boxes in 393 images.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">(ordenar classes por ordem alfabética)</span></p></body></html>"))
        self.lbl_groundtruth_dir_5.setText(_translate("Dialog", "Statistics:"))
        self.btn_plot_bb_per_classes.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_plot_bb_per_classes.setText(_translate("Dialog", "plot bounding boxes per class"))
        self.btn_save_image.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_save_image.setText(_translate("Dialog", "save"))
        self.lbl_image_file_name.setText(_translate("Dialog", "no image to show"))
        self.chb_gt_bb.setText(_translate("Dialog", "draw groundtruths"))
        self.chb_det_bb.setText(_translate("Dialog", "draw detections"))
        self.btn_previous_image.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_previous_image.setText(_translate("Dialog", "<<"))
        self.btn_next_image.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_next_image.setText(_translate("Dialog", ">>"))
        self.lbl_detections_dir_6.setText(_translate("Dialog", "objDet confusion matrix"))
        self.lbl_IOU_thresh_2.setText(_translate("Dialog", "IOU threshold:"))
        self.lbl_IOU_thresh_3.setText(_translate("Dialog", "Conf threshold:"))
        self.btn_plot_objdet_confusematrix.setToolTip(_translate("Dialog", "The configurations will be applied in a random ground truth image."))
        self.btn_plot_objdet_confusematrix.setText(_translate("Dialog", "plot objDet confusion matrix"))
        self.lbl_detections_dir_3.setText(_translate("Dialog", "display class:"))
        self.txb_statistics_forcurimg.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Current image:<br />- [car]: 12 gt boxes, 20 gt boxes</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- [person]: 12 gt boxes, 20 gt boxes</p></body></html>"))

import os
import random

import cv2
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox
from src.bounding_box import BoundingBox
from src.ui.details_ui import Ui_Dialog as Details_UI
from src.utils import general_utils
from src.utils.enumerators import BBType
from src.utils.general_utils import (add_bb_into_image, get_files_dir,
                                     remove_file_extension,
                                     show_image_in_qt_component)
import numpy as np
from src.utils.plot_confusionmatrix import plot_confusion_matrix, plot_confusion_matrix_2
from src.utils.enumerators import BBFormat, BBType, CoordinatesType
from datetime import datetime as dt
# ------------------ [ zx add start ] ------------------
from sys import path
cm_module_folder = os.path.join(os.path.dirname(__file__), "..", "..", "..", "object_detection_confusion_matrix")
path.append(cm_module_folder)
import confusion_matrix
from  confusion_matrix import ConfusionMatrix as ObjDetConfusionMatrix
# ------------------ [ zx add end ] ------------------

class Details_Dialog(QMainWindow, Details_UI):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # initialize variables
        self.dir_images = ''
        self.gt_annotations = None
        self.det_annotations = None
        self.allclass_dict = None
        self.text_statistics = '<b>#TYPE_BB#:</b><br>'
        self.text_statistics += '<br>* A total of <b>#TOTAL_BB#</b> bounding boxes were found in <b>#TOTAL_IMAGES#</b> images.'
        self.text_statistics += '<br>* The average area of the bounding boxes is <b>#AVERAGE_AREA_BB#</b> pixels.'
        self.text_statistics += '<br>* The amount of bounding boxes per class is:'
        self.text_statistics += '<br>#AMOUNT_BB_PER_CLASS#'
        self.lbl_sample_image.setScaledContents(True)
        # set maximum and minimum size
        self.setMaximumHeight(self.height())
        self.setMaximumWidth(self.width())
        # set selected image based on the list of images
        self.selected_image_index = 0

        self.statistics_forcurimg = '<b>#Current image#:</b><br>'
        self.statistics_forcurimg += '<br><b>#TOTAL_GTBOXS#</b> gt boxes, <b>#TOTAL_DETBOXS#</b> det boxes.'
        self.statistics_forcurimg += '<br>#AMOUNT_BB_PER_CLASS#'

        self.cur_imgFilePath, self.cur_gtbox_num,  self.cur_detbox_num,  self.cur_gtbox_distribution, \
        self.cur_detbox_distribution, self.cur_gt_bboxes, self.cur_det_bboxes = \
            None, None, None, None, None, None, None

    def initialize_ui(self):
        # clear all information
        self.txb_statistics.setText('')
        self.lbl_sample_image.setText('')
        self.btn_previous_image.setEnabled(False)
        self.btn_next_image.setEnabled(False)
        # Create text with ground truth statistics
        if self.type_bb == BBType.GROUND_TRUTH:
            stats = self.text_statistics.replace('#TYPE_BB#', 'Ground Truth')
            self.annot_obj = self.gt_annotations
        elif self.type_bb == BBType.DETECTED:
            stats = self.text_statistics.replace('#TYPE_BB#', 'Detections')
            self.annot_obj = self.det_annotations
        self.chb_det_bb.setVisible(False)
        self.chb_gt_bb.setVisible(False)
        if self.det_annotations is not None and self.det_annotations != []:
            self.chb_det_bb.setVisible(True)
        if self.gt_annotations is not None and self.gt_annotations != []:
            self.chb_gt_bb.setVisible(True)
        stats = stats.replace('#TOTAL_BB#', str(len(self.annot_obj)))
        stats = stats.replace('#TOTAL_IMAGES#', str(BoundingBox.get_total_images(self.annot_obj)))
        stats = stats.replace('#AVERAGE_AREA_BB#',
                              '%.2f' % BoundingBox.get_average_area(self.annot_obj))
        # Get amount of bounding boxes per class
        self.bb_per_class = BoundingBox.get_amount_bounding_box_all_classes(self.annot_obj)
        amount_bb_per_class = 'No class found'
        if len(self.bb_per_class) > 0:
            amount_bb_per_class = ''
            longest_class_name = len(max(self.bb_per_class.keys(), key=len))
            for c, amount in self.bb_per_class.items():
                c = c.ljust(longest_class_name, ' ')
                amount_bb_per_class += f'   {c} : {amount}<br>'
        stats = stats.replace('#AMOUNT_BB_PER_CLASS#', amount_bb_per_class)
        self.txb_statistics.setText(stats)

        # get first image file and show it
        if os.path.isdir(self.dir_images):
            self.image_files = get_files_dir(
                self.dir_images, extensions=['jpg', 'jpge', 'png', 'bmp', 'tiff', 'tif'])
            if len(self.image_files) > 0:
                self.selected_image_index = 0
            else:
                self.selected_image_index = -1
        else:
            self.image_files = []
            self.selected_image_index = -1

        # insert items into combo box
        self.comb_displayClass.addItem("all")
        for id, desc in self.allclass_dict.items():
            self.comb_displayClass.addItem(desc)

        if (self.selected_image_index >= 0):
            self.cur_imgFilePath, self.cur_gtbox_num,  self.cur_detbox_num, \
             self.cur_gtbox_distribution, self.cur_detbox_distribution, self.cur_gt_bboxes, self.cur_det_bboxes =\
                self.load_bbs(self.selected_image_index)

        self.show_image()


    def load_bbs(self, imgidx):

        detbox_num, gtbox_num = 0, 0
        gtbox_distribution, detbox_distribution = {}, {}
        gt_bboxes, det_bboxes = None, None

        # Get bounding boxes of the loaded image
        img_name = self.image_files[imgidx]
        img_name = general_utils.get_file_name_only(img_name)

        if self.gt_annotations is not None:
            gt_bboxes = BoundingBox.get_bounding_boxes_by_image_name(self.gt_annotations, img_name)
            gtbox_num = len(gt_bboxes)
            for bb in gt_bboxes:
                label = bb.get_class_id()
                if gtbox_distribution.get(label, None) is None: gtbox_distribution[label] = 0
                gtbox_distribution[label] += 1

        if self.det_annotations is not None:
            det_bboxes = BoundingBox.get_bounding_boxes_by_image_name(self.det_annotations, img_name)
            detbox_num = len(det_bboxes)
            for bb in det_bboxes:
                label = bb.get_class_id()
                if detbox_distribution.get(label, None) is None: detbox_distribution[label] = 0
                detbox_distribution[label] += 1

        return self.image_files[imgidx], gtbox_num, detbox_num, gtbox_distribution, detbox_distribution, gt_bboxes, det_bboxes


    def show_image(self):
        if self.selected_image_index not in range(len(self.image_files)):
            self.btn_save_image.setEnabled(False)
            self.chb_gt_bb.setEnabled(False)
            self.chb_det_bb.setEnabled(False)
            self.lbl_sample_image.clear()
            self.lbl_image_file_name.setText('no image to show')
            return
        # Get all annotations and detections from this file
        if self.annot_obj is not None:
            # If Ground truth, bb will be drawn in green, red otherwise
            self.btn_previous_image.setEnabled(True)
            self.btn_next_image.setEnabled(True)
            self.btn_save_image.setEnabled(True)
            self.chb_gt_bb.setEnabled(True)
            self.chb_det_bb.setEnabled(True)
            self.lbl_image_file_name.setText(f'{self.selected_image_index}/{len(self.image_files)}: {self.cur_imgFilePath}')

            displayClassLabel = self.comb_displayClass.currentText()
            print("displayClassLabel = ", displayClassLabel)

            # Draw bounding boxes
            self.loaded_image = self.draw_bounding_boxes([displayClassLabel] if displayClassLabel != 'all' else None)
            if self.loaded_image is None:
                QMessageBox.warning(self, "Warning!", "当前图片打不开！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                return

            # Show image
            show_image_in_qt_component(self.loaded_image, self.lbl_sample_image)

            self.update_txb_statistics_forcurimg(self.cur_imgFilePath,
                                                 self.cur_gtbox_num, self.cur_detbox_num,
                                                 self.cur_gtbox_distribution, self.cur_detbox_distribution)

    def draw_bounding_boxes(self, displayClassLabel_list = None ):

        # Load image to obtain a clean image (without BBs)
        img_path = os.path.join(self.dir_images, self.cur_imgFilePath)

        # ---------------------------------------------------------------
        # [20220502] zx modified below codes to support chinese-filepath image
        # ---------------------------------------------------------------
        # img = cv2.imread(img_path)
        # ---------------------------------------------------------------
        try:
            img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)  # use opencv read from image of chinese filepath
        except Exception as e:
            return None

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Add bounding box`x`xes depending if the item is checked
        if self.chb_gt_bb.isChecked() and self.gt_annotations is not None:
            bboxes = self.cur_gt_bboxes

            # Draw bounding boxes
            for bb in bboxes:
                # label = None
                label = bb.get_class_id()
                if (displayClassLabel_list is not None and (label not in displayClassLabel_list)):
                    continue
                img = add_bb_into_image(img, bb,
                                        box_thickness=1,
                                        box_color=(0, 255, 0),
                                        text_font=cv2.FONT_HERSHEY_SIMPLEX,
                                        text_color=(255, 0, 0),
                                        text_thickness=1,
                                        text_fontscale=0.6,
                                        label=label)

        if self.chb_det_bb.isChecked() and self.det_annotations is not None:
            bboxes = self.cur_det_bboxes

            # Draw bounding boxes
            for bb in bboxes:
                # label = None
                label = bb.get_class_id()
                if (displayClassLabel_list is not None and (label not in displayClassLabel_list)):
                    continue
                img = add_bb_into_image(img, bb,
                                        box_thickness=1,
                                        box_color=(0, 0, 255),
                                        text_font=cv2.FONT_HERSHEY_SIMPLEX,
                                        text_color=(255, 0, 255),
                                        text_thickness=1,
                                        text_fontscale=0.6,
                                        label=label)

        return img

    def show_dialog(self, type_bb, gt_annotations=None, det_annotations=None, gt_version=None, det_version=None, allclass_dict=None, dir_images=None):
        self.type_bb = type_bb
        self.gt_annotations = gt_annotations
        self.det_annotations = det_annotations
        self.allclass_dict = allclass_dict
        self.gt_version = gt_version
        self.det_version = det_version
        self.dir_images = dir_images
        self.initialize_ui()
        self.show()

    def btn_plot_bb_per_classes_clicked(self):
        # dict_bbs_per_class = BoundingBox.get_amount_bounding_box_all_classes(gt_bbs, reverse=True)
        general_utils.plot_bb_per_classes(self.bb_per_class,
                                          horizontally=False,
                                          rotation=90,
                                          show=True)
        # plt.close()
        # plt.bar(self.bb_per_class.keys(), self.bb_per_class.values())
        # plt.xlabel('classes')
        # plt.ylabel('amount of bounding boxes')
        # plt.xticks(rotation=45)
        # plt.title('Bounding boxes per class')
        # fig = plt.gcf()
        # fig.canvas.set_window_title('Object Detection Metrics')
        # fig.show()

    # def btn_load_random_image_clicked(self):
    #     self.load_random_image()

    def btn_next_image_clicked(self):
        # If reached the last image, set index to start over
        if self.selected_image_index == len(self.image_files) - 1:
            self.selected_image_index = 0
        else:
            self.selected_image_index += 1

        if (self.selected_image_index >= 0):
            self.cur_imgFilePath, self.cur_gtbox_num,  self.cur_detbox_num, \
             self.cur_gtbox_distribution, self.cur_detbox_distribution, self.cur_gt_bboxes, self.cur_det_bboxes = \
                self.load_bbs(self.selected_image_index)

        self.show_image()

    def btn_previous_image_clicked(self):
        if self.selected_image_index == 0:
            self.selected_image_index = len(self.image_files) - 1
        else:
            self.selected_image_index -= 1

        if (self.selected_image_index >= 0):
            self.cur_imgFilePath, self.cur_gtbox_num,  self.cur_detbox_num, \
             self.cur_gtbox_distribution, self.cur_detbox_distribution, self.cur_gt_bboxes, self.cur_det_bboxes = \
                self.load_bbs(self.selected_image_index)

        self.show_image()

    def btn_save_image_clicked(self):
        dict_formats = {
            'PNG Image (*.png)': 'png',
            'JPEG Image (*.jpg, *.jpeg)': 'jpg',
            'TIFF Image (*.tif, *.tiff)': 'tif'
        }
        formats = ';;'.join(dict_formats.keys())
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, file_extension = QFileDialog.getSaveFileName(self,
                                                                "Save Image File",
                                                                "",
                                                                formats,
                                                                options=options)
        if file_name != '':
            # the extension was not informed, so add it
            if '.' not in file_name:
                file_name = file_name + '.' + dict_formats[file_extension]
            cv2.imwrite(file_name, cv2.cvtColor(self.loaded_image, cv2.COLOR_RGB2BGR))

    def chb_det_bb_clicked(self, state):
        displayClassLabel = self.comb_displayClass.currentText()
        # Draw bounding boxes
        self.loaded_image = self.draw_bounding_boxes([displayClassLabel] if displayClassLabel != 'all' else None)
        if self.loaded_image  is None:
            QMessageBox.warning(self, "Warning!", "当前图片打不开！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        # Show image
        show_image_in_qt_component(self.loaded_image, self.lbl_sample_image)

        self.update_txb_statistics_forcurimg(self.cur_imgFilePath,
                                             self.cur_gtbox_num, self.cur_detbox_num,
                                             self.cur_gtbox_distribution, self.cur_detbox_distribution)

    def chb_gt_bb_clicked(self, state):
        displayClassLabel = self.comb_displayClass.currentText()
        # Draw bounding boxes
        self.loaded_image = self.draw_bounding_boxes([displayClassLabel] if displayClassLabel != 'all' else None)
        if self.loaded_image  is None:
            QMessageBox.warning(self, "Warning!", "当前图片打不开！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        # Show image
        show_image_in_qt_component(self.loaded_image, self.lbl_sample_image)

        self.update_txb_statistics_forcurimg(self.cur_imgFilePath,
                                             self.cur_gtbox_num, self.cur_detbox_num,
                                             self.cur_gtbox_distribution, self.cur_detbox_distribution)

    # ----------------- [zx add] ------------------------
    def update_txb_statistics_forcurimg(self, curImgFName, gtbox_num, detbox_num, gtbox_distribution, detbox_distribution):

        stats = self.statistics_forcurimg.replace('#Current image#', curImgFName)
        stats = stats.replace('#TOTAL_GTBOXS#', str(gtbox_num) if (self.gt_annotations is not None) else '-')
        stats = stats.replace('#TOTAL_DETBOXS#', str(detbox_num) if (self.det_annotations is not None) else '-')

        labels = set.union(set(gtbox_distribution.keys()), set(detbox_distribution.keys()))

        amount_bb_per_class = ''
        for label in labels:
            amount_bb_per_class += f'- {label} : '
            has_gt = False
            if (self.gt_annotations is not None):
                if label in gtbox_distribution.keys():
                    amount_bb_per_class += f'<b>{gtbox_distribution[label]}</b> gt boxes'
                    has_gt = True
            if (self.det_annotations is not None):
                if label in detbox_distribution.keys():
                    if has_gt: amount_bb_per_class += ', '
                    amount_bb_per_class += f'<b>{detbox_distribution[label]}</b> det boxes'
            amount_bb_per_class += '<br>'
        stats = stats.replace('#AMOUNT_BB_PER_CLASS#', amount_bb_per_class)

        self.txb_statistics_forcurimg.setText(stats)

    def comb_displayClass_changed(self):
        displayClassLabel = self.comb_displayClass.currentText()

        if (self.selected_image_index >= 0):
            self.cur_imgFilePath, self.cur_gtbox_num,  self.cur_detbox_num, \
             self.cur_gtbox_distribution, self.cur_detbox_distribution, self.cur_gt_bboxes, self.cur_det_bboxes = \
                self.load_bbs(self.selected_image_index)

        self.show_image()

    def btn_plot_objdet_confusematrix_clicked(self):
        if (self.gt_annotations is None) or (self.det_annotations is None):
            QMessageBox.warning(self,"Warning!","无法展示objdet confusionMatrix! 因为当前视图只加载了groundtruth数据！",
                                QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            return

        iou_threshold_for_objdet_confusematrix = self.dsb_IOU_threshold_for_objdet_confusematrix.value()
        conf_threshold_for_objdet_confusematrix= self.dsb_conf_threshold_for_objdet_confusematrix.value()
        self.plot_object_detection_confusion_matrix(self.allclass_dict,
                                                    iou_threshold_for_objdet_confusematrix,
                                                    conf_threshold_for_objdet_confusematrix,
                                                    self.gt_version,
                                                    self.det_version,
                                                    None,
                                                    True)

    def plot_object_detection_confusion_matrix(self,
                                 allclass_dict,
                                 eval_confThresh = 0.57,
                                 eval_iouThreshold = 0.5,
                                 gt_version = None,
                                 det_version = None,
                                 savePath=None,
                                 showGraphic=True):
        # iou_threshold = result['iou_threshold']
        cm = ObjDetConfusionMatrix(num_classes=len(allclass_dict), CONF_THRESHOLD=eval_confThresh,
                                   IOU_THRESHOLD=eval_iouThreshold)

        for i, imgfilepath in enumerate(self.image_files):
            img_name = general_utils.get_file_name_only(imgfilepath)

            """
            gt_bboxes, det_bboxes format:
            [ BoundingBox(image_name=img_name,
                             class_id=classes[annotation['category_id']],
                             coordinates=(x1, y1, bb_width, bb_height),
                             type_coordinates=CoordinatesType.ABSOLUTE,
                             img_size=images[img_id]['img_size'],
                             confidence=confidence,
                             bb_type=bb_type,
                             format=BBFormat.XYWH) ]
            """
            gt_bboxes = BoundingBox.get_bounding_boxes_by_image_name(self.gt_annotations, img_name)
            det_bboxes = BoundingBox.get_bounding_boxes_by_image_name(self.det_annotations, img_name)

            # detections (Array[N, 6]), x1, y1, x2, y2, conf, class
            detections = np.empty((len(det_bboxes), 6), np.float32)
            # labels (Array[M, 5]), class, x1, y1, x2, y2
            labels = np.empty((len(gt_bboxes), 5), np.float32)

            for gti, gtb in enumerate(gt_bboxes):
                labels[gti][0] = [k for k, v in allclass_dict.items() if v == gtb.get_class_id()][0]
                labels[gti][1:] = gtb.get_absolute_bounding_box(format=BBFormat.XYX2Y2)

            for dti, dtb in enumerate(det_bboxes):
                detections[dti][0:4] = dtb.get_absolute_bounding_box(format=BBFormat.XYX2Y2)
                detections[dti][4] = dtb.get_confidence()
                detections[dti][5] = [k for k, v in allclass_dict.items() if v == dtb.get_class_id()][0]

            cm.process_batch(detections, labels)

        cmatrix = cm.return_matrix()

        titlestr = f"ObjDet Confusion Matrix @ {dt.now().strftime('%Y-%m-%d %H:%M')}\n"
        # print("eval_confThresh = ", eval_confThresh, "eval_iouThreshold = ", eval_iouThreshold )
        titlestr += f"confThresh: {eval_confThresh:.2f}, iouThresh: {eval_iouThreshold:.2f}\n"
        titlestr += f"Ground Truth dataset: {gt_version}\nDetection dataset: {det_version}\n"
        titlestr += "每个方格有2个数字，上面是个数，下面是该个数在所在行中的比例\n"
        plot_confusion_matrix(cmatrix, list(allclass_dict.values()) + ["noGtOrDet"],
                             title = titlestr,
                              displayProbInInt=False)


import fnmatch
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui
from src.utils.enumerators import BBFormat


def get_classes_from_txt_file(filepath_classes_det):
    classes = {}
    f = open(filepath_classes_det, 'r')
    id_class = 0
    for id_class, line in enumerate(f.readlines()):
        classes[id_class] = line.replace('\n', '')
    f.close()
    return classes


def replace_id_with_classes(bounding_boxes, filepath_classes_det):
    classes = get_classes_from_txt_file(filepath_classes_det)
    for bb in bounding_boxes:
        if not is_str_int(bb.get_class_id()):
            print(
                f'Warning: Class id represented in the {filepath_classes_det} is not a valid integer.'
            )
            return bounding_boxes
        class_id = int(bb.get_class_id())
        if class_id not in range(len(classes)):
            print(
                f'Warning: Class id {class_id} is not in the range of classes specified in the file {filepath_classes_det}.'
            )
            return bounding_boxes
        bb._class_id = classes[class_id]
    return bounding_boxes


def convert_box_xywh2xyxy(box):
    arr = box.copy()
    arr[:, 2] += arr[:, 0]
    arr[:, 3] += arr[:, 1]
    return arr


def convert_box_xyxy2xywh(box):
    arr = box.copy()
    arr[:, 2] -= arr[:, 0]
    arr[:, 3] -= arr[:, 1]
    return arr


# size => (width, height) of the image
# box => (X1, X2, Y1, Y2) of the bounding box
def convert_to_relative_values(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    cx = (box[1] + box[0]) / 2.0
    cy = (box[3] + box[2]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = cx * dw
    y = cy * dh
    w = w * dw
    h = h * dh
    # YOLO's format
    # x,y => (bounding_box_center)/width_of_the_image
    # w => bounding_box_width / width_of_the_image
    # h => bounding_box_height / height_of_the_image
    return (x, y, w, h)


# size => (width, height) of the image
# box => (centerX, centerY, w, h) of the bounding box relative to the image
def convert_to_absolute_values(size, box):
    w_box = size[0] * box[2]
    h_box = size[1] * box[3]

    x1 = (float(box[0]) * float(size[0])) - (w_box / 2)
    y1 = (float(box[1]) * float(size[1])) - (h_box / 2)
    x2 = x1 + w_box
    y2 = y1 + h_box
    return (round(x1), round(y1), round(x2), round(y2))



def add_bb_into_image(image, bb,
                       box_thickness=2,
                       box_color = (255, 0, 0),
                       text_font = cv2.FONT_HERSHEY_SIMPLEX,
                       text_color = (255, 0, 0),
                       text_thickness=1,
                       text_fontscale = 0.3,
                       label=None):

    r = int(box_color[0])
    g = int(box_color[1])
    b = int(box_color[2])

    x1, y1, x2, y2 = bb.get_absolute_bounding_box(BBFormat.XYX2Y2)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    cv2.rectangle(image, (x1, y1), (x2, y2), (b, g, r), box_thickness)
    # Add label
    if label is not None:
        # Get size of the text box
        (tw, th) = cv2.getTextSize(label, text_font, text_fontscale, text_thickness)[0]
        # Top-left coord of the textbox
        (xin_bb, yin_bb) = (x1 + text_thickness, y1 - th + int(12.5 * text_fontscale))
        # Checking position of the text top-left (outside or inside the bb)
        if yin_bb - th <= 0:  # if outside the image
            yin_bb = y1 + th  # put it inside the bb
        r_Xin = x1 - int(text_thickness / 2)
        r_Yin = y1 - th - int(text_thickness / 2)

        """
        # Draw filled rectangle to put the text in it
        cv2.rectangle(image, (r_Xin, r_Yin - thickness),
                      (r_Xin + tw + thickness * 3, r_Yin + th + int(12.5 * text_fontscale)), (b, g, r),
                      -1)
        cv2.putText(image, label, (xin_bb, yin_bb), text_font, text_fontscale, (0, 0, 0), text_thickness,
                    cv2.LINE_AA)
        """
        cv2.putText(image, label, (xin_bb, yin_bb), text_font, text_fontscale, text_color, text_thickness,
                    cv2.LINE_AA)
    return image


def remove_file_extension(filename):
    return os.path.join(os.path.dirname(filename), os.path.splitext(filename)[0])


def get_files_dir(directory, extensions=['*']):
    ret = []
    for extension in extensions:
        if extension == '*':
            ret += [f for f in os.listdir(directory)]
            continue
        elif extension is None:
            # accepts all extensions
            extension = ''
        elif '.' not in extension:
            extension = f'.{extension}'
        ret += [f for f in os.listdir(directory) if f.lower().endswith(extension.lower())]
    return ret


def remove_file_extension(filename):
    return os.path.join(os.path.dirname(filename), os.path.splitext(filename)[0])


def image_to_pixmap(image, scaledToQsize):
    image = image.astype(np.uint8)
    if image.shape[2] == 4:
        qformat = QtGui.QImage.Format_RGBA8888
    else:
        qformat = QtGui.QImage.Format_RGB888

    # --------------------------- [ zx update start ] -------------------------------
    # image = QtGui.QImage(image.data, image.shape[1], image.shape[0], image.strides[0], qformat)
    # image = image.scaled(scaledToQsize, QtCore.Qt.KeepAspectRatio) ## image= image.rgbSwapped()
    # return QtGui.QPixmap(image).scaled(scaledToQsize, QtCore.Qt.KeepAspectRatio)
    # -------------------------------------------------------------------------------
    fw, fh = scaledToQsize.width(), scaledToQsize.height()
    ih, iw = image.shape[0:2]
    if float(fw)/fh <= float(iw)/ih:
        dw = int(fw)
        dh = int(dw / float(iw) * ih)
    else:
        dh = int(fh)
        dw = int(dh / float(ih) * iw)

    xoff = int((fw - dw)/2)
    yoff = int((fh - dh) / 2)
    nimg = np.zeros((fh, fw, image.shape[2]), dtype = np.uint8)

    simg = cv2.resize(image, (dw, dh))
    nimg[yoff:yoff+dh, xoff:xoff+dw, ...] = simg
    fimg = QtGui.QImage(nimg.data, nimg.shape[1], nimg.shape[0], nimg.strides[0], qformat)
    # --------------------------- [ zx update end ] -------------------------------

    return QtGui.QPixmap(fimg)


def show_image_in_qt_component(image, label_component):
    pix = image_to_pixmap(image.astype(np.uint8), label_component.size())
    label_component.setScaledContents(True)
    label_component.setPixmap(pix)
    label_component.setAlignment(QtCore.Qt.AlignCenter)


def get_files_recursively(directory, extension="*"):
    # for f in get_files_dir(directory, [extension]): print("zx ...", f)
    files = [
        os.path.join(dirpath, f) for dirpath, dirnames, files in os.walk(directory)
        for f in get_files_dir(directory, [extension]) if os.path.isfile(os.path.join(dirpath, f))
    ]
    # Disconsider hidden files, such as .DS_Store in the MAC OS
    ret = [f for f in files if not os.path.basename(f).startswith('.')]
    return ret


def is_str_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def get_file_name_only(file_path):
    if file_path is None:
        return ''
    return os.path.splitext(os.path.basename(file_path))[0]


# allowed_extensions is used only when match_extension=False
def find_file(directory, file_name, match_extension=True, allowed_extensions=[]):
    if os.path.isdir(directory) is False:
        return None
    for dirpath, dirnames, files in os.walk(directory):
        for f in files:
            f1 = os.path.basename(f)
            f2 = file_name
            if match_extension:
                match = f1 == f2
            else:
                f1 = os.path.splitext(f1)[0]
                f2 = os.path.splitext(f2)[0]
                f_ext = os.path.splitext(f)[-1].lower()
                match = f1 == f2 and (len(allowed_extensions) == 0 or f_ext in allowed_extensions)
            if match:
                return os.path.join(dirpath, os.path.basename(f))
    return None


def find_image_file(directory, file_name):
    return find_file(directory, file_name, False, [".bmp", ".jpg", ".jpeg", ".png"])


def get_image_resolution(image_file):
    if image_file is None or not os.path.isfile(image_file):
        print(f'Warning: Path {image_file} not found.')
        return None

    # ---------------------------------------------------------------
    # [20220502] zx modified below codes to support chinese-filepath image
    # ---------------------------------------------------------------
    # img = cv2.imread(image_file)
    # ---------------------------------------------------------------
    img = cv2.imdecode(np.fromfile(image_file, dtype=np.uint8), -1)  # use opencv read from image of chinese filepath
    if img is None:
        print(f'Warning: Error loading the image {image_file}.')
        return None
    h, w, _ = img.shape
    return {'height': h, 'width': w}


def draw_bb_into_image(image, boundingBox,
                       box_thickness=2,
                       box_color = (255, 0, 0),
                       text_font = cv2.FONT_HERSHEY_SIMPLEX,
                       text_color = (255, 0, 0),
                       text_thickness=1,
                       text_fontscale = 0.3,
                       label=None):
    if isinstance(image, str):

        # ---------------------------------------------------------------
        # [20220502] zx modified below codes to support chinese-filepath image
        # ---------------------------------------------------------------
        # image = cv2.imread(image)
        # ---------------------------------------------------------------
        image = cv2.imdecode(np.fromfile(image, dtype=np.uint8), -1)  # use opencv read from image of chinese filepath

    r = int(box_color[0])
    g = int(box_color[1])
    b = int(box_color[2])

    xIn = boundingBox[0]
    yIn = boundingBox[1]
    cv2.rectangle(image, (boundingBox[0], boundingBox[1]), (boundingBox[2], boundingBox[3]),
                  (b, g, r), box_thickness)
    # Add label
    if label is not None:
        # Get size of the text box
        (tw, th) = cv2.getTextSize(label, text_font, text_fontscale, text_thickness)[0]
        # Top-left coord of the textbox
        (xin_bb, yin_bb) = (xIn + text_thickness, yIn - th + int(12.5 * text_fontscale))
        # Checking position of the text top-left (outside or inside the bb)
        if yin_bb - th <= 0:  # if outside the image
            yin_bb = yIn + th  # put it inside the bb
        r_Xin = xIn - int(text_thickness / 2)
        r_Yin = yin_bb - th - int(text_thickness / 2)

        """"""
        # Draw filled rectangle to put the text in it
        cv2.rectangle(image, (r_Xin, r_Yin - text_thickness),
                      (r_Xin + tw + text_thickness * 3, r_Yin + th + int(12.5 * text_fontscale)), (b, g, r),
                      -1)
        cv2.putText(image, label, (xin_bb, yin_bb), text_font, text_fontscale, (0, 0, 0), text_thickness,
                    cv2.LINE_AA)
        """"""

        cv2.putText(image, label, (xin_bb, yin_bb), text_font, text_fontscale, text_color, text_thickness,
                cv2.LINE_AA)
    return image


def plot_bb_per_classes(dict_bbs_per_class,
                        horizontally=True,
                        rotation=0,
                        show=False,
                        extra_title=''):
    plt.close()
    if horizontally:
        ypos = np.arange(len(dict_bbs_per_class.keys()))
        plt.barh(ypos, dict_bbs_per_class.values())
        plt.yticks(ypos, dict_bbs_per_class.keys())
        plt.xlabel('amount of bounding boxes')
        plt.ylabel('classes')
    else:
        plt.bar(dict_bbs_per_class.keys(), dict_bbs_per_class.values())
        plt.xlabel('classes')
        plt.ylabel('amount of bounding boxes')
    plt.xticks(rotation=rotation)
    title = f'Distribution of bounding boxes per class {extra_title}'
    plt.title(title)
    if show:
        # plt.tight_layout()
        # plt.show(aspect='auto')
        fig = plt.gcf()
        fig.canvas.set_window_title(title)
        fig.tight_layout()
        fig.show()
    return plt

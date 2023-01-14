# -*- coding: utf-8 -*-

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

def plot_confusion_matrix_2(confusion_matrix, allclass_labels, displayProbInInt = False):
    disp = ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = allclass_labels)
    disp.plot(
        include_values = True,              #  混淆矩阵每个单元格上显示具体数值
        cmap = "viridis",                   #  不清楚啥意思，没研究，使用的sklearn中的默认值
        ax = None,                          #  同上
        xticks_rotation = "horizontal",     #  同上
        # values_format = "d",                 #  显示的数值格式
        colorbar = True
    )
    plt.show()


# confusion_matrix[detection_class, gt_class]
def plot_confusion_matrix(confusion_matrix, allclass_labels, 
													title=None, displayProbInInt = False):

    cmap = plt.cm.binary
    # cm = confusion_matrix(y_true, y_pred)
    cm = confusion_matrix
    tick_marks = np.array(range(len(allclass_labels))) + 0.5
    np.set_printoptions(precision=2)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure(figsize=(10, 12), dpi=120)
    ind_array = np.arange(len(allclass_labels))
    x, y = np.meshgrid(ind_array, ind_array)

    for x_val, y_val in zip(x.flatten(), y.flatten()):
        if (displayProbInInt):
            c = cm[y_val][x_val]
            plt.text(x_val, y_val, "%d" % (c,), color='red', fontsize=8, va='center', ha='center')

        else:
            c = cm[y_val][x_val]
            c_norm = cm_normalized[y_val][x_val]
            if (c_norm > 0.01):
                # You can custom text size and color here
                plt.text(x_val, y_val, "%d\n%0.2f" % (c, c_norm,), color='red', fontsize=7, va='center', ha='center')
            else:
                plt.text(x_val, y_val, "%d" % (0,), color='red', fontsize=7, va='center', ha='center')
    if(displayProbInInt):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
    else:
        plt.imshow(cm_normalized, interpolation='nearest', cmap=cmap)
    plt.gca().set_xticks(tick_marks, minor=True)
    plt.gca().set_yticks(tick_marks, minor=True)
    plt.gca().xaxis.set_ticks_position('none')
    plt.gca().yaxis.set_ticks_position('none')
    plt.grid(True, which='minor', linestyle='-')
    plt.gcf().subplots_adjust(left=0.25)
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.colorbar()
    xlocations = np.array(range(len(allclass_labels)))
    
    allclass_labels_gt = allclass_labels[:-1]
    allclass_labels_gt.append("noMatchDet_gtBoxNum")
    plt.xticks(xlocations, allclass_labels_gt, rotation=90)
    
    allclass_labels_det = allclass_labels[:-1]
    allclass_labels_det.append("noMatchGt_detBoxNum")
    plt.yticks(xlocations, allclass_labels_det)
    
    plt.ylabel('Groundtruth Classes')
    plt.xlabel('Predict Classes')
    if title is None:
        plt.title("Confusion Matrix")
    else:
        plt.title(title)

    plt.savefig('confusion_matrix.jpg', dpi=300)
    plt.show()
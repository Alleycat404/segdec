
import numpy as np
import torch
from sklearn.metrics import confusion_matrix

__all__ = ['SegmentationMetric']

"""
confusionMetric  # 注意：此处横着代表预测值，竖着代表真实值，与之前介绍的相反
P\L     P    N
P      TP    FP
N      FN    TN
"""


class SegmentationMetric(object):
    def __init__(self):
        self.numClass = 2

    def meanIntersectionOverUnion(self, imgPredict, imgLabel):
        # Intersection = TP Union = TP + FP + FN
        # IoU = TP / (TP + FP + FN)
        confusionMatrix = torch.from_numpy(self.genConfusionMatrix(imgPredict, imgLabel))
        intersection = torch.diag(confusionMatrix)  # 取对角元素的值，返回列表
        union = torch.sum(confusionMatrix, dim=0) + torch.sum(confusionMatrix, dim=1) - torch.diag(
            confusionMatrix)  # axis = 1表示混淆矩阵行的值，返回列表； axis = 0表示取混淆矩阵列的值，返回列表
        IoU = intersection / union  # 返回列表，其值为各个类别的IoU
        # mIoU = torch.nanmean(IoU)  # 求各类别IoU的平均
        return IoU[1]

    def genConfusionMatrix(self, imgPredict, imgLabel):
        if len(imgPredict.squeeze().shape) >= 3:
            Matrix = []
            for i in range(imgPredict.squeeze().shape[0]):
                for j in range(imgPredict.squeeze().shape[1]):
                    # print(imgLabel.squeeze()[i][j])
                    # print(imgPredict.squeeze()[i][j])
                    matrix = confusion_matrix(imgLabel.squeeze()[i][j], imgPredict.squeeze()[i][j], labels=[0, 1], sample_weight=None)
                    Matrix.append(matrix)
            Matrix = np.sum(Matrix, axis=0)
            return Matrix
        else:
            Matrix = []
            for i in range(imgPredict.squeeze().shape[0]):
                # print(imgLabel.squeeze()[i])
                # print(imgPredict.squeeze()[i])
                Matrix.append(confusion_matrix(imgLabel.squeeze()[i], imgPredict.squeeze()[i], labels=[0, 1], sample_weight=None))
            Matrix = np.sum(Matrix, axis=0)
        return Matrix


    # def reset(self):
    #     self.confusionMatrix = np.zeros((self.numClass, self.numClass))


if __name__ == '__main__':
    # imgPredict = torch.tensor([[1, 1, 0, 0], [1, 1, 0, 0]])
    # imgLabel = torch.tensor([[1, 0, 0, 0], [1, 1, 0, 0]])
    imgPredict = torch.randint(0, 2, (4, 1, 4, 4))  # 可直接换成预测图片
    imgLabel = imgPredict  # 可直接换成标注图片

    metric = SegmentationMetric()

    mIoU = metric.meanIntersectionOverUnion(imgPredict, imgLabel)
    print('mIoU is : %f' % mIoU)

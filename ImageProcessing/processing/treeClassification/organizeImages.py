from array import array
from email.mime import image
from importlib.resources import path
import os
from pyexpat import features
import shutil #biblioteca do sistema operacional
import cv2 #biblioteca do OpenCV
import numpy as np

class ModelTreeClassification:
    def __init__(self):
        self.__memoria = {}
    
    def fit(self):
        return
        
            

def getMaxValue(hist_teste:array):
    maxValue = 0
    color = 0
    i = 0

    for colorRate in hist_teste:
        if maxValue < colorRate[0]:
            maxValue = colorRate[0]
            color = i
        i+=1
    return color

def createDataSets(base_addr):
    image_folder = os.listdir(base_addr)

    i = 0
    dataSetTest = []
    dataSetTraining = []
    dataSetFeatures = []

    for folder in image_folder:
        dataSetFeatures.append(folder)
        h = 0
        for file in os.listdir(rf'{base_addr}\{folder}'):
            h+=1
            if h >= 10:
                dataSetTest.append(rf'{base_addr}\{folder}\{file}')
            else:
                dataSetTraining.append(rf'{base_addr}\{folder}\{file}')
        i+=1
        if i >= 10:
            break

    return (dataSetTraining, dataSetTest, dataSetFeatures) #retorno de TUPLA é uma lista imutável tanto em ordem e valores

if __name__ == '__main__': #Define se o arquivo de execução for o próprio arquivo ele vai executar o código abaixo
    base_addr = r'ImageProcessing\processing\treeClassification\BarkVN-50_mendeley'
    dataX, dataY, species = createDataSets(base_addr)

    speciesDict = {}    
    for specie in species:
        trees = [x for x in dataX if specie in x]
        colorListX = []
        for tree in trees:
            image = cv2.imread(tree)
            histX = cv2.calcHist([image], [0], None, [255], [0,255])
            color = getMaxValue(histX)
            colorListX.append(color)
        speciesDict[specie] = np.mean(colorListX)

    result = {}

    for imagePath in dataY:
        image = cv2.imread(imagePath)
        histY = cv2.calcHist([image], [0], None, [255], [0,255])
        color = getMaxValue(histY)
        colorDif = {}
        for specie in species:
            colorDif[specie] = abs(speciesDict[specie] - color)
        minValue = 255
        resultSpecie = ""
        for specie in species:
            if colorDif[specie] < minValue:
                minValue = colorDif[specie]
                resultSpecie = specie
        if resultSpecie in result.keys():
            result[resultSpecie].append(imagePath)
        else:
            result[resultSpecie] = [imagePath]
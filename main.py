from os import listdir
from os.path import isfile, join
from os import walk
import csv
from tqdm import tqdm
import time

def buildcsv( theDatasetPath ):
    allPlantDiseasePaths = [];
    for (dirpath, dirnames, filenames) in walk(theDatasetPath):
        allPlantDiseasePaths.extend(dirnames)
        break

    with open('label_train.csv', 'w', newline='') as thecsvfile:
        writer = csv.writer(thecsvfile, quoting=csv.QUOTE_ALL)
        theHeadRow = allPlantDiseasePaths[:]
        # make theHeadRow a new copy of allPlantDiseasePaths
        theHeadRow.insert(0, "filename")
        writer.writerow(theHeadRow)
        # In Python, it is essential to do alignment and indentation making the function or loop a block
        # 在Python语言中，让函数或循环的始末按照规则对齐或缩进形成一个区块是很重要的，否则无法运行

        for index in range(len(allPlantDiseasePaths)):
            allThePlantDiseaseImageNames = [f for f in listdir(theDatasetPath+"/"+allPlantDiseasePaths[index]) if isfile(join(theDatasetPath+"/"+allPlantDiseasePaths[index], f))]
            # print (allThePlantDiseaseImageNames)
            thisRow = [0] * len(allPlantDiseasePaths)
            thisRow[index] = 1
            for theImageName in allThePlantDiseaseImageNames:
                insertThisRow = thisRow[:]
                insertThisRow.insert(0,theImageName);
                writer.writerow(insertThisRow)

    return;

if __name__ == "__main__":
    buildcsv(theDatasetPath="raw/color")

# onlyfiles = [f for f in listdir("raw/color/Apple___healthy") if isfile(join("raw/color/Apple___healthy", f))]
#
# print (onlyfiles)
#
# f = []
# for (dirpath, dirnames, filenames) in walk("raw/color"):
#     f.extend(dirnames)
#     break
#
# print (f)

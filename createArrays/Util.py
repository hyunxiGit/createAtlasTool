# coding=utf-8
import os
import imghdr
from PIL import Image

# return parent directory of the script
def getImgFolder():
    imageFolder = formatPathString(os.path.dirname(__file__)).rsplit("/", 1)[0]
    return imageFolder

def formatPathString (sourceStr):
    targetStr = sourceStr.replace('\\','/')
    return targetStr

def getImgFileList(sourcePath , useSubFolder = False):
    targetlist = []
    # todo : add alert info for non image files / exeption

    # do not use sub folder
    if not useSubFolder:
        for path in os.listdir(sourcePath):
            fullPath =  sourcePath + "/" + path
            if os.path.isfile(fullPath) and imghdr.what(fullPath) != None:
                targetlist .append(fullPath)
    # use sub folder
    else :
        list_dirs = os.walk(sourcePath)
        for root, dirs, files in list_dirs:
            for f in files:
                myFile = formatPathString(os.path.join(root, f))
                if imghdr.what(myFile) != None:
                    targetlist.append(formatPathString(os.path.join(root, f)))
                    print (imghdr.what(myFile))

    return targetlist

class ImgArray:
    def __init__(self, imgSize):
        # image size in tuple (width, height)
        self.imgSize = imgSize
        # image file list with the same size
        self.imgList = []
        self.mode = "RGB"

    def addImg(self, img):
        self.imgList.append(img)

# return list of
def getImgSizedList (sourceList):
    # todo check if a given list is Image
    # share the same index
    sizeList = []
    imgList = []
    for imgFile in sourceList:
        img = Image.open(imgFile, 'r')
        if img.size not in sizeList:
            newImgArray = ImgArray(img.size)
            newImgArray.addImg(imgFile)
            sizeList.append(img.size)
            imgList.append(newImgArray)
            currentImgArray = newImgArray
        else:
            myIndex = sizeList.index(img.size)
            currentImgArray = imgList[myIndex]
            currentImgArray.addImg(imgFile)

        if img.mode == "RGBA" and img.mode !=currentImgArray.mode :
            currentImgArray.mode = "RGBA"

    return (imgList)

def createTextureAtlas (sourceImgArray):
    #todo : check if the sourceImgArray is a Im a ImgArray

    myImgList = sourceImgArray.imgList[:]
    myImgCount = len(myImgList)
    sourceSize = (sourceImgArray.imgSize[0], sourceImgArray.imgSize[1])

    myTargetImgMode = sourceImgArray.mode
    myTargetImgSize = (sourceSize[0], sourceSize[1]*myImgCount)
    myTargetImgColor = (0,0,0,1) if myTargetImgMode == "RGBA" else (0,0,0)
    myTargetImg = Image.new(myTargetImgMode, myTargetImgSize, myTargetImgColor)

    for i in range(myImgCount):
        curImg = Image.open(myImgList[i])
        targetBox = (0,i*sourceSize[1],sourceSize[0],(i+1)*sourceSize[1])
        myTargetImg.paste (curImg,targetBox)

    return (myTargetImg)


def getUserYesNoInput (tipsToShow):

    yesCases = ['y', 'yes', 'ye', 'Y', 'YE', 'YES']
    noCases = ['n', 'no', 'N', 'NO']
    toRun = 'ng'

    tips = tipsToShow if isinstance(tipsToShow, basestring) else 'Please choose '

    while toRun == 'ng':
        useInput = raw_input(tips+' (y/n) : ')
        if useInput in yesCases:
            return True
        elif useInput in noCases:
            return False
        else:
            toRun = 'ng'

def validateImgFolder(spMode = False):
    # get the default image folder or get the user defined folder
    if not spMode:
        sourcePath = getImgFolder()
    else:
        sourcePath = raw_input("Please enter the image folder path:\n")
    myImagFileList = [] if not os.path.isdir(sourcePath) else getImgFileList(sourcePath)
    while len(myImagFileList)==0:
        sourcePath = raw_input("The given folder does not contain any images or the folder\n you specified is invalid, please specify a valid image folder:\n")
        if os.path.isdir(sourcePath):
            myImagFileList = getImgFileList(sourcePath)
    return sourcePath





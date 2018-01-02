import argparse
import textwrap
import Util
import os
import string

# the menu part
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
    ---------------------------------------------
    To run, type:
           CreateArrays.py  '''),
    epilog=textwrap.dedent('''
    ---------------------------------------------
    Please type [CreateArray.py] to run it:'''),
    prefix_chars='-')

parser.add_argument('-s',action = 'store_true',  help='run in silent mode')
parser.add_argument('-sp',action = 'store_true',  help='specify the source img folder. By default this will be the parent folder of where the tool folder located.')
parser.add_argument('-o',  help='specify the output name. By default this will be [OutputName_size.extension]')
# parser.add_argument('-tp',action = 'store_true',  help='specify the output folder. Bn default the tool will create a out folder in the same folder as source images folder.')


args = parser.parse_args()

# validate output name
if args.o != None:
    outputName = args.o
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    for c in args.o :
        if c not in valid_chars:
            print "The output name yousepcified is not valid, default name will be used!"
            outputName = "OutputName"
            break
else :
    outputName = "OutputName"

#validate source folder

targetImgFolder = Util.validateImgFolder(args.sp)
imagFileList = Util.getImgFileList(targetImgFolder)
print targetImgFolder

# output folder
# todo : customize folder
outPutFolder = targetImgFolder+"/out/"
if not os.path.exists(outPutFolder):
    os.makedirs(outPutFolder)


# informations for user to confirm
def runSilent (silentMode = False):
    imgSizedList = Util.getImgSizedList(imagFileList)
    # toRun = 'true'
    toRun = True
    if (silentMode == False):
        print textwrap.dedent('''
            ---------------------------------------------
            Target folder is : ''')
        print targetImgFolder
        print textwrap.dedent('''\n
            The output folder will be : ''')
        print outPutFolder
        print textwrap.dedent('''
            The output Name will start with : ''')
        print outputName
        print textwrap.dedent('''
            ---------------------------------------------''')
        toRun = Util.getUserYesNoInput('Do you want to do the atlar creation now ')

    # run the tool
    if toRun == True:
        createTexture(imgSizedList)


def createTexture (sourseList):
    print textwrap.dedent('''
            ---------------------------------------------
            The following images have been created : ''')
    for myImgArray in sourseList:
        outputFileName = outPutFolder + outputName + "_" + str(myImgArray.imgSize[0]) + "x" + str(
            myImgArray.imgSize[1]) + ".png"
        Util.createTextureAtlas(myImgArray).save(outputFileName)
        print outputFileName

if len (imagFileList) >0:
    runSilent(args.s)
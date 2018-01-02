This python tool collect same size images into image atlas.
 
Prepare: 
	The tool will need python 2.x version and PIL package installed.
	The tool will need python path add to environment variable.
	Copy the folder [createArrays] and file [runCreateArrays.bat] into the image folder

To run the tool:
	1.double click    runCreateArrays.bat 
	2.enter python CreateArrays.py in the command line tool


About the tool:
	By default, create Texture atlars for same size images that are located in the same folder
	with [createArrays] and [runCreateArrays.bat]. 

	But you can also target another image folder by using   
	python CreateArrays.py -sp
	In this case, the tool will allow you input the absolute path for the target image folder.
	To be notice, if the default image folder does not contain any image files, you have to specify
	a valid folder to conitue.
	
	By default the output name will be OutputName_size.extension. You can change the name by using
	python CreateArrays.py -o imageName

	The output files will be located in a [out] folder that is created in the target image folder.

Thank you!
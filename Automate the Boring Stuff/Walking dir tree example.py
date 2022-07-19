import os

for folderName, subfolders, filenames  in os.walk('d:\\albert\\python\\delicious'):
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

	for subfolder in subfolders:
            if 'fish' in subfolder:
               # os.rmdir(subfolder)
                print ('rmdir on ' + subfolder)

        for file in filenames:
            if file.endswith('.py'):
                shutil.copy(os.join(folderName, file), (folderName, file + '.backup'))

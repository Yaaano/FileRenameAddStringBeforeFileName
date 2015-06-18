import os
import Tkinter
import tkFileDialog
import tkMessageBox

#select path
root = Tkinter.Tk()
root.withdraw()
path = tkFileDialog.askdirectory()

#get each filename
fileList = os.listdir(path)
if len(fileList) == 0:
    print "There are no files"
    sys.exit()

#write a string you want to add before the file name
print "Write a string you want to add before the file name"
addString = raw_input()

#add the string before the file name
for file in fileList:
    os.rename(os.path.join(path, file), os.path.join(path, addString + file))

print "Finish"

#------------------------------------------------------------------------------
# Name:        Path Restore (Computer Transfer)
# Description: Educational
#
# Author:      Robert S. Spencer
#
# Created:     5/7/2016
# Python:      3.5
#------------------------------------------------------------------------------

import os, shutil

function = input("Save (S) or Restore (R) ? ")

cwd = os.getcwd()

def save():
    print ("Save Function....")
    complete = False
    filedict = {}
    currentfolderdict = {'CWD':os.getcwd()}
    while complete is False:      
        newfolderdict = {}      
        for folder in currentfolderdict:
            os.chdir(currentfolderdict[folder])
            print ('\n......',folder,'......')            
            print (currentfolderdict[folder])              
            for item in os.listdir(currentfolderdict[folder]):
                if os.path.isdir(item) == True:
                    print ('   //',item,'//')
                    newfolderdict[item] = os.path.abspath(item)
                else:
                    print ('  ',item)
                    filedict[item] = currentfolderdict[folder][18:]  # Snip Path Root!
        if len(newfolderdict) == 0:
            complete = True
        else:
            currentfolderdict = newfolderdict
    os.chdir(cwd)
    return filedict


def restore():    
    print ("Restore Function....")
    for item in os.listdir(cwd):
        print (item, filedict[item])        
        if not os.path.exists(cwd+'/Restore'+filedict[item]):
            os.makedirs(cwd+'/Restore'+filedict[item])
        shutil.copy2(os.path.abspath(item), cwd+'/Restore'+filedict[item])

if function == 'S':
    filedict = save()    
    f = open('Path_Dictionary.txt','a')
    f.write(str(filedict)+'\n')   
    f.close()             

    
if function == 'R':
    restore()
    
    





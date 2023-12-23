# Import necessary packages.
import os
from openpyxl import Workbook
wb = Workbook()

ws = wb.active

# Start/stop condition.
convert = 'y'

while convert == "y":
    try:
        # Enter filepath and list files in said directory.
        filepath = input("Please enter your file path:")
        entries = os.listdir(filepath)
        print('\n')
        
        # Print file names.
        print("The following files were added to the CD Nexus.")
        for index, entry in enumerate(entries):
            print(os.path.splitext(entry)[0])
            doc_name = ws.cell(row = index + 1 , column = 2 , value = os.path.splitext(entry)[0])
        print('\n')
        
        #Update `convert` to continue or stop loop
        convert = input('Do you have any other files names you wish to extract? (Y/N):')
        
        #Save the CD Nexus in desired destination
        wb.save('C:\\Users\\santi\\source\\repos\\FileName\\test.xlsx')
    #Output if a filepath is not entered
    except WindowsError:
        print('Bruh, that\'s not a filepath, try again.')





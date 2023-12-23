# Import necessary packages.
import os
from openpyxl import Workbook
wb = Workbook()

ws = wb.active

# Start/stop condition.
convert = 'y'

# `Python` starts at need to add 1 to start at appropriate cell on Excel.
row_index = 1

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
            doc_name = ws.cell(row = index + row_index , column = 2 , value = os.path.splitext(entry)[0])
            row = index + row_index
        print('\n')
        
        #When iterating index is reset to 0, need the 1 to start at the appropriate cell.
        row_index = row + 1
        #Update `convert` to continue or stop loop
        convert = input('Do you have any other files names you wish to extract? (Y/N):')
        
        #Save the CD Nexus in desired destination
        wb.save('your filepath')
    #Output if a filepath is not entered
    except WindowsError:
        print('Bruh, that\'s not a filepath, try again.')





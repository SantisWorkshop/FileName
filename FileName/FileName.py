import os

convert = 'y'

while convert == "y":
    try:
        filepath = input("Please enter your file path:")
        entries = os.listdir(filepath)
        print('\n')
        
        for entry in entries:
            print(entry)
        print('\n')
        check_periods = input("Except for the file type, are there any files with a \".\" in its name? (Y/N):")
        print('\n')

        check_periods: check_periods.strip().lower()
        sep = '.'

        if check_periods == 'n':
            for entry in entries:
                print(entry.partition(sep)[0])
    
        convert = input('Do you have any other files names you wish to extract? (Y/N):')

    except WindowsError:
        print('Bruh, that\'s not a filepath, try again.')





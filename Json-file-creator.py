# Rhett Coleman / CIS245-T302 / 11/5/2020

import os
import time
import json

# file setup
def file_setup():
    global filePath
    global fileName
    setup_task = True
    while setup_task == True:
        #Directory Setup
        userdirinput = input("\nWhere would you like the file to be located?"
                             "\nNote: The file path starts in the user's home directory"
                             "\nEx. Desktop/PythonProjects"
                             "\nUser/Username/")

        inputdirfixed = f'~/{userdirinput}/'  # "~/Desktop/"
        filePath = os.path.expanduser(inputdirfixed)


        if os.path.isdir(filePath):
            print("\nDirectory Found! Now let's make the file.")
            #File Setup
            inputfilefixed = input('Please name the file: ')
            fileName = f'{inputfilefixed}.json'
            setup_task = False
            return setup_task

        else:
            print("\nWe're sorry, the file path you have entered does not exist."
                  "\nPlease ensure spelling and capitalization are correct."
                  "\nAlso ensure / and \ are used appropriately.")
            time.sleep(2)

def Questionare():
    print("\nNow we would like to ask you a few questions.")
    name = input('What is your name?: ')
    address = input('What is your address?: ')
    phone_number = input('What is your phone number?: ')

    user_information = f'{name},{address},{phone_number}'
    return user_information


#Main Function
if __name__ == '__main__':
    print('#### Welcome to the File Creator ####')
    file_setup()
    user_information = Questionare()

    #Writing file
    with open(os.path.join(filePath, fileName), 'w+') as personal_info_file:
        json.dump(user_information, personal_info_file)
        print('--- File created successfully! ---')

    #Reading File
    print('\nHere are the contents of your file:')
    completePath = filePath + fileName
    with open(completePath) as personal_info_file:
        data = json.load(personal_info_file)
    print(data)

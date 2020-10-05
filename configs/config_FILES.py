'''
For a flawless upload of many files to all the desired items the following
variables have to be set:

upload_list   which is a list of 2-element lists
e2            the 2-element list containing 1. the item id and 2. the folder
              from which all files will be upload to the item on TUdatalib

Replace <directory_path> with the WHOLE path to the folder you want to
upload files from.
Note that you have to give path to a folder, not a file and that EVERYTHING
from that folder will be upload to the item!!!!
'''

upload_list = None #python list of list of strings

'''
Please stick to this format (number of elements variable):

upload_list = [
               ["<item_id>","<directory_path>"],
               ["<item_id>","<directory_path>"]
              ]
'''

#Only works for public collections atm
#For private ones you must find the id by klicking on "Edit collection" and
#then read it of from the "assign roles" tab

import sf.API as api
import sf.utils as utils

if __name__ == "__main__":
    print("Only works for public collections.")
    print("Please enter the name or a part of the name of the collection:")
    user_input = input()
    collection_dict = api.get_collections(None)
    key,cID = utils.find_entry(user_input, collection_dict)
    if key == None or cID == None:
        print("No collection found.")
        print("It a) may not exist")
        print("...b) might be private")
        print("Or you typed it incorrectly")
    else:
        print("Full name: {}, ID: {}".format(key, cID))
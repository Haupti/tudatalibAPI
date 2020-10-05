import configs.config_FILES as cFILES
import sf.utils as utils
import sf.API as api

import os

upload_list = cFILES.upload_list

if __name__ == "__main__":
    if upload_list == None:
        print("Please fill in 'config_FILES' in the 'configs' folder")
        exit()
    else:
        email, password = api.ask_login_data()
        cookie = api.login(email, password)

        #loops threw all item-folder pairs in the config list
        for element in upload_list:
            #extracts the file names in the folder (given path)
            file_names = os.listdir(element[1])
            #loops threw all all files in that folder and uploads the to
            #the item id specified
            for file_name in file_names:
                file_path = str(element[1])+'/'+str(file_name)
                response = api.upload(element[0], file_path, cookie)
                #informs you that upload failed if website Returns
                #an status other than "ok"
                if response.status_code != 200:
                    print("ERROR: Upload of {} failed. Upload skipped.".format(file_name))

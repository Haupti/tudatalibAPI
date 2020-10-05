import sf.API as api
import sf.utils as utils
import configs.config_META as cMETA

item_list = cMETA.item_id_list
metadata_list = cMETA.metadata_list

if __name__ == "__main__":
    if item_list == None or metadata_list == None:
        print("Please fill in 'the config_META' in the 'configs' folder.")
    else:
        email, password = api.ask_login_data()
        cookie = api.login(email, password)
        for index,item_id in enumerate(item_list):
            r = api.upload_metadata(item_id, metadata_list[index],cookie)
            if r.status_code == 400:
                Print("ERROR: probably wrong metadata format. Upload skipped.")
            if r.status_code == 500:
                raise Exception("ERROR: probably non existing item. Upload skipped.")

import configs.config_IC as cIF
import sf.utils as utils
import sf.API as api

collection_id = cIF.collection_id
metadata = cIF.metadata

if __name__ == "__main__":
    if collection_id == None:
        print('Please specify the collection ID in the "config_IC.py" file')
        print('in the "configs" folder and retry.')
        print('If you dont know how to get it run "get_collection_id.py"')
        print('in the "helpers" folder or read the information.')
        print('in the config file.')
    else:
        email, password = api.ask_login_data()
        cookie = api.login(email, password)
        if api.collection_exists(collection_id,cookie) and metadata != None:
            print("creating item...")
            r = api.create_item(collection_id, metadata, cookie)
            if r.status_code == 200:
                print("item created")
            api.logout(cookie)
            exit()

        elif api.collection_exists(collection_id,cookie) and metadata == None:
            print("There is no metadata and thus no name for the item specified")
            print("in the config file. Please enter a name for the item now:")
            user_input1 = input()
            print("Are you shure to use '{}' as name for the item? (y/n)".format(user_input1))
            user_input2 = input()
            if user_input2 == "y":
                metadata = [{"key":"dc.title",
                             "value":user_input1,
                             "language":None}]
                print("creating item...")
                r = api.create_item(collection_id,metadata,cookie)
                if r.status_code == 200:
                    print("item created")
                api.logout(cookie)
                exit()
            else:
                print("Input was '{}' which is either 'n' or invalid.".format(user_input2))
                print("exiting...")
                api.logout(cookie)
                exit()

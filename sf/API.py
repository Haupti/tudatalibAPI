#custompackages
from . import config
from . import cache
from . import utils

#packages
import requests
import getpass

#importing from package config
rest_url = config.rest_url
#import files.config.rest_test_url as rest_test_url

#Login with given email adress and passwort, returns session cookie
def login(email, password):
    logindata = {"email":email,"password":password}
    cookie = requests.post(rest_url+'/login', data = logindata).cookies
    return cookie

#logs out using the cookie you got from login
def logout(cookie):
    requests.get(rest_url+'/logout', cookies = cookie)

def availability():
    r = requests.get(rest_url+'/test')
    if r.text.lower() != 'rest api is running.':
        raise Exception('REST API not running. The response code was: {}.'.format(r.status_code))
        raise Exception('Please contact an administrator') #Which is not Marwin Acker
        exit()
    return r

#aks for login data.
#This saves the email to the config and later asks you if you want to use this
#or give a new one
def ask_login_data():
    email = cache.email
    if email == None:
        email = input("Enter EMail adress: ")
    else:
        use_cache = input("Do you want to use '{}' as Email adress? (y/n) ".format(cache.email))
        if use_cache == "y":
            email = cache.email
        elif use_cache == "n":
            email = input("Enter EMail adress: ")
        else:
            print("invalid input")
            ask_login_data()
    password = getpass.getpass("Enter password: ")
    utils.write_to_cache(email,"email")
    return email, password

#This uploads a file, given its path, to an bitstream, given its ID
#this also needs the session cookie
def upload_to_bitstream(file_path, bitstream_id, cookie):
    r = requests.put(rest_url+'/bitstreams/'+bitstream_id+'/data',
                     cookies = cookie, data = open(file_path, 'rb'))
    return r

#creates bitstream to item, given its ID. Returns the bitstream id
def create_bitstream(item_id, filename, cookie):
    r = requests.post(rest_url+'/items/'+item_id+'/bitstreams?name='+filename,
                      cookies = cookie)
    _,_,leftover = r.text.partition('<bitstream><link>/rest/bitstreams/')
    bitstream_id,_,_ = leftover.partition('</link>')
    return bitstream_id

#uploads file to item
def upload(item_id, file_path, cookie):
    file_name = file_path.split("/")[-1] #filename is last in path to file
    bitstream_id = create_bitstream(item_id,file_name, cookie)
    response = upload_to_bitstream(file_path, bitstream_id, cookie)
    return response
    #create_bitstream(item_id, file)

#creates item given collection id and metadata of item and cookie
def create_item(collection_id, metadata, cookie):
    item = {"metadata":metadata}
    r = requests.post(rest_url+'/collections/'+collection_id+'/items',
                      cookies = cookie, json = item)
    return r

#makes a request to TUdatalibs rest api to get all public collections
def get_collections(cookie):
    r = requests.get("{}/collections".format(rest_url),cookies = cookie)
    collections_dict = utils.get_collections_dict(r)
    return collections_dict

#checks if a collection exists given its ID, returns True if so
def collection_exists(collection_id, cookie):
    r = requests.get('{}/collections/{}'.format(rest_url,collection_id),
                     cookies = cookie)
    if str(r.content) == 'b' '' or 'b''' == str(r.content):
        return False
    else: return True

#uploads given metadata to given item (id), returns response object
def upload_metadata(item_id, metadata, cookie):
    r = requests.post('{}/items/{}/metadata'.format(rest_url,item_id),
                        cookies = cookie, json = metadata)
    return r

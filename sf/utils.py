from . import API as api
#replaces keyword variable with what u give it
def write_to_cache(value, keyword):
    rf = open('./sf/cache.py','r')
    lines = []
    for line in rf:
        key,_,_ = line.partition(" = ")
        if keyword in key:
            lines.append(keyword+" = "+str('"{}"'.format(value)))
        else:
            lines.append(line)
    rf.close()
    wf = open('./sf/cache.py','w')
    wf.write('\n'.join(lines))
    wf.close()

#gets a response object and extracts the collections with id as a dictionary
def get_collections_dict(response_object):
    str_content = str(response_object.content)
    lst = str_content.split('},{')

    bitstream_dict = {}

    collection_list = []
    for element in lst:
        collection_list.append(element.split(','))

    names = []
    ids = []
    for collection in collection_list:
        for element in collection:
            if "uuid" in element:
                ids.append(element.split('":"')[1][:-1])
            elif "name" in element:
                names.append(element.split('":"')[1][:-1])

    for i in range(len(names)):
        bitstream_dict[names[i]] = ids[i]
    return bitstream_dict

#returns full name and id if found
def find_entry(search_name, collection_dict):
    for key in collection_dict:
        if search_name in key:
            return key, collection_dict[key]
    return None

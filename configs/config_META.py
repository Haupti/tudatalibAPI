'''
Set the metadata according to the descritpion below, as well as the
collection id.
'''

item_id_list = None #python list of strings
metadata_list = None #python list of list of dictionarys

'''
Item id can be obtained from the "Edit Item" page in the web
interface.
For each Item you specify you have to specify a list of metadata entrys
for this item.
Each list of metadata entrys must be in the list "metadata_list"
Each metadata entry must be a dictionary.
See examples below.
(keywords in example folder -> "metadata_keywords.txt")

Example entry for the metadata list:

                    {"key":"dc.contributor.author",
                     "value":"Mustermann, Max",
                     "language":None
                    }

Example metadata list:

example_metadata = [{"key":"dc.contributor.author",
                     "value":"Mustermann, Max",
                     "language":None
                    },
                    {"key":"dc.date.issued",
                     "value":"2019",
                     "language":None
                    }
                   ]
'''

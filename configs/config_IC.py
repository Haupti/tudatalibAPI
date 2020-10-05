'''
If you know the collection id please write it here as python string.
Also set the metadata according to the descritpion below, as well as the
collection id.
'''
collection_id = None #pyhton string
metadata = None #python list of dictionarys

'''
Collection id can be obtained from the "Sammlung bearbeten" page in the web
interface. If this is left as "None" you will be asked for the collection
name later.

The metadata for item creation should at least contain the dc.title keyword
as shown in the example below. Of course you can add extra metadata entrys
to the list (python list) with different keywords.
(keywords in example folder -> "metadata_keywords.txt")

Example entry for the metadata list:
{"key":"dc.title",
"value":"Example Item Name",
"language":None
}

Example metadata list:
example_metadata = [{"key":"dc.title",
                     "value":"Example Item Name",
                     "language":None
                     }
                    {"key":"dc.date.issued",
                     "value":"2019",
                     "language":None
                    }
                   ]
'''

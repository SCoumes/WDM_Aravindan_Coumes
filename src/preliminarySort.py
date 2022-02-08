import random

import utilitary

def getfields(n, datapath, temppath) :
    """ Samples n s2 files located in datapath and returns all the names of fields of articles found in these files. Use temppath as a temp folder for file hadling."""
    temp_file = temppath + "/temp.json"
    fieldnames = set()
    all_files = utilitary.listfiles(datapath)
    to_read = random.sample(all_files, n)

    for f in to_read :
        utilitary.decompress(f, temp_file)
        for article in utilitary.read_json_list(temp_file) :
            for field in article["fieldsOfStudy"] :
                fieldnames.add(field)

    return list(fieldnames)

def test_field(article, fieldname) : 
    return fieldname in article["fieldsOfStudy"]

# First writeup 
def filter_data(fieldname, datapath, new_datapath, temp_path, filesize = 100) :
    """Get all articles contained in datapath to new files in new_datapath"""
    temp_file = temp_path + "/temp.json"
    to_read = utilitary.listfiles(datapath)
    to_write = []
    written = 0

    for f in to_read : 
        utilitary.decompress(f, temp_file)
        for article in utilitary.read_json_list(temp_file) :
            if test_field(article, fieldname) :
                to_write.append(article)
        if len(to_write) > filesize :
            utilitary.write_json(to_write, new_datapath + "/data_" + str(written) + ".json")
            written += 1
            to_write = []
    utilitary.write_json(to_write, new_datapath + "/data_" + str(written) + ".json")

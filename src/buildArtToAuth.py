import utilitary
import json

def buildTable(datapath) : 
    all_files = utilitary.listfiles(datapath)
    table = dict()

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            authors = []
            for author in article["authors"] :
                try :
                    authID = int(author["ids"][0])
                    authors.append(authID)
                except Exception :
                    pass
            ID = int(article["id"], 16)
            table.update({ID : authors})

    return table

def putTableOnDisk(datapath, targetpath) :
    table = buildTable(datapath)
    fileDict = dict()
    sizecount = 0
    filecount = 0

    for (ID, authList) in table.items() :
        fileDict.update({ID : authList})
        sizecount += 1
        if sizecount >= 1000 :
            with open(institupath + "/artToAuth_" + str(filecount) + ".json", "w") as f :
                json.dump(fileDict, f)
            fileDict = dict()
            sizecount = 0
            filecount += 1

def getTableFromDisk(targetpath) :
    all_files = utilitary.listfiles(targetpath)
    table = dict()

    for f_name in all_files :
        with open(f_name, "r") as f :
            table.update(json.load(f))

    return table

def incrTable(id1, id2, table) :
    if id1 not in table.keys() :
        table.update({id1 : {id2 : 1}})
    elif id2 not in table[id1].keys() :
        table[id1].update({id2 : 1})
    else :
        table[id1][id2] += 1

def updateCount(citingAuthors, citedAuthors, table) :
    for author in citingAuthors :
        try :
            citingID = int(author["ids"][0])
        except Exception :
            continue
        for citedID in citedAuthors :
            incrTable(citingID,citedID, table)

def buildCitationTable(datapath, artToAuth) : 
    all_files = utilitary.listfiles(datapath)
    table = dict()

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            for ID in article["outCitations"] :
                artID = int(ID, 16)
                citingAuthors = article["authors"]
                citedAuthors = artToAuth[artID]
                updateCount(citingAuthors, citedAuthors, table)

    return table

def putTableOnDisk(datapath, targetpath, artToAuth) :
    """Contrary to other disk IO functions. The targetpath here is a file, not a dir"""
    filedict = buildCitationTable(datapath, artToAuth)
    with open(targetpath, "w") as f :
        json.dump(fileDict, f)

def getTableFromDisk(targetpath) :
    with open(targetpath, "r") as f :
        return json.load(f)

 

import utilitary
import json

def incrTable(id1, id2, table) :
    if id1 not in table.keys() :
        table.update({id1 : {id2 : 1, "total" : 1}})
    elif id2 not in table[id1].keys() :
        table[id1].update({id2 : 1})
        table[id1]["total"] += 1
    else :
        table[id1][id2] += 1
        table[id1]["total"] += 1

def updateCount(citingAuthors, citedAuthors, table) :
    for author in citingAuthors :
        try :
            citingID = author["ids"][0]
        except Exception :
            continue
        for citedID in citedAuthors :
            incrTable(citingID,citedID, table)

def getTimePeriod(timePeriods, year_str) :
    year = int(year_str)
    for index, val in enumerate(timePeriods) :
        if val > year : return index
    return len(timePeriods)

def buildCitationTables(datapath, artToAuth, timePeriods) : 
    all_files = utilitary.listfiles(datapath)
    tables = [dict() for _ in timePeriods] + [dict()]

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            table = tables[getTimePeriod(timePeriods, article["year"])]
            for artID in article["outCitations"] :
                try :
                    citedAuthors = artToAuth[artID]
                except Exception :
                    continue
                citingAuthors = article["authors"]
                updateCount(citingAuthors, citedAuthors, table)

    return tables

def putTableOnDisk(datapath, targetpath, artToAuth, timePeriods) :
    """Contrary to other disk IO functions. The targetpath here is a file, not a dir"""
    fileList = buildCitationTables(datapath, artToAuth, timePeriods)
    with open(targetpath, "w") as f :
        json.dump(fileList, f)

def getTableFromDisk(targetpath) :
    with open(targetpath, "r") as f :
        return list(json.load(f))

 

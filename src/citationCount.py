import utilitary
import json

def incrTable(id1, id2, table) :
    if id2 not in table.keys() :
        table.update({id2 : {id1 : 1, "total" : 1}})
    elif id1 not in table[id2].keys() :
        table[id2].update({id1 : 1})
        table[id2]["total"] += 1
    else :
        table[id2][id1] += 1
        table[id2]["total"] += 1

def updateCount(citingAuthors, citedAuthors, table) :
    for author in citingAuthors :
        try :
            citingID = author["ids"][0]
        except Exception :
            continue
        for citedID in citedAuthors :
            incrTable(citingID,citedID, table)

def getTimePeriod(timePeriods, year) :
    for index, val in enumerate(timePeriods) :
        if val > year : return index
    return len(timePeriods)

def buildCitationTables(datapath, artToAuth, timePeriods) : 
    """ This returns a list of two dimensional tables. For T a table we have T[A][B] the number of citations that A received from B and T[A][total] the total number of citations received by A."""
    all_files = utilitary.listfiles(datapath)
    tables = [dict() for _ in timePeriods] + [dict()]

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            try :
                year = int(article["year"])
            except Exception :
                continue
            table = tables[getTimePeriod(timePeriods, year)]
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

 

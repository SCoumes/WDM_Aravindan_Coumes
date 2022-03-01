import utilitary
import json

def addArticleInstitutions(tableAffiliations, authorID, authorName, articleTitle) :
            try : 
                queryFunction = lambda name, paper : ["The cheese alliance"] #TODO move to Priyanka function here
                institutions = queryFunction(authorName, articleTitle)
                tableAffiliations.update({authorID : institutions})
            except Exception :
                pass

def addAuthorToTable(author, table, article) :
    try :
        ID = author["ids"][0]
        if ID in table.keys() :
            pass
        else :
            table.update({ID : (author["name"], article["title"])})
    except Exception :
        pass

def getInstitutions(datapath) : 
    all_files = utilitary.listfiles(datapath)
    tableAffiliations = dict() #Meant to contain pairs (author_id, list_of_instituions)
    authorsTable = dict()

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            for author in article["authors"] :
                addAuthorToTable(author, authorsTable, article)
    
    for authorID in authorsTable.keys() :
        authorName, articleTitle = authorsTable[authorID]
        addArticleInstitutions(tableAffiliations, authorID, authorName, articleTitle)

    return tableAffiliations

def putInstitutionsOnDisk(datapath, institupath) :
    """The main function to use to treat the data and list all institutions. Saves on disk."""
    table = getInstitutions(datapath)
    fileDict = dict()
    sizecount = 0
    filecount = 0

    for authorName in table.keys() :
        fileDict.update({authorName : table[authorName]})
        sizecount += 1
        if sizecount >= 1000 :
            with open(institupath + "/authorInstitutions_" + str(filecount) + ".json", "w") as f :
                json.dump(fileDict, f)
            fileDict = dict()
            sizecount = 0
            filecount += 1

def getInstitutionsFromDisk(institupath) :
    """The main function to get the list of institutions affiliations as a dict form what is written on disk"""
    all_files = utilitary.listfiles(institupath)
    table = dict()

    for f_name in all_files :
        with open(f_name, "r") as f :
            table.update(json.load(f))

    return table

def oneQuery(name, articleName) :
    """ Fake function, for the time being"""
    return ["The very serious institution for cheese"]

#
#
# print(getInstitutions("../test/filtered_test_data", oneQuery))
putInstitutionsOnDisk("../test/filtered_test_data", "../test/institutions")
print("Ok on disk")
print(getInstitutionsFromDisk("../test/institutions"))

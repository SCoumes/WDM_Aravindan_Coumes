import utilitary
import json

def addArticleInstitutions(table, article) :
    for author in article["authors"] :
        authorName = author["name"]
        institutions = oneQuery(authorName, article["title"])
        if authorName in table.keys() : 
            institutions = institutions + table[authorName]
            table.update({authorName : institutions})
        else : 
            table.update({authorName : institutions})

def getInstitutions(datapath, queryFunction) : 
    all_files = utilitary.listfiles(datapath)
    table = dict() #Meant to contain pairs (author, list_of_instituions)

    for f in all_files :
        for article in utilitary.read_json_list(f) :
            addArticleInstitutions(table, article)

    return table

def putInstitutionsOnDisk(datapath, institupath) :
    """The main function to use to treat the data and list all institutions. Saves on disk."""
    queryFunction = lambda name, paper : ["The cheese alliance"] #TODO move to Priyanka function here
    table = getInstitutions(datapath, queryFunction)
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

#def oneQuery(name, articleName) :
#    """ Fake function, for the time being"""
#    return ["The very serious institution for cheese"]
#
#
#
## print(getInstitutions("../test/filtered_test_data", oneQuery))
#putInstitutionsOnDisk("../test/filtered_test_data", "../test/institutions", oneQuery)
#print("Ok on disk")
#print(getInstitutionsFromDisk("../test/institutions"))

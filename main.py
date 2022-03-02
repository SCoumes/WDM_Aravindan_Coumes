import sys
import os

sys.path.append("src")

args = sys.argv

if len(args) <= 1 :
    print("Please specify a command.")
    print("Usage recap : ")
    print(" sample datapath tempdir nbr_samples")
    print("filter datapath tempdir targetpath fieldname")
    print("compute_institutions datapath institutionpath")
elif args[1] == "test" :
    import WDM_test as test
    if args[2] == "all" :
        test.testAll()
    elif args[2] == "filter" :
        test.testFilter()
    elif args[2] == "institutions" :
        test.testInstitutions()
    elif args[2] == "artToAuth" :
        test.testArtToAuth()
    elif args[2] == "citationCount" :
        test.testCitationCount()
    else :
        print("Unknown test")
elif args[1] == "sample" :
    from  preliminarySort import getfields
    datapath = args[2]
    temp_dir = args[3]
    nbr_samples = int(args[4])
    print(getfields(nbr_samples, datapath, temp_dir))
elif args[1] == "filter" :
    from preliminarySort import filter_data
    from utilitary import clean_folder
    datapath = args[2]
    temp_path = args[3]
    new_datapath = args[4]
    fieldname = args[5]
    clean_folder(new_datapath) 
    filter_data(fieldname, datapath, new_datapath, temp_path)
elif args[1] == "compute_institutions" :
    from getInstitutions import putInstitutionsOnDisk as compInsti
    from utilitary import clean_folder
    datapath = args[2]
    institupath = args[3]
    compInsti(datapath, institupath)
elif args[1] == "artToAuth" :
    from buildArtToAuth import putTableOnDisk
    datapath = args[2]
    targetpath = args[3]
    putTableOnDisk(datapath, targetpath)
elif args[1] == "citation_count" :
    from buildArtToAuth import getTableFromDisk
    from citationCount import putTableOnDisk
    datapath = args[2]
    arttapath = args[3]
    targetpath = args[4]
    
    artToAuth = getTableFromDisk(arttapath)
    timePeriods = [1990, 2000, 2010]
    putTableOnDisk(datapath, targetpath, artToAuth, timePeriods)
elif args[1] == "citation_rings" :
    from ringsCitations import putListsOnDisk
    from citationCount import getTableFromDisk
    citacountpath = args[2]
    targetpath = args[3]

    citationCount = getTableFromDisk(citacountpath)
    putListsOnDisk(citationCount, targetpath)
elif args[1] == "self_citation" :
    from selfCitation import printStatsFromTables
    from citationCount import getTableFromDisk
    citacountpath = args[2]
    citationCount = getTableFromDisk(citacountpath)
    printStatsFromTables(citationCount)
elif args[1] == "parasite" :
    from main_Parasite import __main_parasite__ as parasite
    datapath = args[2]
    maxP = int(args[3])
    parasite(datapath, maxP)
else : 
    print("Unknown command")


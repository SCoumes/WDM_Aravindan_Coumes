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
else : 
    print("Unknown command")


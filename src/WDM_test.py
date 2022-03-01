def testFilter() :
    from preliminarySort import filter_data
    from utilitary import clean_folder
    datapath = "test/test_data"
    temp_path = "temp"
    new_datapath = "test/filtered_test_data"
    fieldname = "Business"
    clean_folder(new_datapath) 
    filter_data(fieldname, datapath, new_datapath, temp_path)

def testInstitutions() :
    from getInstitutions import putInstitutionsOnDisk, getInstitutionsFromDisk
    putInstitutionsOnDisk("test/filtered_test_data", "test/institutions")
    print("Ok on disk")
    print(getInstitutionsFromDisk("test/institutions"))

def testArtToAuth() :
    from buildArtToAuth import putTableOnDisk, getTableFromDisk
    putTableOnDisk("test/filtered_test_data", "test/ArtToAuth")
    print("Ok on disk")
    print(getTableFromDisk("test/ArtToAuth"))
    
def testAll() :
    print("test filter")
    testFilter()
    print("test institutions")
    testInstitutions()
    print("test artToAuth")
    testArtToAuth()

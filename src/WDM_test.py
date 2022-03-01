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
    

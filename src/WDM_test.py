def testInstitutions() :
    from getInstitutions import putInstitutionsOnDisk, getInstitutionsFromDisk
    putInstitutionsOnDisk("test/filtered_test_data", "test/institutions")
    print("Ok on disk")
    print(getInstitutionsFromDisk("test/institutions"))

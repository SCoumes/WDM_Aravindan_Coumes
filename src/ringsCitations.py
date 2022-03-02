import json

def secondHighest(hm) :
    maxkey = None
    maxval = 0
    for key in hm.keys() :
        val = hm[key]
        if val > maxval and key != "total":
            maxval = val
            maxkey = key
    return maxkey, maxval

def getCandidates(author, authorCitations) :
   maxkey, maxval = secondHighest(authorCitations)
   if maxkey == None : return [] #Can't be in a ring if you have no citations
   if maxval * 4 < authorCitations["total"] : return [] #We only care about rings of size 3
   minval = authorCitations["total"] // 2 - maxval
   candidates = []
   if maxkey != author : candidates.append((maxkey, maxval))
   for key in authorCitations.keys() :
       val = int(authorCitations[key])
       if key <= author : continue
       if val >= minval : candidates.append((key, val))
   return candidates

def checkRing(table, mainAuth, candi1, candi2) :
    try : 
        if (table[candi1][mainAuth] + table[candi1][candi2]) * 2 < table[candi1]["total"] : return False
        if (table[candi2][mainAuth] + table[candi2][candi1]) * 2 < table[candi2]["total"] : return False
        return True
    except Exception :
        return False

def getRingsFromCandidates(table, author, candidates) :
    ringList = []
    for (index1, candi1) in enumerate(candidates) : 
        for index2 in range(index1 + 2, len(candidates)) :
            candi2 = candidates[index2]
            if (table[author][candi1] + table[author][candi2]) * 2 < table[author]["total"] :
                break
            if checkRing(table, author, candi1, candi2) :
                ringList.append((author, candi1, candi2))
    return ringList   

def getRingsFromTable(citationCountTable) :
    table= citationCountTable
    allRings = []
    for author in table.keys() :
        candidates = getCandidates(author, table[author])
        candidates.sort(reverse = True, key = lambda a : a[1])
        clean_candidates = [pair[0] for pair in candidates]
        allRings = allRings + getRingsFromCandidates(table, author, clean_candidates)
    return allRings  

def putListsOnDisk(citationCountTables, targetpath) :
    count = 0
    for table in citationCountTables :
        fileList = getRingsFromTable(table)
        with open(targetpath + "/rings_" + str(count) + ".json", "w") as f :
            json.dump(fileList, f)
        count += 1

def getTableFromDisk(targetpath) :
    with open(targetpath, "r") as f :
        return list(json.load(f))


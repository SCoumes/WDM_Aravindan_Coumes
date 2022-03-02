import statistics as stat

def selfCitationList(citationCountTable) :
    table = citationCountTable
    result = []
    for ID in table.keys() :
        if ID in table[ID].keys() :
            result.append(table[ID][ID] / table[ID]["total"])
        else :
            result.append(0)
    return result

def statsFromTable(citationCountTable) :
    L = selfCitationList(citationCountTable)
    nbr_above_half = 0
    for val in L :
        if val > 0.5 : nbr_above_half += 1
    fraction_above_half = nbr_above_half / len(L)

    mean = stat.mean(L)
    median = stat.median(L)

    return(fraction_above_half, mean, median)

def printStatsFromTables(citationCountTables) :
    for table in citationCountTables :
        print(statsFromTable(table))

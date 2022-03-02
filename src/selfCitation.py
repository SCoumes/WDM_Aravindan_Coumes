import statistics as stat

def selfCitationList(citationCountTable) :
    table = citationCountTable
    return [table[ID][ID] / table[ID]["total"] for ID in table.keys()]

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

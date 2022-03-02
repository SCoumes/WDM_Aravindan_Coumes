import itertools as it
import graph_create

def Calculate_Jornal_Score(G, article_journel_map):
    degree = G.Degree(G.nodes())
    journal_article = {}
    for i, v in article_journel_map.items():
        journal_article[v] = [i] if v not in journal_article.keys() else journal_article[v] + [i]
    
    for i in journal_article.keys():
        journal[i] = sum(degree[j] for j in journal_article[i])
    return journel


def NodePersonanlizarion(G, journel):
    Personalization = {}
    for each in G.nodes()
        if(each in article_journel_map.keys()):
            Personalization[each] = journal[article_journel_map[each]]
        else:
            Personalization[each] = G.degree(each)
    return Personalization
	

def sort_Reverse(result, Threshold = 3):
    sortResult = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    final = {k: sortResult[k] for k in it.ifilter(lambda x: x > Threshold, sortResult.keys())}
    return final
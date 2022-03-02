import itertools as it
import graph_create
import matplotlib as plt

def degree_G(G):
    return dict(list(G.in_degree(G.nodes())))

def Calculate_Jornal_Score(G, article_journel_map):
    degree =  degree_G(G)
    journal = {}
    print(degree)
    journal_article = {}
    for i, v in article_journel_map.items():
        journal_article[v] = [i] if v not in journal_article.keys() else journal_article[v] + [i]
    
    try:
        for i in journal_article.keys():
            journal[i] = sum(degree[j] for j in journal_article[i])
    except :
        journal[i] = 1
    return journal



def NodePersonanlizarion(G, journel, article_journel_map):
    Personalization = {}
    for each in G.nodes():
        try:
            if(each in article_journel_map.keys()):
                Personalization[each] = journel[article_journel_map[each]]
            else:
                Personalization[each] = G.degree(each)
        except: 
            Personalization[each] = 1
    return Personalization

def sort_Reverse(result, Threshold = 3):
    final = []
    sortResult = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

    for each in sortResult.keys():
        if(sortResult[each] < Threshold):
            final.append(each)
    return final
    


def visualise(G, path):
    G = nx.complete_graph(5)
    nx.draw(G)
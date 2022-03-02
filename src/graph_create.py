import utilitaries


def Find_Article_Journel_map(article_sample, Max = 6001):
    article_journel_map = {}
    for i in range(1,Max):
        for each in articles_sample[i]:
            try:
                article_journel_map[each['id']]  = each['journalName']      
            except:
                pass
    return article_journel_map
	
def construct_Citation_graph_Edge(articles, k, Max = 6001):
    Edgelist = []
    for i in range(1,Max):
        for each in articles[i]:
            if(each['outCitations'] and each['inCitations'] > k):
                Edgelist.append([(each['id'], out)for out in each['outCitations']])
            if(each['inCitations'] > k):
                Edgelist.append([(inc, each['id'])for inc in each['inCitations']])
    edges = []
    for each in Edgelist:
        for i in each:
            edges.append(i)
    return edges
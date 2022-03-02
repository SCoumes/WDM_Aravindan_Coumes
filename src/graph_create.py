import utilitaries


def Find_Article_Journel_map(article_sample, Max = 6001):
    article_journel_map = {}
    for i in range(1,Max):
        for each in article_sample[i]:
            try:
                article_journel_map[each['id']]  = each['journalName']      
            except:
                pass
    return article_journel_map
	
def construct_Citation_graph_Edge(articles, k, Max ):
    Edgelist = []
    for i in range(1,Max):
        for each in articles[i]:
            if(each['outCitations'] and len(each['inCitations']) > k):
                Edgelist.append([(each['id'], out)for out in each['outCitations']])
            if(len(each['inCitations']) > k):
                Edgelist.append([(inc, each['id'])for inc in each['inCitations']])
    edges = []
    for each in Edgelist:
        for i in each:
            edges.append(i)
    return edges
    
def construct_Citation_graph(articles):
    Citation_Graph = {}
    Max = 6001
    for i in range(1,Max):
        for each in articles[i]:
            try:
                if (each['id'] not in Citation_Graph.keys()):
                    Citation_Graph[each['id']] = []
                Citation_Graph[each['id']].append(each['outCitations'])
                for nodes in article['inCitations']:
                    if (nodes not in Citation_Graph.keys()):
                        Citation_Graph[nodes] = []
                    Citation_Graph[nodes].append(each['id'])
            except:
                pass
        
    return Citation_Graph
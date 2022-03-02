import networkx as nx
import graph_create
import Tools_Parasite


def __main_Parsites__(Path, Max):
    
    
    articles_sample = {}
    
    journels = {}
    
    
    for i in range(1,Max):
        articles_sample[i] = read_json_list( Path + str(i) + '.json')
 
    article_journel_map = Find_Article_Journel_map(article_sample, Max)
    Edgelist =  construct_Citation_graph_Edge(articles_sample, 4)
    
    G = nx.DiGraph(Edgelist)

    p = NodePersonanlizarion(G, journel)
    result  = nx.pagerank(G, personalization = p)
    del_vertices = sort_Reverse(result, 3)
    G.remove_nodes_from(del_vertices)
    
    #I still have to write function for finding the maximum component of a given size
    
 __main_Parsites__(Path, Max) #Please specify path of data and max - number files to be considered out 6000 (if all the files are considered give it as 6001)
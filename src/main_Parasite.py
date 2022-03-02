import networkx as nx
import graph_create
import Tools_Parasite
import visualisetions

import networkx as nx
import json
def __main_Parsites__(Path, Max, Threshold ):
    articles_sample = {}
    journels = {}
    for i in range(1,Max):
        articles_sample[i] = read_json_list( Path + str(i) + '.json')
    article_journel_map =Find_Article_Journel_map(articles_sample, Max)
    
    
    print("commencing construction of edgelist")
    Edgelist =  construct_Citation_graph_Edge(articles_sample, 10, Max)
    
    print("commencing construction of graph")
    G = nx.DiGraph(Edgelist)
    string1 = "Nodes : " + str(G.number_of_nodes()) + ",\t Edges :" + str(G.number_of_edges()) + ", \t Threshold: " + str(Threshold) + "\t Max:" + str(Max) + "\n"
    #print("Finding The base node values based on journels")
    journel = Calculate_Jornal_Score(G, article_journel_map)
    
    p = NodePersonanlizarion(G, journel, article_journel_map)
    
    #print("Pagerank")
    result  = nx.pagerank(G, personalization = p)
    #print(min(result))
    #print(max(result))
    del_vertices = sort_Reverse(result, Threshold) #can chnange this to see how when we change the Threshold for parasite changes the graph
    G.remove_nodes_from(del_vertices)
    #print(len(del_vertices))
    
    #print(largest_cc)
    string2 = "Nodes : " + str(G.number_of_nodes()) + ",\t Edges :" + str(G.number_of_edges()) + ", \t Threshold: " + str(Threshold) + "\t Max:" + str(Max)+ "\n"
    #print(string1)
    #print(string2)
    with open(Path + "ResultsParasite.txt", encoding='utf-8', mode='a') as f:
        f.write(string1)
        f.write(string2)
    visualise(G, 'C:/Users/priya/OneDrive/Documents/ProjectWebData/')
    
__main_Parsites__('C:/Users/priya/OneDrive/Documents/ProjectWebData/S2_filtered/data_', 100, 70) #Please specify path of data and max - number files to be considered out 6000 (if all the files are considered give it as 6001)
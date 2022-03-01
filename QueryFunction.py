from serpapi import GoogleSearch
def queryFunction(title, author):
    Institutes = {}
    string = '+'.join(str.split(title)) + "+" + '+'.join(str.split(author))  
    params = {
        "engine": "google_scholar",
        "q": string,
        "api_key": "255dc7fe9dd992e9626160a1d48557435eacc85f8445f9bbf0d624142d9cfd8d"
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    try: 
        Author_Ids = results['organic_results'][0]['publication_info']['authors']

        for each in Author_Ids:
            intermediate = {}
            params = {
              "engine": "google_scholar_author",
              "author_id": each['author_id'],
              "api_key": "255dc7fe9dd992e9626160a1d48557435eacc85f8445f9bbf0d624142d9cfd8d"
            }


            search = GoogleSearch(params)
            results = search.get_dict()
            try:
                intermediate['name'] = each['name']
                intermediate['affiliations'] = results['author']['affiliations']
                Institutes[each['author_id']]  =  intermediate
                return Institutes
            except KeyError:
                pass
    except KeyError:
        pass
def queryFunction(title, author):
        string = '+'.join(str.split(title).append) + "+" + str('+'.join(str.split(author).append))   
        params = {
            "engine": "google_scholar",
            "q": string,
            "api_key": "255dc7fe9dd992e9626160a1d48557435eacc85f8445f9bbf0d624142d9cfd8d"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        Author_Ids = results['organic_results'][0]['publication_info']['authors']
        Institutes = {}
        for each in Author_Ids:
            params = {
              "engine": "google_scholar_author",
              "author_id": each['author_id'],
              "api_key": "255dc7fe9dd992e9626160a1d48557435eacc85f8445f9bbf0d624142d9cfd8d"
            }
            intermediate['name'] = each['name']
            
            search = GoogleSearch(params)
            results = search.get_dict()
            intermediate['affiliations'] = results['author']['affiliations']
            Institutes[each['author_id']]  =  intermediate
    return Institutes
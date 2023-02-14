from algoliasearch_django import algolia_engine



def get_client():
    return algolia_engine.client


def get_index(index_name='dev__TennisCourt'):
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if 'tags' in kwargs:
        tags = kwargs.pop('tags') or []
        if len() != 0:
            params['filters'] = 'tags:{}'.format(','.join(tags))
    results = index.search(query)
    return results
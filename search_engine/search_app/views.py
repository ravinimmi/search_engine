import json

import requests
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from search_util import SearchUtil

su = SearchUtil()
su.load_data('search_app/data/data.json')
su.generate_inverted_indices()


@csrf_exempt
def search(request):
    data = json.loads(request.body)
    queries = data.get('queries')
    k = data.get('K')

    if k is None:
        return JsonResponse({'message': 'parameter K is missing in request.'}, status=400)
    if queries is None:
        return JsonResponse({'message': 'parameter queries is missing in request.'}, status=400)

    result = []
    for query in queries:
        summaries = su.search(query, k)
        for summary in summaries:
            summary['query'] = query
            summary['author'] = get_author(summary['id'])
        result.append(summaries)

    return JsonResponse(result, safe=False)


def get_author(book_id):
    data = {'book_id': book_id}
    r = requests.post(settings.AUTHOR_API_URL, data=json.dumps(data))
    return r.json()['author']

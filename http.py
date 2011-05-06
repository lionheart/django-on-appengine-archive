from django.http import HttpResponse
from django.utils import simplejson as json

class JsonResponse(HttpResponse):
    def __init__(self, data):
        content = json.dumps(data, ensure_ascii=False)
        super(JsonResponse, self).__init__(content=content,
                mimetype='application/json; charset=utf8')


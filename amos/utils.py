from django.http import QueryDict


def url_with_querystring(path, raw_querystring):
    querystring = QueryDict(raw_querystring)
    return path + '?' + querystring.urlencode(safe='/')

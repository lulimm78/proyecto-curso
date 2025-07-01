from django.http import HttpResponsePermanentRedirect

def redirect_to_www(get_response):
    def middleware(request):
        host = request.get_host()
        if host == "manu-contreras.com":
            return HttpResponsePermanentRedirect("https://www.manu-contreras.com" + request.get_full_path())
        return get_response(request)
    return middleware

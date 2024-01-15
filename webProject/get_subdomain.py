import threading

request_config = threading.local()

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split('.')
        subdomain = host[0] if len(host) > 2 else None
        request_config.subdomain = subdomain
        return self.get_response(request)

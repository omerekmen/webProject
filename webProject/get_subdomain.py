current_subdomain = 2
host = None

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        global current_subdomain
        host = request.get_host().split('.')
        current_subdomain = host[0] if len(host) > 1 else None
        response = self.get_response(request)
        current_subdomain = None  # Reset after request is processed
        return response
from threadlocals.threadlocals import set_thread_variable

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        subdomain = request.get_host().split('.')[0]
        set_thread_variable('subdomain', subdomain)
        response = self.get_response(request)
        return response
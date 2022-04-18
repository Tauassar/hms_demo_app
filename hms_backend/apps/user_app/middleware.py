import time


class DelayMiddleware(object):
    def __init__(self, get_response):
            self.get_response = get_response

    def __call__(self, request):
        time.sleep(0.5)
        return self.get_response(request)

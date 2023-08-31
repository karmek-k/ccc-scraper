class RequestError(BaseException):
    """Error for responses from the `requests` library"""

    def __init__(self, response):
        super().__init__(f'error while requesting {response.url}: status {response.status_code}')

        self.response = response


class ResourceNotFoundError(FileNotFoundError):
    def __init__(self, resource, message=None):
        if message is None:
            message = f'Cannot find resource {resource}'
        
        super().__init__(message)
        

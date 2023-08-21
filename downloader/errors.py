class RequestError(BaseException):
    """Error for responses from the `requests` library"""

    def __init__(self, response):
        super().__init__(f'error while requesting {response.url}: status {response.status_code}')
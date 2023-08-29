class Chapter:
    """`Chapter` contains individual articles"""

    def __init__(self, title, resource_name=None, article_range=None):
        self.title = title
        self.resource_name = resource_name
        self.article_range = article_range

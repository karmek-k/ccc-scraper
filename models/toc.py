class Part:
    """`Part` is a container for other `Part`s"""

    def __init__(self, title, parts=None):
        self.title = title
        self.parts = parts


class Chapter(Part):
    """`Chapter` is a `Part` that contains individual articles"""

    def __init__(self, title, resource_name=None, article_range=None):
        super().__init__(title, None)  # TODO: contains articles, not `None`
        self.resource_name = resource_name
        self.article_range = article_range

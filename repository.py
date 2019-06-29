from github_handler import GitHubHandler


class Repository(object):
    name=""
    handler=None

    def __init__(self, name):
        self.name=name
        self.handler=GitHubHandler(name)
        pass

    def get_report_of_issues(self):
        pass
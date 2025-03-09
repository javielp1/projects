class Park:

    def __init__(self, park_json):
        self.name = park_json['fullName']
        self.url = park_json['url']
        self.state = park_json['states']

    def get_url(self):
        # gets the url for a park
        return self.url

    def get_url_with_park_name_(self):
        # gets the url of the park with the name
        if self.name is not None:
            return self.url

    def get_state(self):
        return self.state

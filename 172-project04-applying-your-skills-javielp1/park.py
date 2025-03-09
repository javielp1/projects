class Park:
    def __init__(self, park_json):
        self.name = park_json['fullName']
        self.url = park_json['url']
        self.description = park_json['description']
        self.image_url = park_json['images'][0]['url']

    def __str__(self):
        return f"Park Name: {self.name}\nID: {self.id}\nURL: {self.url}\nDescription: {self.description}\nImage URL: {self.image_url}"

    def get_park(self):
        return self.name

    def get_url(self):
        return self.url

    def get_description(self):
        return self.description

    def get_image_url(self):
        return self.image_url

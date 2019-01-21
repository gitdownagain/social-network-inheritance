from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp or datetime.utcnow()
        self.user = None # required for user attribute

    def set_user(self, user):
        self.user = user

class TextPost(Post):
    # Need clarification on the init method
    # why doesn't this work with the regular init?
    def __init__(self,text,timestamp=None):
        super(TextPost, self).__init__(text, timestamp) 
        
    def __str__(self):
        formatted_time = self.timestamp.strftime("%A, %b %d, %Y")
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name,self.user.last_name,self.text,formatted_time)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp) #timestamp required?
        self.image_url = image_url
        
    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name,self.user.last_name,self.text,self.image_url,self.timestamp.strftime("%A, %b %d, %Y"))
        


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        return ('@{first_name} Checked In: "{text}"'
                '\n\t{coordinates}\n\t{date}').format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            coordinates="{}, {}".format(self.latitude, self.longitude),
            date=self.timestamp.strftime("%A, %b %d, %Y"))
        
# super added, confused about when to have the additional attributes in the init
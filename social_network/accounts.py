
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email

        # new
        self.following = []
        self.posts = []
        
    def add_post(self, post):
        post.set_user(self)     # FORGOT THIS?!?!
        self.posts.append(post)

    def get_timeline(self):
        # supposed to return each post object such as user2_post1, user2_post2
        a_list_of_posts = []
        
        for a_user in self.following:
            # could be multiple posts
            a_list_of_posts += a_user.posts
       
        return a_list_of_posts

    def follow(self, other):
        self.following.append(other) # if they're following someone, append them to this list     
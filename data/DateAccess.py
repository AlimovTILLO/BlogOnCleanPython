class DataAccessor:
    Users = {}
    Posts = {}

    def initial(self):
        initial_users = {'1': {'Name': 'alimovtillo', 'Fname': 'Tillo', 'Lname': 'Alimov', 'password': '254668kg'},
                         '2': {'Name': 'roma', 'Fname': 'Rakhmatullo', 'Lname': 'Alimov', 'password': '254668kg'},
                         }

        initial_posts = {
            '1': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my first post', 'Active': '1'},
            '2': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my second post', 'Active': '1'},
        }
        self.Users.update(initial_users)
        self.Posts.update(initial_posts)

    def insert(self, post_id, user_id, title, text):
        post = {'%s': {'User_ID': '%s', 'Title': '%s', 'Text': '%s', 'Active': '1'}} % (post_id, user_id, title, text)
        self.Posts.update(post)

    def update(self, post_id, user_id, title, text):
        post = {'%s': {'User_ID': '%s', 'Title': '%s', 'Text': '%s', 'Active': '1'}} % (post_id, user_id, title, text)
        self.Posts.update(post)

    def delete(self):
        del self.Posts['3']

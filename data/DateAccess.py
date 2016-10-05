class DataAccessor:
    Users = {}
    Posts = {}

    def initial(self):
        initial_users = {'1': {'Name': 'alimovtillo', 'Fname': 'Tillo', 'Lname': 'Alimov', 'password': '254668kg'},
                         '2': {'Name': 'alimovtillo', 'Fname': 'Tillo', 'Lname': 'Alimov', 'password': '254668kg'},
                         }

        initial_posts = {
            '1': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my first post', 'Active': 1},
            '2': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my second post', 'Active': 1},
        }
        self.Users.update(initial_users)
        self.Posts.update(initial_posts)

    def insert(self):
        inserted_post = {'3': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my another post', 'Active': 1}}
        self.Posts.update(inserted_post)

    def update(self):
        inserted_post = {'3': {'User_ID': 1, 'Title': 'Hi', 'Text': 'It"s my another post', 'Active': 1}}
        self.Posts.update(inserted_post)

    def delete(self):
        print('gfhjkl')
        del self.Posts['3']

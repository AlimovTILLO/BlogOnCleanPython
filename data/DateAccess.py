import json


class DataAccessor:
    conn = None
    cur = None

    def __init__(self):
        try:
            self.conn = {
                'users': {
                    'user1': {'Name': 'alimovtillo', 'firstname': 'Tillo', 'lastname': 'Alimov', 'password': '254668kg',
                              'posts': {
                                  '1': {'Title': 'Hi', 'text': 'It"s my first post'},
                                  '2': {'Title': 'Hi', 'text': 'It"s my second post'},
                              }, },
                    'user2': {'Name': 'alimovtillo', 'firstname': 'Tillo', 'lastname': 'Alimov',
                              'password': '254668kg'},
                }, }
        except:
            print('Error to connect DB')

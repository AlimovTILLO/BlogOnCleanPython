import json

#
# book = {}
#
# book['rom'] = {
#     'name': 'rom',
#     'address': '126 akhunbaeva, Bishkek',
#     'post': ''
# }
#
# s = json.dumps(book)
# with open("json.txt", "w") as f:
#     f.write(s)
#     print("DONE!!!")
# /////////////////////////////////

#
#
# f = open("json.txt", "r")
# s = f.read()
# book = json.loads(s)
# print(book['tom']['phone'])
# for person in book:
#     print(book[person])
# //////////////////////////////////

# with open('json.txt', 'r+') as f:
#     json_data = json.load(f)
#     json_data['rom']['post'] = {"id": "3", "title": "Hi", "text": "it's my firs post"}
#     f.seek(0)
#     f.write(json.dumps(json_data))
#     f.truncate()


data = {'users': {'user1': {'password': '254668kg', 'firstname': 'Tillo', 'lastname': 'Alimov',
                            'posts': {'post2': {'Title': 'Hi', 'text': 'It"s my second post'},
                                      'post1': {'Title': 'Hi', 'text': 'It"s my first post'}}, 'Name': 'alimovtillo'},
                  'user2': {'password': '254668kg', 'firstname': 'Tillo', 'lastname': 'Alimov', 'Name': 'alimovtillo'}}}

for i in data:
    posts = data['users']['user1']['posts']

data['users']['user1']['posts']['1'] = {'Title': 'Hi', 'text': 'It"s my another post'}

for i in posts:
    title = data['users']['user1']['posts']['%s' % i]['Title']
    text = data['users']['user1']['posts']['%s' % i]['text']
    print(title, text)



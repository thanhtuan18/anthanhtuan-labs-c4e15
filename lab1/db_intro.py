from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds157873.mlab.com:57873/c4e15"

# 1. Mo 1 ket noi
client = MongoClient(mongo_uri)

# 2. Lay cai tu ra
db = client.get_default_database()

# 3. lay tai lieu ra
games = db["game"] # tu dong keo tu ra

game_list = games.find()

for game in game_list:
    print(game["description"])

# # 4. tao 1 tai lieu moi
# new_game = {
#     "title": "Spyfall",
#     "description": "Bluff game"
# }
#
# # 5. dat tai lieu lai vao tu
# games.insert_one(new_game)

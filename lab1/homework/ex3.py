from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
customers = db["customers"]

# Đếm số ref_Cách 1:
# ref1 = 0
# ref2 = 0
# ref3 = 0
#
# for customer in customers.find():
#     if customer["ref"] == "events":
#         ref1 += 1
#     elif customer["ref"] == "ads":
#         ref2 += 1
#     else:
#         ref3 += 1
#
# print(ref1, ref2, ref3)

# Đếm số ref_Cách 2:
n1 = customers.find({"ref": "events"}).count()
n2 = customers.find({"ref": "wom"}).count()
n3 = customers.find({"ref": "ads"}).count()

#####################################

labels = ["events", "wom", "ads"]
values = [n1, n2, n3]

pyplot.pie(values, labels= labels)
pyplot.axis("equal")

pyplot.show()

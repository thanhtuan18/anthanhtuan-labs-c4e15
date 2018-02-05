# from pymongo import MongoClient
#
# mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# client = MongoClient(mongo_uri)
# db = client.get_default_database()
#
# customers = db["customers"]
#
# n1 = customers.find({"ref": "events"}).count()
# n2 = customers.find({"ref": "wom"}).count()
# n3 = customers.find({"ref": "ads"}).count()
#
# print(n1, n2, n3)

# from pymongo import MongoClient
# from matplotlib import pyplot
#
# mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# client = MongoClient(mongo_uri)
# db = client.get_default_database()
# customers = db["customers"]
#
# n1 = customers.find({"ref": "events"}).count()
# n2 = customers.find({"ref": "wom"}).count()
# n3 = customers.find({"ref": "ads"}).count()
#
# values = [n1, n2, n3]
# labels = ["events", "wom", "ads"]
#
# pyplot.pie(values, labels=labels)
# pyplot.axis("equal")
# pyplot.show()

# from pymongo import MongoClient
# from matplotlib import pyplot
#
# mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#
# client = MongoClient(mongo_uri)
# db = client.get_default_database()
# customers = db["customers"]
#
# n1 = customers.find({"ref": "events"}).count()
# n2 = customers.find({"ref": "wom"}).count()
# n3 = customers.find({"ref": "ads"}).count()
#
# values = [n1, n2, n3]
# labels = ["events", "wom", "ads"]
#
# pyplot.pie(values, labels=labels)
# pyplot.axis("equal")
# pyplot.show()

# from pymongo import MongoClient
#
# mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# client = MongoClient(mongo_uri)
# db = client.get_default_database()
# posts = db["posts"]
# post_new = {
#     "title": "U23 Việt Nam",
#     "author": "ATT",
#     "content": """
#     Việt Nam ơi, chiều Thường Châu trắng xóa
#     90 triệu người dõi theo bước những chiến binh
#     Ôi những đôi chân không hề mệt mỏi
#     Dẫu tuyết kia rơi tàn nhẫn vô tình
#     Thua 1 trận và thủ hòa 1 trận
#     Thắng 3 lần- chỉ vậy đã thành danh
#     Dẫu gục ngã trước thiên đường uất hận
#     Nhưng ngọn đuốc tim anh đã cháy cạn trước khung thành
#     Hãy ngừng rơi đi em những giọt buồn tiếc nuối
#     Hãy thắp sáng tự hào ngọn lửa trái tim
#     Trận chiến này không có nghĩa là trận cuối
#     Chiến thắng lớn hơn là chiến thắng chính mình
#     Ta đã ngẩng cao đầu với năm châu bốn biển
#     Con thuyền Việt Nam đã rẽ sóng băng mình
#     Trước thử thách, gian nan càng quyết chí
#     Ta chẳng sợ điều gì khi là những chiến binh
#     Ta vô địch dẫu ta không đoạt cúp
#     Những chàng trai kiên cường đưa lịch sử sang trang
#     Bóng đá Việt Nam đã ghi danh châu lục
#     Tổ quốc đón các anh như những anh hùng..."""
# }
#
# posts.insert_one(post_new)

from datetime import datetime

now = datetime.now()

print(now.year, now.month)

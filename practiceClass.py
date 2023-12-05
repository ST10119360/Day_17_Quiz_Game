# Creating classes
# class User:
#     def __init__(self,id,username):
#         print("new User being created...")
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1# self is used to reference the object being created
#
# user_1 = User("001","Josh")
# print(user_1.username, user_1.id)
#
# user_2 = User("002","Jared")
# print(user_2.id)
# user_1.follow(user_2)
# print(user_1.followers, user_1.following)
# print(user_2.followers, user_2.following)
class User:
    def __init__(self, user_id, user_name):
        print('new user being created...')
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

user1 = User('001', 'Nick')
# print(user1.name)
user2 = User('002', 'Jack')
user1.follow(user2)

print(user1.follower)

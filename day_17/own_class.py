class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.follower = 0  # this is a default value.
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = User(1, "Satyam")
user2 = User(2, "Shivam")

print(user1.name)
print(user1.id)
print(user2.name)
print(user2.id)

user1.follow(user2)
print(f"{user1.name} follower is {user1.follower}")
print(f"{user1.name} following is {user1.following}")

print(f"{user2.name} follower is {user2.follower}")
print(f"{user2.name} following is {user2.following}")
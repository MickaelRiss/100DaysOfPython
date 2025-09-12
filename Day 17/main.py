class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(1,"Mickael")
user_2 = User(2,"Chloe")

print("Avant le follow:")
print(f"{user_1.username} a {user_1.followers} followers et follow {user_1.following} personnes.")
print(f"{user_2.username} a {user_2.followers} followers et follow {user_2.following} personnes.")

user_1.follow(user_2)

print("Apres le follow:")
print(f"{user_1.username} a {user_1.followers} followers et follow {user_1.following} personnes.")
print(f"{user_2.username} a {user_2.followers} followers et follow {user_2.following} personnes.")

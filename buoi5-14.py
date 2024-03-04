class StarCookie:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

#star_cookie1 = StarCookie()
#star_cookie1.weight = 15
#star_cookie1.color = "Red"
#print(star_cookie1.weight)
#print(star_cookie1.color)

#star_cookie2 = StarCookie()
#star_cookie2.weight = 16
#star_cookie2.color = "Blue"
#print(star_cookie2.weight)
#print(star_cookie2.color)

class Youtube:
    def __init__ (self, username, subscribers = 0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = Youtube("Elshad")
print(user1.username)
print(user1.subscribers)

user2 = Youtube("Renad")
user2.subscribers = 5
print(user2.username)
print(user2.subscribers)

user1.subscribe(user2)
user2.subscribe(user1)
print(f"user 1 subscribers: {user1.subscribers}")
print(f"user 1 subscriptions: {user1.subscriptions}")
print(f"user 2 subscribers: {user2.subscribers}")
print(f"user 2 subscribers: {user2.subscriptions}")

# def greet():
#     friend = yield  # generator
#     print(f"Hello, {friend}")


# g = greet()
# g.send(None)    # priming the generator
# g.send("Friend")


from collections import deque

friends = deque(("FriendOne", "SecondFriend", "AnotherFriend"))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

# or
"""
def greet(g):
    yield from g
"""


greeter = greet(friend_upper())

greeter.send(None)
greeter.send("Hello")
print("Print something")
greeter.send("How are you,")
from collections import deque
from types import coroutine

friends = deque(("FriendOne", "SecondFriend", "AnotherFriend"))

@coroutine              # !!!!
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")


async def greet(g):
    print("Starting...")
    await g             # this is exactly the same as `yield from g`
    print("Ending...")


greeter = greet(friend_upper())

greeter.send(None)
greeter.send("Hello")
print("Print something")
greeter.send("How are you,")
greeter.send("How are you,")
greeter.send("How are you,")
greeter.send("How are you,")
greeter.send("How are you,")
import time
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(["install", "pyfirmata"])
    from pyfirmata import Arduino, util

board = Arduino("port_here")

iterator = util.Iterator(board)
iterator.start()

v1 = board.get_pin("a:0:i")

time.sleep(1.0)
print(v1.read())

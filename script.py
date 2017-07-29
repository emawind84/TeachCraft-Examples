import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'. Replace with your own IP/name!
mc = minecraft.Minecraft.create(address="127.0.0.1", name="Surfernight")

# PUT CODE HERE.
# Checkout the /examples directory with ready-to-go scripts, all you need to do is update your IP and name in them! 


x = 110
z = 14
y = 64

while True:
    pos = mc.player.getTilePos()

    print "x", pos.x
    print "y", pos.y
    print "z", pos.z

    # If player position is same as teleportation pad...
    if pos.x == x and pos.z == z and pos.y == y:
        # We are on the teleportation pad!
        mc.postToChat("Beam me up, Scotty!")
    time.sleep(.1)
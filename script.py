import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'. Replace with your own IP/name!
mc = minecraft.Minecraft.create(address="127.0.0.1", name="Surfernight")

# PUT CODE HERE.
# Checkout the /examples directory with ready-to-go scripts, all you need to do is update your IP and name in them! 

x,y,z = mc.player.getTilePos()
print x,y,z
#mc.player.setTilePos(x, y+40 , z)
from mcpi import minecraft 
import mcpi.block as block 
import time

# Draw a corner tower
def drawTower(x,y,z):

	# Draw a block and hollow it out
        mc.setBlocks(x,y,z,x+6,y+10,z+6, block.STONE_BRICK)
        mc.setBlocks(x+1,y,z+1,x+5,y+9,z+5, block.AIR)

	# Then add the castelations on the top.
        for n in range(0,7,2):
           	mc.setBlock(x+n,y+11,z,block.STONE_BRICK)
                mc.setBlock(x+n,y+11,z+6,block.STONE_BRICK)

                mc.setBlock(x,y+11,z+n,block.STONE_BRICK)
                mc.setBlock(x+6,y+11,z+n,block.STONE_BRICK)

        # add caseltation
        #for n in xrange(x,x+7,2):

	#	print n,y+11,z
                #mc.setBlock(n,y+11,z,block.STONE_BRICK)
                #mc.setBlock(n,y+11,z+6,block.STONE_BRICK)
                
	#	print x,y+11,n 
        #        mc.setBlock(x,y+11,n,block.STONE_BRICK)
        #        mc.setBlock(x+6,y+11,n,block.STONE_BRICK)

# Draw a wall in either the x or z direction        
def drawWall(x,y,z,direction):

        if direction==1:
                mc.setBlocks(x,y,z,x+11,y+7,z,block.STONE_BRICK)
        else:
                mc.setBlocks(x,y,z,x,y+7,z+11,block.STONE_BRICK)

# Draw a castle, consisting of 4 towers, and 4 walls.
def drawCastle(x,y,z):

        drawTower(x,y,z)
        drawTower(x+17,y,z)
        drawTower(x,y,z+17)
        drawTower(x+17,y,z+17)

        drawWall(x+7,y,z+1,1)
        drawWall(x+7,y,z+22,1)
        drawWall(x+1,y,z+7,0)
        drawWall(x+22,y,z+7,0)

# Draw a lenght of fence. Note that we look to see the height of the terrain and 
# build the fance at that height. Can get a bit wierd if there is a tree in the way!
#def drawFence(xPos,zPos):

	# How big of a fence?
#	size = 39

	# Draw the x direction fence
#	for n in range(xPos,xPos+size):
#		y = mc.getHeight(n,zPos)
#        	mc.setBlock(n,y,zPos,block.FENCE)
#        	mc.setBlock(n,y+1,zPos,block.FENCE)
#		y = mc.getHeight(n,zPos+size)
#        	mc.setBlock(n,y,zPos+size,block.FENCE)
#        	mc.setBlock(n,y+1,zPos+size,block.FENCE)

	# Then the z direction fence
#	for n in range(zPos,zPos+size):
#		y = mc.getHeight(xPos,n)
#        	mc.setBlock(xPos,y,n,block.FENCE)
#        	mc.setBlock(xPos,y+1,n,block.FENCE)
#		y = mc.getHeight(xPos+size,n)
#        	mc.setBlock(xPos+size,y,n,block.FENCE)
#        	mc.setBlock(xPos+size,y+1,n,block.FENCE)

def drawFenceEx(xPos,zPos):

	# How big of a fence?
	size = 39
	height = 2

	# Draw the x direction fence
	for n in range(xPos,xPos+size):
		y = mc.getHeight(n,zPos)
        	mc.setBlocks(n,y,zPos,n,y+height,zPos,block.FENCE)
		y = mc.getHeight(n,zPos+size)
        	mc.setBlocks(n,y,zPos+size,n,y+height,zPos+size,block.FENCE)

	# Then the z direction fence
	for n in range(zPos,zPos+size):
		y = mc.getHeight(xPos,n)
        	mc.setBlocks(xPos,y,n,xPos,y+height,n,block.FENCE)
		y = mc.getHeight(xPos+size,n)
        	mc.setBlocks(xPos+size,y,n,xPos+size,y+height,n,block.FENCE)

#def drawFoundationsOld(x,y,z):

	# Draw a huge block of stone and clear a huge block or air above it

#	mc.setBlocks(x-2,y,z-2,x+33,y-10,z+35,block.MOSS_STONE)
#	mc.setBlocks(x-2,y,z-2,x+33,y+20,z+35,block.AIR)

	# Hoolow out the block to make a huge dungeaon
#	mc.setBlocks(x+1,y-3,z+1,x+32,y-9,z+32,block.AIR)

	# TODO : what is this? And a hole to get into the cave - 
	# mc.setBlock(x+10,y,z+10,block.AIR)

# Draw a set of foundations to build the castle one. thats a block, hollowewed 
# out to make a cellar, and a moat
def drawFoundations(x,y,z):

	# Draw a huge block of stone and clear a huge block or air above it
	mc.setBlocks(x,y,z,x+37,y-10,z+37,block.MOSS_STONE)
	mc.setBlocks(x,y+1,z,x+37,y+20,z+37,block.AIR)

	# Clear a space that will become the moat
	mc.setBlocks(x+1,y-1,z+1,x+36,y,z+36,block.WATER)

	# And raise a platform for the castle
	mc.setBlocks(x+3,y,z+3,x+34,y-1,z+34,block.MOSS_STONE)

	# Hollow out the block to make a huge dungeaon
	mc.setBlocks(x+1,y-3,z+1,x+32,y-9,z+32,block.AIR)

# Get a connection to the game. Work out where the player is
mc = minecraft.Minecraft.create()
xPos,yPos,zPos = mc.player.getTilePos()

# And draw the castle
drawFoundations(xPos-4,yPos,zPos-4)
drawCastle(xPos+2,yPos,zPos)
drawFenceEx(xPos-5,zPos-5)



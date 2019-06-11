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
        
def drawWall(x,y,z,direction):

        if direction==1:
                mc.setBlocks(x,y,z,x+11,y+7,z,block.STONE_BRICK)
        else:
                mc.setBlocks(x,y,z,x,y+7,z+11,block.STONE_BRICK)

def drawCastle(x,y,z):

        #mc.setBlocks(x,y,z,x+22,y,z+22,block.COBBLESTONE)
        
        drawTower(x,y,z)
        drawTower(x+17,y,z)
        drawTower(x,y,z+17)
        drawTower(x+17,y,z+17)

        drawWall(x+7,y,z+1,1)
        drawWall(x+7,y,z+22,1)
        drawWall(x+1,y,z+7,0)
        drawWall(x+22,y,z+7,0)

def drawFence(xPos,zPos):
	for n in range(xPos,xPos+30):
		y = mc.getHeight(n,zPos)
        	mc.setBlock(n,y,zPos,block.FENCE)
        	mc.setBlock(n,y+1,zPos,block.FENCE)
		y = mc.getHeight(n,zPos+30)
        	mc.setBlock(n,y,zPos+30,block.FENCE)
        	mc.setBlock(n,y+1,zPos+30,block.FENCE)

	for n in range(zPos,zPos+30):
		y = mc.getHeight(xPos,n)
        	mc.setBlock(xPos,y,n,block.FENCE)
        	mc.setBlock(xPos,y+1,n,block.FENCE)
		y = mc.getHeight(xPos+30,n)
        	mc.setBlock(xPos+30,y,n,block.FENCE)
        	mc.setBlock(xPos+30,y+1,n,block.FENCE)

# Draw a moat around the outside
def drawMoat(x,y,z):

	#medium = block.WATER
	medium = block.GOLD_BLOCK

	mc.setBlocks(x,y-1,z,x+32,y-2,z-1,medium)
	mc.setBlocks(x,y-1,z+32,x+32,y-2,z+33,medium)

	mc.setBlocks(x,y-1,z,x-1,y-2,z+32,medium)
	#mc.setBlocks(x+32,y-1,z,x+32,y-2,z+32,medium)

def drawFoundations(x,y,z):

	# Draw a huge block of stone and clear a huge block or air above it

	mc.setBlocks(x-2,y,z-2,x+33,y-10,z+35,block.MOSS_STONE)
	mc.setBlocks(x-2,y,z-2,x+33,y+10,z+35,block.AIR)

	# Hoolow out the block to make a huge dungeaon
	mc.setBlocks(x+1,y-3,z+1,x+32,y-9,z+32,block.AIR)

	# TODO : what is this? And a hole to get into the cave - 
	# mc.setBlock(x+10,y,z+10,block.AIR)

def drawFoundationsEx(x,y,z):

	# Draw a huge block of stone and clear a huge block or air above it
	mc.setBlocks(x,y,z,x+37,y-10,z+37,block.MOSS_STONE)
	mc.setBlocks(x,y+1,z,x+37,y+10,z+37,block.AIR)

	# Clear a space that will become the moat
	mc.setBlocks(x+1,y-1,z+1,x+36,y,z+36,block.WATER)
	#mc.setBlocks(x+2,y-2,z+2,x+36,y-1,z+36,block.AIR)

	# And raise a platform for the castle
	mc.setBlocks(x+3,y,z+3,x+34,y-1,z+34,block.MOSS_STONE)

	# Hollow out the block to make a huge dungeaon
	mc.setBlocks(x+1,y-3,z+1,x+32,y-9,z+32,block.AIR)

mc = minecraft.Minecraft.create()
xPos,yPos,zPos = mc.player.getTilePos()

drawFoundationsEx(xPos-4,yPos,zPos-4)
drawFence(xPos-3,zPos-3)
#drawCastle(xPos+2,yPos,zPos)
#drawMoat(xPos-4,yPos,zPos-4)

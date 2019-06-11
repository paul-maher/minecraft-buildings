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

def drawMoat(x,y,z):
	mc.setBlocks(x,y-1,z,x+32,y+2,z,block.AIR)
	mc.setBlocks(x,y-1,z+32,x+32,y+1,z+32,block.AIR)

	mc.setBlocks(x,y-1,z,x,y+2,z+32,block.AIR)
	mc.setBlocks(x+32,y-1,z,x+32,y+2,z+32,block.AIR)

def drawFoundations(x,y,z):
	mc.setBlocks(x,y,z,x+33,y-10,z+33,block.MOSS_STONE)
	mc.setBlocks(x,y,z,x+33,y+10,z+33,block.AIR)
	mc.setBlocks(x+1,y-3,z+1,x+32,y-9,z+32,block.AIR)
	mc.setBlock(x+10,y,z+10,block.AIR)
	
mc = minecraft.Minecraft.create()
xPos,yPos,zPos = mc.player.getTilePos()

drawFoundations(xPos-4,yPos,zPos-4)
drawFence(xPos-3,zPos-3)
drawCastle(xPos+2,yPos,zPos)
drawMoat(xPos-4,yPos,zPos-4)

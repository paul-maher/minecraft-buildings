from mcpi import minecraft 
import mcpi.block as block 
import time 
import random

# Draw a set of stairs going up
def drawStairs(x,y,z,flights):

	for n in range(0,flights):
		
		# draw blocks (only on the ground flooor!)
		#mc.setBlock(x+1,y,z, block.STONE)		
		#mc.setBlock(x+2,y,z, block.STONE)		
		#mc.setBlock(x+3,y,z, block.STONE)
		#mc.setBlock(x+2,y+1,z, block.STONE)
		#mc.setBlock(x+3,y+1,z, block.STONE)
                #mc.setBlock(x+3,y+2,z, block.STONE)

		# draw stairs
		mc.setBlock(x,y,z,block.STAIRS_WOOD)		
		mc.setBlock(x+1,y+1,z,block.STAIRS_WOOD)		
		mc.setBlock(x+2,y+2,z,block.STAIRS_WOOD)
		mc.setBlock(x+3,y+3,z, block.STAIRS_WOOD)
		
		# knock thru
		mc.setBlock(x,y+3,z,block.AIR)
		mc.setBlock(x+1,y+3,z,block.AIR)
		mc.setBlock(x+2,y+3,z,block.AIR)
		#mc.setBlock(x+3,y+3,z,block.AIR)
		
		y+=4
			
# Draw one set of blocks of a skyscraper
def drawLevel(xStart, yStart, zStart, xSize, zSize, brickType, floorType):
    for x in range(0, xSize):
        for z in range(0, zSize):
            if x == xSize-1 or z == zSize-1 or x == 0 or z == 0:
                print xStart+x, yStart, zStart+z, brickType
                mc.setBlock(xStart+x, yStart, zStart+z, brickType)
                time.sleep(0.05)
            else:
                print xStart+x, yStart, zStart+z, floorType
                mc.setBlock(xStart+x, yStart, zStart+z, floorType)
                time.sleep(0.05)

# Draw one storey of a skyscraper
def drawStorey(xStart, yStart, zStart, xSize, zSize, brickType, floorType, needsARoof):

    #Draw floor first
    drawLevel(xStart,yStart,zStart,xSize,zSize,brickType, floorType)
    print "draw wall...."
    # Draw wall
    drawLevel(xStart,yStart+1,zStart,xSize,zSize,brickType, block.AIR)
    drawLevel(xStart,yStart+2,zStart,xSize,zSize,brickType, block.AIR)
    drawLevel(xStart,yStart+3,zStart,xSize,zSize,brickType, block.AIR)
    
    # Add a roof if needed
    if needsARoof == True:
        drawLevel(xStart,yStart+4,zStart,xSize,zSize,brickType, brickType)

    # Add Windows

# Draw a multi level skyscraper
def drawSkyscraper(xStart, yStart, zStart, xSize, ySize,brickType, floorType, stories):
    for x in range(0,stories-1):
	drawStorey(xStart,(yStart+x*4),zStart,xSize,ySize,brickType,floorType,False)
    drawStorey(xStart,(yStart+(stories-1)*4),zStart,xSize,ySize,brickType,floorType,True)

    drawStairs(xStart+3,yStart+1,zStart+ySize-2,stories-1)

# Draw a road in eother the X or Z planes
def drawARoad(direction, length, width):

    # Start from under the players feet
    xPos,yPos,zPos = mc.player.getTilePos()

    if direction == 1:
        xEnd = xPos + length
        zEnd = zPos + width
    elif direction == 2:
        zEnd = zPos + length
        xEnd = xPos + width
    elif direction == 3:
        xEnd = xPos - length
        zEnd = zPos + width
    elif direction == 4:
        zEnd = zPos - length
        xEnd = xPos + width

    print xPos, zPos, xEnd, zEnd

    for x in range(xPos, xEnd):
        for z in range(zPos, zEnd):
             #print x, yPos, z
             mc.setBlock(x, yPos, z, block.STONE)
             mc.setBlock(x, yPos+1, z, block.AIR)
             mc.setBlock(x, yPos+2, z, block.AIR)
             mc.setBlock(x, yPos+3, z, block.AIR)
             time.sleep(0.1)

# Connect to gamne
mc = minecraft.Minecraft.create()
xPos,yPos,zPos = mc.player.getTilePos()

# Draw a house near me
drawSkyscraper(xPos+2, yPos, zPos+1, 8, 8, block.IRON_BLOCK, block.SANDSTONE, 8)

#draw a road near me
#drawARoad(1,30,3)
#drawARoad(2,30,3)
#drawARoad(3,30,3)
#drawARoad(4,30,3)

# this is TNT that explodes when you hit it
#mc.setBlock(xPos,yPos,zPos,block.TNT.0)



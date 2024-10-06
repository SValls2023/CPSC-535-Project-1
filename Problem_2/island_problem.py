# Input: 2D array of 0's & 1's, where 0 represents part of a land mass & 1 represents water
# Output: Count of 0's forming the largest possible land mass after changing exactly one 1 to 0

def findLargestIsland(matrix): # MAIN Function
    if not matrix: #If input is empty, Return 0
        return 0
        
    rows_size = len(matrix)
    cols_size = len(matrix[0]) #Finding size rows,columns of matrix
    allSizes = {} #For storing land mass sizes
    visitedMatrix = [[False]*cols_size for _ in range(rows_size)] #Tracking visited cells
    directionsAllowed=[(1, 0),(-1, 0),(0, 1),(0, -1)] #Allowed directions (up, down, left, right) respectively
    
    def depthFirstSearch(r,c,landmassId): #Performing Depth First Search
        stack = [(r,c)] 
        size = 0
        while stack:
            x,y = stack.pop()
            if visitedMatrix[x][y]: #Check if cell is already visited
                continue
            visitedMatrix[x][y] = True #Mark current cell visited
            size += 1 #Increment the size of the land mass
            allSizes[landmassId].add((x, y)) #Add the cell to the current land mass
            
            #Explore the four possible directions from the current cell
            for drows,dcols in directionsAllowed:
                nr,nc = x+drows, y+dcols
                
            #Check if the neighbor is within bounds, unvisited, and part of land (0)
                if 0 <= nr < rows_size and 0<=nc<cols_size and not visitedMatrix[nr][nc] and matrix[nr][nc]==0:
                    stack.append((nr, nc)) #Add the neighbor of current cell to the stack

        return size #size of the land mass found

    #Calculate for all land masses
    landmassId=0 #For every land mass, start from 0
    for r in range(rows_size):
        for c in range(cols_size):
        # If the cell is land (0) and has not been visited, perform DFS
            if matrix[r][c]==0 and not visitedMatrix[r][c]:
                allSizes[landmassId]=set()
                size=depthFirstSearch(r,c,landmassId) #Calculate the size of this land mass
                landmassId+=1 #Increment the land mass ID

    maxLandmass=0 #Track the maximum land mass size

    #Evaluate changing each '1' to '0' to see the effect on land mass size
    for r in range(rows_size):
        for c in range(cols_size):
            if matrix[r][c]==1: #Check if the current cell is water i.e. 1
                adjacentLandmassIds=set() #Set to track adjacent land masses
                
                #Check all neighboring cells to find adjacent land masses
                for drows,dcols in directionsAllowed:
                    nr,nc=r+drows,c+dcols #Find the coordinates of the neighboring cell
                    
                    #If the neighboring cell is within bounds and is land i.e. 0
                    if 0<=nr<rows_size and 0<=nc<cols_size and matrix[nr][nc]==0:
                        for landmassId in allSizes:
                        #If the neighboring cell belongs to a land mass, add its ID
                            if (nr,nc) in allSizes[landmassId]:
                                adjacentLandmassIds.add(landmassId)

                newLandmassSize=1
                for landmassId in adjacentLandmassIds:
                    newLandmassSize+=len(allSizes[landmassId]) #Add sizes of adjacent land masses
                maxLandmass=max(maxLandmass,newLandmassSize) #Update the maximum_land_mass size
    return maxLandmass #Return the largest land mass found



def main():
    file = open('input.txt', 'r')
    read = file.readlines()
    test_matrix = []

    for line in read:
        lineData = [int(x) for x in line.strip().split(", ")]
        test_matrix.append(lineData)
    
    largest = findLargestIsland(test_matrix)
    print(largest)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
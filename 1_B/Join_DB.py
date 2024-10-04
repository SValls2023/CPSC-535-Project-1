# Create database based on file inputs
def makeDatabase(fileString):
    file = open(fileString, 'r')
    read = file.readlines()
    file.close()
    database = []
    for line in read:
        lineData = line.strip().split(", ")
        dbTuple = (lineData[0], lineData[1])
        database.append(dbTuple)
    return database

# Input: Two databases, L and R, each with k elements
# Output: A joined database with shared k elements between L and R
def joinDatabase(leftDB, rightDB):
    if leftDB == None or rightDB == None:
        return None
    
    dbDictionary = {}
    joinedDB = []

    for i in range(len(leftDB)):
        tupleItem = leftDB[i]
        dbDictionary.update({tupleItem[0] : i})

    for j in rightDB:
        key = j[0]
        value = j[1]
        if dbDictionary.get(key) != None:
            joinedDB.append((key, leftDB[dbDictionary[key]][1], value))

    return joinedDB

def main():
    # Get file input for both databases
    databaseA = makeDatabase('dataBaseA.txt')
    databaseB = makeDatabase('dataBaseB.txt')
    joinedDatabase = joinDatabase(databaseA, databaseB)
    print(joinedDatabase)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
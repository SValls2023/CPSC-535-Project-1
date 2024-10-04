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
    # If leftDB ir rightDB are empty, return an empty list
    if leftDB == None or rightDB == None:
        return []
    
    dbDictionary = {}
    joinedDB = []

    # Store all leftDB elements in dictionary (Key: Name, Value: Index Location)
    for i in range(len(leftDB)):
        tupleItem = leftDB[i]
        dbDictionary.update({tupleItem[0] : i})

    # If the rightDB contains a name found in leftDB, store the key in joinedDB with both its leftDB and rightDB values
    for j in rightDB:
        key = j[0]
        value = j[1]
        if dbDictionary.get(key) != None:
            joinedDB.append((key, leftDB[dbDictionary[key]][1], value))

    return joinedDB

def main():
    # Get file input for both databases
    databaseA = makeDatabase('databaseA.txt')
    databaseB = makeDatabase('databaseB.txt')
    joinedDatabase = joinDatabase(databaseA, databaseB)
    print(joinedDatabase)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
# Input: List of item tuples (price, item) and target sum
# Output: Item pair that adds up to the target sum
def shipTwoItems(product_list, target):
    # If item list is empty, return NIL
    if not product_list:
        return "NIL"
    
    # Dictionary to store all previous looked at items 
    itemDictionary = {}
    targetProducts = []
    
    # Loop through all items in the list
    for i in range(len(product_list)):
        tupleItem = product_list[i]
        targetDifference = target - tupleItem[0]
        # If item in dictionary matches with targetDifference, return pair (current item, dictionary item)
        if itemDictionary.get(targetDifference) != None:
            targetProducts.append(tupleItem)
            targetProducts.append(product_list[itemDictionary[targetDifference]])
            return targetProducts
        # Add item to dictionary if a pair has not been found
        itemDictionary.update({tupleItem[0] : i})

    return "NIL"


def main():
    # Get file input
    file = open('items.txt', 'r')
    read = file.readlines()
    itemList = []

    for line in read:
        lineData = line.strip().split(", ")
        itemTuple = (int(lineData[0]), lineData[1])
        itemList.append(itemTuple)

    # Get user input for target sum
    targetSum = int(input("Enter a target sum: "))

    # Run Algorithm
    targetSumPair = shipTwoItems(itemList, targetSum)

    # Print results
    print(targetSumPair)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
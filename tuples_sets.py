# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get Value
# print(fruits[1])

# Can't changes value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get Length
# print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# Check if in set
# print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Add to duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete set
del fruits_set

print(fruits_set)

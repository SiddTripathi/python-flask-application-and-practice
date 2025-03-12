#Now lets understand the advanced set operations in python

friends = {'John', 'Michael', 'Tom', 'Eric', 'Michael'}
friends_abroad = {'John', 'Michael'}
new_friends = {'Mike', 'Harvey', 'Jessica','John'}

local_friends = friends.difference(friends_abroad) #difference method removes the items that are in the second set from the first set
print(f"The local friends are {local_friends}")

#if you do reverse of the above operation you will get empty set as the items in the second set are already in the first set
reverse_friends_abroad = friends_abroad.difference(friends)
print(f"The reverse friends abroad will be empty list {reverse_friends_abroad}")



#union method combines the items in both sets and removes the duplicates
all_friends = friends.union(new_friends)
print(f"All friends are {all_friends}")


#intersection method returns the items that are common in both sets
common_friends = friends.intersection(friends_abroad)
print(f"The common friends are {common_friends}")
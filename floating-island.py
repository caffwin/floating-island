

# Given a rectangular matrix containing only the values “0” and “1”, where the values of “1”
# always appear in the form of a rectangular island and the islands are always separated
# row-wise and column-wise by at least one line of “0”s, count the number of islands in the
# given matrix. Note that the islands can only be diagonally adjacent.
# Input: Matrix of elements with values either 0 or 1
# Output: An integer which is the count of all rectangular islands

Input: 
[[1, 1, 0, 1],
 [1, 1, 0, 1],
 [0, 0, 1, 0],
 [0, 0, 1, 0]]

=> Output: 3
    
# iterate through the lists for each row
# iterate through each row at a specific index to access columns

# Check first to see which other coordinates (beside or above) are part of the island
# if we hit a 0, that indicates that we've hit "water"

# 0, 0 is the number to "inspect" 
# 0, 1
# 1, 0
# If these are part of the island, continue looking:

# 0, 2
# 2, 0

# minimum condition to know if another island is separate is if both coordinates are 1 apart
# 1, 1 -> 2, 2 new island

# 2, 2 -> 2, 3 not a new island

# 2, 2 -> 1, 3 is a new island
# difference between first and second coordinates greater than 2 = new island
print("Welcome to Treasure Map!\n")

r1 = ["🥰", "🥶", "😓"]
r2 = ["👀", "🦹‍♀️", "💑"]
r3 = ["🩰", "👑", "🚵🏻‍♂️"]

treasure_map = [r1, r2, r3]

print(f"{r1}\n{r2}\n{r3}\n")

position = input("Enter the position (row,col) where you want to put the treasure ")

row, col = int(position[0]),int(position[1])

treasure_map[row - 1][col - 1] = "💰"

print(f"\nUpdated Map:\n{r1}\n{r2}\n{r3}")


# print("Welcome to Treasure Map!\n")

# r1 = ["🥰", "🥶", "😓"]
# r2 = ["👀", "🦹‍♀️", "💑"]
# r3 = ["🩰", "👑", "🚵🏻‍♂️"]

# treasure_map = [r1, r2, r3]

# print(f"{r1}\n{r2}\n{r3}\n")

# position = input("Enter the position (row,col) where you want to put the treasure (e.g., 2,3): ")

# # Splitting input into row and column
# row, col = map(int, position.split(','))  [hey int() is a function to convert to int ]

# # Placing treasure at the specified location
# treasure_map[row - 1][col - 1] = "💰"

# # Display the updated map
# print(f"\nUpdated Map:\n{r1}\n{r2}\n{r3}")
 
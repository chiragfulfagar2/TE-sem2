g=0
def print_board(elements): #Defines a function print_board that takes a list elements as input and prints it as a 3x3 board.
    for i in range(9): 
        if i%3 == 0:  #Checks if the current index is divisible by 3. If true, it means a new row is starting, so a newline is printed.
            print()
        if elements[i]==-1:
            print("_", end = " ")
        else:
            print(elements[i], end = " ")
    print()

def solvable(start): #Defines a function solvable that takes a list start as input and checks if the puzzle is solvable.
    inv=0

    for i in range(9):
        if start[i] <= 1:
            continue
        for j in range(i+1,9):
            if start[j]==-1:
                continue
            if start[i]>start[j]:
                inv+=1
    if inv%2==0:
        return True
    return False

def heuristic(start,goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3
    return h + g

def moveleft(start,position):
    start[position],start[position-1]= start[position-1],start[position]
    

def moveright(start,position):
    start[position],start[position+1]= start[position+1],start[position]
    

def moveup(start,position):
    start[position],start[position-3]= start[position-3],start[position]
    

def movedown(start,position):
    start[position],start[position+3]= start[position+3],start[position]
    

def movetile(start,goal):
    emptyat= start.index(-1)
    row = emptyat//3
    col = emptyat%3
    t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
    f1,f2,f3,f4 = 100,100,100,100

    if col -1 >=0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col+1<3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 <3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row-1>=0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heuristic = min(f1, f2,f3,f4)

    if f1==min_heuristic:
        moveleft(start, emptyat)
        print("move tile to left")
    elif f2==min_heuristic:
        moveright(start, emptyat)
        print("move tile to right")
    elif f3==min_heuristic:
        movedown(start, emptyat)
        print("move tile down")
    elif f4 == min_heuristic:
        moveup(start, emptyat)
        print("move tile up")
        
        
def solveEight(start,goal):
    global g
    g+=1
    movetile(start,goal)
    print_board(start)
    f = heuristic(start,goal)
    if f == g:
        print("Solved in {} moves".format(f))
        return

    solveEight(start,goal)


def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state and put -1 in place of the blank")
    for i in range(9):
        start.append(int(input()))

    print("Enter the goal state and put -1 in place of the blank")
    for i in range(9):
        goal.append(int(input()))
    print("start state is:")
    print_board(start)

    print("goal state is:")
    print_board(goal)
    print("\n")

    # To check if solvable
    if solvable(start):
        solveEight(start,goal)
        print("path cost is:{}".format(g))
    else:
        print("Not possible to solve")


if __name__ == '__main__':
    main()






'''g=0: Initializes a global variable g with a value of 0.

def print_board(elements):: Defines a function print_board that takes a list elements as input and prints it as a 3x3 board.

for i in range(9):: Loops through the range from 0 to 8 (9 elements).

if i%3 == 0:: Checks if the current index is divisible by 3. If true, it means a new row is starting, so a newline is printed.

print(): Prints a newline.

if elements[i]==-1:: Checks if the current element at index i is -1.

print("_", end = " "): If the element is -1, it prints an underscore (_) to represent an empty space on the board.

else:: If the element is not -1,

print(elements[i], end = " "): Prints the value of the element followed by a space.

print(): Prints a newline after each row.

def solvable(start):: Defines a function solvable that takes a list start as input and checks if the puzzle is solvable.

inv=0: Initializes a variable inv to 0 to keep track of the number of inversions.

for i in range(9):: Loops through the range from 0 to 8 (9 elements).

if start[i] <= 1:: Checks if the current element at index i is less than or equal to 1. If true, it skips to the next iteration.

continue: Skips to the next iteration of the loop.

for j in range(i+1,9):: Loops through the range from i+1 to 8.

if start[j]==-1:: Checks if the current element at index j is -1. If true, it skips to the next iteration.

if start[i]>start[j]:: Checks if the element at index i is greater than the element at index j. If true, it means there is an inversion.

inv+=1: Increments the inv variable by 1 for each inversion.

if inv%2==0:: Checks if the number of inversions is even.

return True: Returns True if the number of inversions is even, indicating that the puzzle is solvable.

return False: Returns False if the number of inversions is odd, indicating that the puzzle is not solvable.

def heuristic(start,goal):: Defines a function heuristic that calculates the heuristic value between the current state start and the goal state goal.

global g: Specifies that the variable g inside the function refers to the global variable g defined earlier.

h = 0: Initializes a variable h to 0 to store the heuristic value.

for i in range(9):: Loops through the range from 0 to 8 (9 elements).

for j in range(9):: Loops through the range from 0 to 8 (9 elements).

if start[i] == goal[j] and start[i] != -1:: Checks if the element at index i in the current state is equal to the element at index j in the goal state, and it is not an empty space (-1).

h += (abs(j-i))//3 + (abs(j-i))%3: Calculates the Manhattan distance between the positions of the elements in the current state and the goal state. The distance is divided by 3 and added to h.

return h + g: Returns the sum of the heuristic value h and the global variable g as the total cost.

def moveleft(start,position):: Defines a function moveleft that takes the current state start and the position of the empty space position as input, and moves the empty space one position to the left.

start[position],start[position-1]= start[position-1],start[position]: Swaps the element at the current position with the element at the position one step to the left.

def moveright(start,position):: Defines a function moveright that takes the current state start and the position of the empty space position as input, and moves the empty space one position to the right.

start[position],start[position+1]= start[position+1],start[position]: Swaps the element at the current position with the element at the position one step to the right.

def moveup(start,position):: Defines a function moveup that takes the current state start and the position of the empty space position as input, and moves the empty space one position up.

start[position],start[position-3]= start[position-3],start[position]: Swaps the element at the current position with the element at the position three steps up.

def movedown(start,position):: Defines a function movedown that takes the current state start and the position of the empty space position as input, and moves the empty space one position down.

start[position],start[position+3]= start[position+3],start[position]: Swaps the element at the current position with the element at the position three steps down.

def movetile(start,goal):: Defines a function movetile that takes the current state start and the goal state goal as input, and moves the empty space to the neighboring position that leads to the minimum heuristic value.

emptyat= start.index(-1): Finds the position of the empty space (-1) in the current state.

row = emptyat//3: Calculates the row index of the empty space by integer division by 3.

col = emptyat%3: Calculates the column index of the empty space by modulo operation with 3.

t1,t2,t3,t4 = start[:],start[:],start[:],start[:]: Creates copies of the current state start using the slice notation [:].

f1,f2,f3,f4 = 100,100,100,100: Initializes variables f1, f2, f3, f4 to 100 as placeholders for heuristic values.

if col -1 >=0:: Checks if moving the empty space to the left is a valid move (within the bounds of the board).

moveleft(t1, emptyat): Moves the empty space to the left in a copy of the current state t1.

f1 = heuristic(t1, goal): Calculates the heuristic value between the modified state t1 and the goal state goal and assigns it to f1.

if col+1<3:: Checks if moving the empty space to the right is a valid move (within the bounds of the board).

moveright(t2, emptyat): Moves the empty space to the right in a copy of the current state t2.

f2 = heuristic(t2, goal): Calculates the heuristic value between the modified state t2 and the goal state goal and assigns it to f2.

if row + 1 <3:: Checks if moving the empty space down is a valid move (within the bounds of the board).

movedown(t3, emptyat): Moves the empty space down in a copy of the current state t3.

f3 = heuristic(t3, goal): Calculates the heuristic value between the modified state t3 and the goal state goal and assigns it to f3.

if row-1>=0:: Checks if moving the empty space up is a valid move (within the bounds of the board).

moveup(t4, emptyat): Moves the empty space up in a copy of the current state t4.

f4 = heuristic(t4, goal): Calculates the heuristic value between the modified state t4 and the goal state goal and assigns it to f4.

min_heuristic = min(f1, f2,f3,f4): Finds the minimum heuristic value among f1, f2, f3, and f4.

if f1==min_heuristic:: Checks if f1 is equal to the minimum heuristic value.

moveleft(start, emptyat): Moves the empty space to the left in the current state start.

print("move tile to left"): Prints a message indicating that the tile is moved to the left.

elif f2==min_heuristic:: Checks if f2 is equal to the minimum heuristic value.

moveright(start, emptyat): Moves the empty space to the right in the current state start.

print("move tile to right"): Prints a message indicating that the tile is moved to the right.

elif f3==min_heuristic:: Checks if f3 is equal to the minimum heuristic value.

movedown(start, emptyat): Moves the empty space down in the current state start.

print("move tile down"): Prints a message indicating that the tile is moved down.

elif f4 == min_heuristic:: Checks if f4 is equal to the minimum heuristic value.

moveup(start, emptyat): Moves the empty space up in the current state start.

print("move tile up"): Prints a message indicating that the tile is moved up.

def solveEight(start,goal):: Defines a function solveEight that takes the current state start and the goal state goal as input, and recursively solves the puzzle by applying the A* search algorithm.

global g: Specifies that the variable g inside the function refers to the global variable g defined earlier.

g+=1: Increments the global variable g by 1, representing the cost of each move.

movetile(start,goal): Calls the movetile function to move the empty space in the current state start towards the goal state goal.

print_board(start): Prints the current state start as a board.

f = heuristic(start,goal): Calculates the heuristic value between the current state start and the goal state goal and assigns it to f.

if f == g:: Checks if the heuristic value f is equal to the cost g. If true, it means the puzzle is solved.

print("Solved in {} moves".format(f)): Prints a message indicating that the puzzle is solved and displays the number of moves.

return: Exits the function.

solveEight(start,goal): Calls the solveEight function recursively with the current state start and the goal state goal.

def main():: Defines the main function that serves as the entry point of the program.

global g: Specifies that the variable g inside the function refers to the global variable g defined earlier.

start = list(): Initializes an empty list start to store the start state of the puzzle.

goal = list(): Initializes an empty list goal to store the goal state of the puzzle.

print("Enter the start state and put -1 in place of the blank"): Prompts the user to enter the start state of the puzzle, where they should input -1 to represent the blank space.

for i in range(9):: Loops through the range from 0 to 8 (9 elements).

start.append(int(input())): Reads an integer input from the user and appends it to the start list.

print("Enter the goal state and put -1 in place of the blank"): Prompts the user to enter the goal state of the puzzle, where they should input -1 to represent the blank space.

for i in range(9):: Loops through the range from 0 to 8 (9 elements).

goal.append(int(input())): Reads an integer input from the user and appends it to the goal list.

print("start state is:"): Prints a message indicating the start state.

print_board(start): Prints the start state as a board.

print("goal state is:"): Prints a message indicating the goal state.

print_board(goal): Prints the goal state as a board.

if solvable(start):: Checks if the start state is solvable.

solveEight(start,goal): Calls the solveEight function to solve the puzzle with the start state start and the goal state goal.

print("path cost is:{}".format(g)): Prints the path cost, which is the final value of the global variable g.

else:: If the start state is not solvable,

print("Not possible to solve"): Prints a message indicating that it is not possible to solve the puzzle.

if __name__ == '__main__':: Checks if the current script is being run directly.

main(): Calls the main function, which starts the execution of the program.'''

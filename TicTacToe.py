import random
positions = [" "," "," "," "," "," "," "," "," "]
occupied = []
def gameBoard():
    print("""
    {} | {} | {}
    ---------
    {} | {} | {}
    ---------
    {} | {} | {}
    """.format(positions[0],positions[1],positions[2],
               positions[3],positions[4],positions[5],
               positions[6],positions[7],positions[8],))

def user_fun(ch):
    pos = int(input("Enter position ...."))
    if pos in occupied:
        print("You can't move here..")
        user_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)
        
def cpu_fun(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        cpu_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)
def checkWinner():
    winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in winning_combinations:
        if positions[i[0]] == positions[i[1]] == positions[i[2]] != " ":
            return positions[i[0]]
    
def main():
    gameBoard()
    user_choice = input("Enter your choice either X or 0").upper()
    while user_choice not in ['X','0']:
        print("Invalid Input !")
        user_choice = input("Enter your choice either X or 0").upper()
    if user_choice == 'X':
        cpu_choice = '0'
    else:
        cpu_choice = 'X'
    
    print("user_choice is : ",user_choice)
    print("cpu_choice is : ",cpu_choice)
    count = 0
    winner = None
    while count < 5 and not winner:
        count += 1
        user_fun(user_choice)
        gameBoard()
        winner = checkWinner()
        if winner:
            print(f"{winner} congratulations ! you win ...")
            break
        if count == 5:
            print("It's draw !")
            break
        cpu_fun(cpu_choice)
        gameBoard()
        if winner:
            print(f"{winner} congratulations ! you win ...")
            break
main()

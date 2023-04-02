import os

def cleansreen()->None:
    os.system("clear" if os.name == "posix" else "cls")


def board(slot)->None:
    vertical_line = '  |  '
    horizontal_line = '__'
    for i in range(3):
        if i < 2:
            print(f"\t\t\t {slot[i*3]} {vertical_line} {slot[i*3+1]} {vertical_line} {slot[i*3+2]} ")
            print("\t\t\t"+horizontal_line*10+"\n")
        elif i == 2:
            print(f"\t\t\t {slot[i*3]} {vertical_line} {slot[i*3+1]} {vertical_line} {slot[i*3+2]} ")
    print("")

def validate(player):
        if player < 0 or player > 9:
            return False
        return True
        
def winCombination(p1_move,p2_move)->str:
    
    win = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,9],[2,5,8]]

    if len(p1_move) > 2:
        for i in win:
            if set(i).issubset(set(p1_move)):
                return "1"
    if len(p2_move) > 2:
        for i in win:
            if set(i).issubset(set(p2_move)):
                return "2"

def move(slot,won):

    cleansreen()
    print("Tic Tac Toe\n\n")
    if won == "1":
        board(slot)
        print(f"Player {int(won)} wins!")
        return 1
    if won == "2":
        board(slot)
        print(f"Player {int(won)} wins!")
        return 2
    board(slot)

def main()->None:
    cleansreen()
    print("Tic Tac Toe\n\n")
    slot = [" "," "," "," "," "," "," "," "," "]

    board(slot)
    p1_move,p2_move = [],[]
    checker = False
    max_move = 9
    while checker != True:
            if max_move > 0:

                while True:
                    player_1 = int(input("Player 1 move:"))
                    if slot[player_1-1] != " ":
                        print("Slot is taken.Enter again.")
                    else: break

                ifTrue = validate(player_1)
                if ifTrue:

                    max_move-=1
                    slot[player_1-1]="O"
                    p1_move.append(player_1)
                    winner = move(slot,won = winCombination(p1_move,p2_move))
                    if winner == 1:break

                if max_move != 0:

                    while True:
                        player_2 = int(input("Player 2 move:"))
                        if slot[player_2-1] != " ":
                            print("Slot is taken.Enter again.")
                        else: break

                    ifT = validate(player_2)
                    if ifT:
                        max_move-=1
                        slot[player_2-1]="X"
                        p2_move.append(player_2)
                        winner = move(slot,won = winCombination(p1_move,p2_move))
                        if winner == 2: break
            else:
                checker=True
                print("Draw")
                break

    again = input("\nPLAY AGAIN (y/n): ")
    if again =='y':main()
    else:cleansreen(),print("Thank you for playing")

if __name__=="__main__":
    main()
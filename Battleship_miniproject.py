import random
Rows = 5
PATTERN = [] # global variable
X=random.randint(1,Rows)
Y=random.randint(1,Rows)
#intialize the screen

def create_initial():
    for i in range(Rows):
        t_list=[]
        for j in range(Rows):
            t_list.append("0")

        PATTERN.append(t_list)

  
# marking a guess


'''
def create_pattern(a,b):
    for i in range(Rows):
       # t_list=[]
        for j in range(Rows):
            if i==0 and j==b:
                #t_list.append("X ")
                # PATTERN.append(t_list)
                PATTERN[i][j] = "X"
'''
# Here I Modified the code loop is not mandatory
# So Iam directly Written


def create_pattern(a,b):
    PATTERN[a][b] = "X"

def  display_pattern():
    for i in range(Rows):
        for j in range(Rows):
            print(PATTERN[i][j], end=" ")
        print()
    
   # print(f"[HINT: Battleship is at position ({X},{Y})]")

if __name__=="__main__":
   create_initial()
   display_pattern()
   print("The Battleship is at index:",X-1,Y-1)
   # user to enter guess number 
   for count in range(Rows):
        guess_row = int(input("Guess the Row Position of the battleship:"))
        guess_col = int(input("Guess the Column Position of the battleship: "))

        if guess_row==X and guess_col==Y:
            print("Congratulations! you have destroyed the enemy,s battleship")
            
            break
        else:
            if count==Rows-1:
                print("your guess isnt good enough ....Enemy has reached your post and detroyed it. You lose!")
                break

            if guess_row<1 or guess_col<1:
                print("where are you targetting?? Invalid rows and columns.. Enemy is one step closer to you  post ")
            elif guess_row>Rows or guess_col>Rows:
                print("Why are you in the ocean?? Invalid rows and column.. Enemy is one step closer to your post ")
            else:
                print("That was a close shot bot not good enough.. Enemy is one step closer to your post")
            
            create_pattern(guess_row-1, guess_col-1)
            display_pattern()
            print("\n")




    

        
         




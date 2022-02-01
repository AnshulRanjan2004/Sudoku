import random as r
from art import logo
from data import complete
from data import incomplete

print(logo)

game = input("Do you want to play(y/n)").lower()
while game != "y" and game != "n":
  game = input("Please enter 'y' or 'n' only")

while game != 'n':
    c = r.randint(0, 4)
    solved = complete[c]
    unsolved = incomplete[c]

    def prinx(L):
        print("*****************************************")
        k = 0
        for i in L:
            k += 1
            print('||', end=' ')

            s = 0
            for j in i:
                s += 1

                if s % 3 == 0:
                    print(j, end=' ')
                    print("||", end=' ')
                else:
                    print(j, '|', end=' ')
            print()
            if k % 3 == 0:
                print("*****************************************")
            else:
                print("-----------------------------------------")

    prinx(unsolved)

    while solved != unsolved:

      x=[str(i) for i in]
      a = input("Enter row number :")
      while a not in x:
        a = input("Enter a valid row number(1 to 9) :")          
      a = int(a)  
      b = input("Enter column number:")
      while b not in x:
        b = input("Enter a valid row number(1 to 9) :")
      b = int(b)
      c = input("Enter the number:")
      while c not in x:
        c = input("Enter a valid row number(1 to 9) :")
      c = int(c)
      if unsolved[a - 1][b - 1] == "_":
        unsolved[a - 1][b - 1] = c
      else:
        print("You can't change that")

      if solved[a - 1][b - 1] != unsolved[a - 1][b - 1]:
        print("Wrong number !!!!!RETRY")
        unsolved[a - 1][b - 1] = "_"
        prinx(unsolved)
      else:
        prinx(unsolved)
    print("mad u solved it")
    game = input("Do you want to play(y/n)").lower()
    while game != "y" and game != "n":
      game = input("Please enter 'y' or 'n' only")

print("Thanks for joining us")

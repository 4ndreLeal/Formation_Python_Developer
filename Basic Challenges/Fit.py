N = int(input())

while(N > 0):
    A, B = input().split() 
    if len(A) >= len(B):
        if B == A[(len(A) - len(B)):]:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
    N -= 1

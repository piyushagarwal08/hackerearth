W1 = sorted(list(range(1,98,12))+ list(range(12,109,12)))
W1.append('WS')
M1= sorted(list(range(2,99,12)) + list(range(11,108,12)))
M1.append('MS')
A1 = sorted(list(range(3,100,12)) + list(range(10,107,12)))
A1.append('AS')
A2 = sorted(list(range(4,101,12)) + list(range(9,106,12)))
A2.append('AS')
M2 = sorted(list(range(5,102,12)) + list(range(8,105,12)))
M2.append('MS')
W2 = sorted(list(range(6,103,12)) + list(range(7,104,12)))
W2.append('WS')
seat = [W1,W2,A1,A2,M1,M2]
 
T = int(input())
for j in range(0,T):
    N = int(input())
    for i in seat:
        if N in i:
            if i.index(N)%2 == 0:
                print(i[i.index(N)+1],i[-1])
            else:
                print(i[i.index(N)-1],i[-1])

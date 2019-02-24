L = int(input())
N = int(input())
for test in range(0,N):
    width,height = map(int,input().split())

    if width < L or height<L:
        print("UPLOAD ANOTHER")
    elif (width>= L and height>= L):
        if(width == height):
            print("ACCEPTED")
        else:
            print("CROP IT")

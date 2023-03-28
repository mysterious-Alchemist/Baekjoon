while True:
    try:
        x, y = map(float, input().split())
        if x*y == 0:
            print("AXIS")
        elif x*y>0:
            if x>0:
                print("Q1")
            else:
                print("Q3")
        else:
            if x>0:
                print("Q4")
            else:
                print("Q2")
    except:
        break
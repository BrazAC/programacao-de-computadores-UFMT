import random

def main():
    grandeza = 4
    mtz = [[0]*grandeza for _ in range(grandeza)]

    for l in range(grandeza): 
        for c in range(grandeza):
            val = random.randrange(1, 11)
            mtz[l][c] = val
            print(l, c, val)
    
    print(mtz)

if __name__ == "__main__":
    main()
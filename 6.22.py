def main():
    a1 = int(input())
    b1 = int(input())
    c1 = int(input())

    a2 = int(input())
    b2 = int(input())
    c2 = int(input())
    s_f = False
    for n in range(-10, 11):
        for b in range(-10, 11):
            if a1 * n + b1 * b == c1 and a2 * n + b2 * b == c2:
                print(n, b)
                s_f = True
    if not s_f:
        print("No solution")
if __name__ == '__main__':
    main()
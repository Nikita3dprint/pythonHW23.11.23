for n in range(200, 1, -1):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[len(b) - 3] + b[len(b) - 2] + b[len(b) - 1]
    else:
        b += bin((n % 3) * 3)[2:]
    r = int(b, 2)
    if r < 100:
        print(n)
        break
        
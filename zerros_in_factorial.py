def zeros(n):
    a = 0
    while n != 0:
        n = n // 5
        a += n
    return a


if __name__ == "__main__":
    print(zeros(25))

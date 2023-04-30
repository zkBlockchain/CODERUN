def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def is_prime(n):
    if n == 1:
        return False

    d = 2
    while d * d <= n:
        if (n % d == 0):
            return False
        d += 1
    return True


def main():
    A, B = (int(x) for x in input().split())

    if A == 0 or B == 0 or A > B or B % A != 0:
        print(0)
        return
    elif A == B:
        print(1)
        return

    is_B_prime = is_prime(B)
    if A == 1 and is_B_prime:
        print(2)
        return
    elif is_B_prime:
        print(0)
        return

    B //= A
    pk_amounts = 0

    i = 1
    while i * i <= B:
        if B % i == 0:
            if gcd(i, B // i) == 1:
                pk_amounts += 1 + (i * i != B)
        i += 1

    print(pk_amounts)


if __name__ == '__main__':
    main()



def primeSubarrays(A, n):
    max_val = 10 ** 7

    prime = [True] * (max_val + 1)

    prime[0] = False
    prime[1] = False
    for p in range(2, int(max_val ** (0.5)) + 1):

        if prime[p] == True:

            for i in range(2 * p, max_val + 1, p):
                prime[i] = False

    cnt = 0

    for i in range(0, n - 1):
        valarr = [A[i]]
        for j in range(i + 1, n):
            valarr.append(A[j])

            if prime[sum(valarr)] == True:
                print(valarr)
                cnt += 1

    return cnt


if __name__ == "__main__":
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    n = len(A)

    print(primeSubarrays(A, n))

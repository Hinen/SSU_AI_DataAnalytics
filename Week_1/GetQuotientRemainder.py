
n1 = int(input("값 1을 입력하세요 : "))
n2 = int(input("값 2을 입력하세요 : "))

def getQuotientRemainder(a, b):
    return a // b, a % b

Q, R = getQuotientRemainder(n1, n2)
print("몫 : %d, 나머지 : %d" % (Q, R))

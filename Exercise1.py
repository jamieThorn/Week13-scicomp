from math import pi
def leibniz(N):
    pi_N = 0
    for n in range(N):
        nth = 8/((4*n+1)*(4*n+3))
        pi_N += nth    
    return pi_N
def error(pi_N):
    e = abs(pi-pi_N)
    return e
def test():
    n = 10000
    while error(leibniz(n)) > 10**(-7):
        n+=1
    return n
def main():
    pi_100 = leibniz(100)
    pi_1000 = leibniz(1000)
    pi_10000 = leibniz(10000)
    print(error(pi_100))
    print(error(pi_1000))
    print(error(pi_10000))
    nth = test()
    print(nth)
main()
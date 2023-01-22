def leibniz(N):
    pi_N = 0
    for n in range(N):
        nth = 8/((4*n+1)*(4*n+3))
        pi_N += nth    
    return pi_N

def main():
    print(leibniz(1000))
main()
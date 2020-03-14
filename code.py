import numpy as np
import math as m
import matplotlib.pyplot as plt
import sys 

## calculate theory matrix
def cal_theory(N):
    P_theory = np.zeros((N))
    for i in range(N):
        P_theory[i] = m.exp(-(q-p)*((1-p**2/q**2)*(p**2/q**2)**k)*i)
    return P_theory


## Monte Carlo
def cal_simulation(p, q, N, k):
    P = np.zeros((N))
    row_car = np.zeros((N))

    for i in range(10000):
        num_car = 0
        for j in range(N):
            if (np.random.uniform(0,1) < p) : ## car come in
                num_car = num_car + 1
            if (np.random.uniform(0,1) < q and num_car > 0): ## car come out
                num_car = num_car - 1
            row_car[j] = num_car
            r = row_car[0:j]
            element = r[np.where(r<k)]
            if element.shape[0] == j:
                P[j] = P[j] + 1
    P = P/10000
    return P

def main(p, q, N, k):
    P_theory = cal_theory(N)
    P = cal_simulation(p, q, N, k)
    figname = 'p=%f k=%d' % (p, k) + '.png'
    plt.plot(np.arange(N), P[0:N], label='simulation')
    plt.plot(np.arange(N), P_theory[0:N], label='theory')
    plt.ylabel('P(Mn<k)')
    plt.xlabel('t')
    plt.legend(loc='upper right')
    plt.savefig(figname)
    plt.show()

if __name__ == '__main__':
    p = sys.argv[1]
    k = sys.argv[2]
    
    p = 0.4; 
    q = 1-p; 
    N = 1000; 
    k = 5; 
    main(p, q, N, k)


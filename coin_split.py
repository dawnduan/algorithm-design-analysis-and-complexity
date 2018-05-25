# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:51:42 2018

@author: Dawn.Duan
"""
from math import inf

coins = [9,2,5,7,4,8,11]
coins = sorted(coins, reverse = True)

V = 20
q = [inf for i in range(V)]
#assume coins are sorted descendingly
def find_optimum(coins, k, q):
    ind_k = k - 1
    if k in coins: 
        #print('found in coins')
        q[ind_k] = 1
        return q[ind_k]
    if k < coins[-1]: 
        #print('non compatible')
        q[ind_k] = inf
        return q[ind_k]
    if q[ind_k] < inf:
        #print('haha, i memorize it! ', k)
        return q[ind_k]
    else:
        pivot = binary_search(k, coins)  # log(n)
        candidate = coins[pivot:]
        print(candidates)
        temp = inf
        for c in candidates: # n
            print('start with ', k, 'choose coin', c)
            candidates.remove(c)
            temp = min(temp, 1+ find_optimum(coins, k-c, q))
        q[ind_k] = temp
        return q[ind_k]
        
print(find_optimum(coins, V, q))

def binary_search(k, coins):
    pass

def fetch_coins(q, coins, V):
    ind = V - 1
    ans = q[ind]
    soln = []
    while ans > 0:
        for c in coins:
            if c < V and q[c-1] == ans:
                soln.append(c)
                V = c
                ans -= 1
    return soln
                
                
        
    
    
    
'''
proof: 
'''

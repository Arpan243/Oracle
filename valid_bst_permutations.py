import math

MOD = 1000000007
MOD_10_8 = int(math.pow(10, 8) + 7)
memoization = {}

def total_number_BST(num_nodes):
    if num_nodes in memoization:
        return memoization[num_nodes]
    
    if num_nodes == 0 or num_nodes == 1:
        return 1
    
    combinations = 0
    for j in range(1, num_nodes + 1):
        combinations = (combinations + (total_number_BST(j - 1) * total_number_BST(num_nodes - j)) % MOD_10_8) % MOD_10_8
    
    memoization[num_nodes] = combinations
    return combinations

def main():
    number=100
    print(total_number_BST(number))

if __name__ == '__main__':
    main()

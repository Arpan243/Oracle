def calc(base, times):
    return base * (1 << (times - 1))

def main():
    n, k = map(int, input().split())
    discounts = list(map(int, input().split()))
    
    times = [1] * n  # Initially, each discount is applied once
    
    # Perform 'k' adjustments to maximize the discount
    for _ in range(k):
        max_increase = -1
        max_index = -1
        
        for j in range(n):
            curr = calc(discounts[j], times[j])
            next_val = calc(discounts[j], times[j] + 1)
            
            if next_val - curr > max_increase:
                max_increase = next_val - curr
                max_index = j
        
        times[max_index] += 1
    
    # Calculate the final maximum discount using bitwise OR
    max_discount = 0
    for i in range(n):
        max_discount |= calc(discounts[i], times[i])
    
    print(max_discount)

if __name__ == "__main__":
    main()

def find_parent(i, parent):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent[i], parent)  # Path compression
    return parent[i]

def solve(queries, s1, s2, n, m):
    result = []
    parent = list(range(m + 1))  # Initialize parent pointers
    size = [1] * (m + 1)         # Initialize size array

    for i in range(n):
        if queries[i] == "Friend":
            x = find_parent(s1[i], parent)
            y = find_parent(s2[i], parent)
            if x != y:
                # Union by size
                parent[y] = x
                size[x] += size[y]
        else:
            # Output the sum of the sizes of the sets that s1[i] and s2[i] belong to
            result.append(size[find_parent(s1[i], parent)] + size[find_parent(s2[i], parent)])
    
    return result

def main():
    m = 4 # Read number of students
    n = 3 # Read number of queries
    queries = ["Friend","Friend","Total"]  # Read all queries
    s1 = [1,2,1]  # Read first set of students
    s2 = [2,3,4]  # Read second set of students

    result = solve(queries, s1, s2, n, m)
    print(" ".join(map(str, result)))
    
    m = 3 # Read number of students
    n = 2 # Read number of queries
    queries = ["Friend","Total"]  # Read all queries
    s1 = [1,2]  # Read first set of students
    s2 = [2,3]  # Read second set of students

    result = solve(queries, s1, s2, n, m)
    print(" ".join(map(str, result)))  #3 Output the result


    m = 2 # Read number of students
    n = 1 # Read number of queries
    queries = ["Total"]  # Read all queries
    s1 = [1]  # Read first set of students
    s2 = [2]  # Read second set of students

    result = solve(queries, s1, s2, n, m)
    print(" ".join(map(str, result))) #2

    
if __name__ == "__main__":
    main()

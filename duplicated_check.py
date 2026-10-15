def has_duplicates(a):
    for i in range(len(a)):        # outer loop
        for j in range(i):         # inner loop
            if a[i] == a[j]:
                return True
    return False
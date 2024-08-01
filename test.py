test_cases = int(input())

for _ in range(test_cases):
    ln = int(input())
    arr = [int(x) for x in input().split()]
    ref = arr[0]
    diff_arr = []
    cnt = 0
    prev_el = 0

    for i in range(ln):
        if arr[i] < ref:
            diff_arr.append(ref - arr[i])
        else:
            ref = arr[i]
    
    diff_arr.sort()
    diff_arr_len = len(diff_arr)
    
    for k in range(len(diff_arr)):
        cnt += (diff_arr[k] - prev_el)*(diff_arr_len + 1)
        diff_arr_len -= 1
        prev_el = diff_arr[k]

    print(cnt)

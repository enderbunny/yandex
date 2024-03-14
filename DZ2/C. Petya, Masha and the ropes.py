n = int(input())
ropes = list(map(int, input().split()))
max_rop = max(ropes)

ropes.remove(max_rop)

if sum(ropes) >= max_rop:
    print(sum(ropes) + max_rop)
else:
    print(max_rop - sum(ropes))

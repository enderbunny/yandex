n1 = int(input())
n1_list = set(map(int, input().split()))
n2 = int(input())
n2_list = set(map(int, input().split()))
n3 = int(input())
n3_list = set(map(int, input().split()))

k = list(n1_list & n2_list | n2_list & n3_list | n3_list & n1_list)

print(' '.join(map(str, sorted(k))))

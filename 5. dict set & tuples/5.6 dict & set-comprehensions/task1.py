n = input().split()
start = int(n[0])
n = n[1:]
print({count: k for count, k in enumerate(n, start=start)}[4])
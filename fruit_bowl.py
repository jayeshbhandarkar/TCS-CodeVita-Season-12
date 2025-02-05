import math

def cal_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def cal_perimeter(pts):
    pts = sorted(pts)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    low = []
    for p in pts:
        while len(low) >= 2 and cross(low[-2], low[-1], p) <= 0:
            low.pop()
        low.append(p)

    perimeter = 0
    for i in range(len(low) - 1):
        perimeter += cal_distance(low[i], low[i + 1])

    return round(perimeter)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    pts = [tuple(map(int, line.split())) for line in data[1:n + 1]]

    res = cal_perimeter(pts)
    print(res, end="")

"""
座標平面上に相異なるN個の点があるので、そのうちから3点を選んで、角度の最大値を求める。
ここで求めるのは内積の絶対値が最も小さいものを選べば良い。
N^3はN<=2000なので間に合わない
各中央の点Nについて、残りの点をベクトルのtanに沿ってソートするとNlogNかかって、
一点Nを選ぶとそこから最も角度の遠いものはlogNかかる。
よってN^2logNで解ける。これは2000*2000*3log2=10^7スケールで、十分高速である。
"""
import math


def argsort(p, points):
    """
    pとpointsの中で、pとpointsの偏角の順にソートする。
    """
    res = []
    for i in range(len(points)):
        points[i] = (points[i][0] - p[0], points[i][1] - p[1])
        if points[i] != (0, 0):
            res.append(math.degrees(math.atan2(points[i][0], points[i][1])))
    return res


def binary_search_inner(source, target_array):
    """
    sourceに最も近い値を探し、値を返す。
    """
    less = -1
    more = len(target_array)
    while abs(more - less) > 1:
        mid = (more + less) // 2
        if target_array[mid] < source:
            less = mid
        else:
            more = mid
    res = 1e9
    if 0 <= less:
        if abs(res - source) > abs(target_array[less] - source):
            res = target_array[less]
    if more < len(target_array):
        if abs(res - source) > abs(target_array[more] - source):
            res = target_array[more]
    return res


def binary_search(source, target_array):
    """
    sourceから最も偏角が大きくなるようなtarget_arrayの要素を探す。
    この時、source+180に最も近いか、source-180に最も近い値であることがわかる。
    """
    plus = binary_search_inner(source + 180, target_array)
    plus = plus - source
    minus = binary_search_inner(source - 180, target_array)
    minus = source - minus
    res = max(plus, minus)
    return res


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
max_arg = 0

for p0 in points:
    argsorted = argsort(p0, points)
    for p1 in argsorted:
        max_arg = max(max_arg, binary_search(p1, argsorted))

print(max_arg)

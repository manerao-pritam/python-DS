import sys
from heapq import heappush, heappop, heapify

# sys.stdin = open("input", "r")
# sys.stdout = open("output", "w")


# add edge to mst
def update_mst(frm, to, cost, mst):
    if frm in mst:
        mst[frm].update({to: cost})
    else:
        mst[frm] = {to: cost}
        

# this is for prim's to start off with
def make_graph(edges):
    if not edges:
        return {}

    graph = {}

    # this is to make the edge bi-directional
    # i.e. a-b and b-a
    for edge in edges:
        for v in edge[:2]:
            if v in graph:
                continue
            graph[v] = {}

    for start, end, weight in edges:
        graph[start].update({end: weight})
        graph[end].update({start: weight})

    return graph


# prims
def mst_prims(graph, start):
    mst = {}
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapify(edges)

    while edges:
        cost, frm, to = heappop(edges)
        if to not in visited:
            visited.add(to)

            update_mst(frm, to, cost, mst)

            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heappush(edges, (cost, to, to_next))

    return mst


# kruskal needs union and find
# to detect cycle and to find the parent of
# current node
def union(arr, u, v):
    if arr[u] < arr[v]:
        arr[v] = u
    else:
        arr[u] = v


# find parent
def find(arr, u):
    tmp = u
    while arr[tmp] > 0:
        tmp = arr[tmp]

    return tmp


def mst_kruskals(edges):
    mst = {}

    heap = [(cost, frm, to) for frm, to, cost in edges]
    heapify(heap)
    # print(heap)

    parent = [0] * (len(heap) + 1)
    # ret = 0

    while heap:
        cost, frm, to = heappop(heap)

        pa, pb = find(parent, frm), find(parent, to)

        # if parents are not the same
        # then do union
        if pa != pb:
            # union and update parent list
            union(parent, pa, pb)
            # ret += cost
            update_mst(frm, to, cost, mst)

    # print(ret)
    return mst


def main():
    # grid = [
    #     [0, 25, 0, 0, 0, 5, 0],
    #     [25, 0, 12, 0, 0, 0, 10],
    #     [0, 12, 0, 8, 0, 0, 0],
    #     [0, 0, 8, 0, 16, 0, 14],
    #     [0, 0, 0, 16, 0, 20, 18],
    #     [5, 0, 0, 0, 20, 0, 0],
    #     [0, 10, 0, 14, 18, 0, 0]
    # ]

    # grid = [
    #     [0, 15, 25, 0, 0, 0, 0, 0, 0],
    #     [15, 0, 0, 10, 5, 25, 0, 0, 0],
    #     [25, 0, 0, 20, 0, 0, 10, 0, 0],
    #     [0, 10, 20, 0, 0, 0, 0, 10, 5],
    #     [0, 5, 0, 0, 0, 15, 0, 0, 0],
    #     [0, 25, 0, 0, 15, 0, 0, 0, 0],
    #     [0, 0, 10, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 10, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 5, 0, 0, 0, 0, 0]
    # ]

    # # with loops and parallel lines
    # grid = [
    #     [0, 7, 8, 0, 0, 0],
    #     [7, 0, 3, 6, 0, 0],
    #     [8, 3, 0, 4, 3, 0],
    #     [0, 6, 4, 0, 2, 5],
    #     [0, 0, 3, 2, 0, 2],
    #     [0, 0, 0, 5, 2, 0]
    # ]

    # {'a': 0, 'b': 1, 'c': 2, 'd': 6,
    #  'e': 3, 'f': 7, 'g': 8, 'h': 4, 'i': 5}

    # grid = [
    #     [0, 4, 0,]
    # ]

    # print('sum of mst:', mst_prims(grid, return_sum=True))
    # print('mst:', mst_prims(grid))
    edges = [
        ("a", "b", 7),
        ("a", "c", 8),
        ("b", "c", 3),
        ("b", "d", 6),
        ("c", "d", 4),
        ("c", "e", 3),
        ("d", "e", 2),
        ("d", "f", 5),
        ("e", "f", 2),
    ]

    edges = [
        (1, 2, 25),
        (1, 6, 5),
        (2, 3, 12),
        (2, 7, 10),
        (3, 4, 8),
        (4, 5, 16),
        (4, 7, 14),
        (5, 6, 20),
        (5, 7, 18),
    ]

    # prims
    print(mst_prims(make_graph(edges), start=1))

    # Kruskals
    print(mst_kruskals(edges))


if __name__ == "__main__":
    main()

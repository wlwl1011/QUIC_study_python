def searchGragh(g, a):
    qu = []
    done = set()

    qu.append(a)
    done.add(a)

    while qu:
        d = qu.pop(0)
        print(d)
        for x in g[d]:
            if x not in done:
                qu.append(x)
                done.add(x)


fr_info = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]

}
print(fr_info[1])
searchGragh(fr_info, 1)

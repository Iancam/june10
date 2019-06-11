
def grid(n, k, base="x"):
    return [[base]*k for _ in range(n)]


def pprintGrid(g):
    print("\n".join(["".join(a) for a in g]))

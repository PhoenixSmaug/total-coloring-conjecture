import sys
from pysms.qcir_graph_builder import *
from itertools import combinations

# encode that the graph has a total coloring with k colors
def total_coloring(builder, k):
    color = [[builder.id() for _ in range(k)] for _ in builder.V]
    edge_color = [[[builder.id() if u < v else None for c in range(k)] for v in builder.V] for u in builder.V]

    outputGate = AndGate(builder.id(), [])

    for v in builder.V:
        outputGate.appendToInput(OrGate(builder.id(), [color[v][i] for i in range(k)]))  # each vertex has at least one color

    for v, w in combinations(builder.V, 2):
        outputGate.appendToInput(OrGate(builder.id(), [edge_color[v][w][i] for i in range(k)]))  # each edge has at least one color

    for v, w in combinations(builder.V, 2):
        for i in range(k):
            outputGate.appendToInput(OrGate(builder.id(), [-builder.var_edge(v, w), -color[v][i], -color[w][i]]))  # adjacent vertices are not allowed to have the same color

    for v, w in combinations(builder.V, 2):
        for i in range(k):
            outputGate.appendToInput(OrGate(builder.id(), [-builder.var_edge(v, w), -color[v][i], -edge_color[v][w][i]]))  # edge and its endpoints are not allowed to have the same color

    for v, w1, w2 in combinations(builder.V, 3):
        for i in range(k):
            outputGate.appendToInput(OrGate(builder.id(), [-builder.var_edge(v, w1), -builder.var_edge(v, w2), -edge_color[v][w1][i], -edge_color[v][w2][i]]))  # adjacent edges are not allowed to have the same color

    return outputGate

# search for a counter example to the total coloring conjecture with n vetices and degree limit d
def search_counter(n, d):
    builder = GraphEncodingBuilder(n, directed=False)
    no_col = total_coloring(builder, d + 2)
    no_col = NegatedGate(no_col)

    builder.addUniversalGate(no_col)

    deg = builder.maxDegree(d)  # technically this only ensures that Delta <= d, but even if Delta < d not having a total coloring with d + 2 is sill a counter example to the conjecture

    builder.addExistentialGate(deg)

    builder.solve(allGraphs=True)

# search for a counter example to the total coloring conjecture with n vertices
def main(n):
    # start at 6, since the conjecture is proven for d <= 5 (https://doi.org/10.1016/0012-365X(95)00286-6)
    for i in range(6, n + 1):
        search_counter(n, i)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qbf.py <integer>")
        sys.exit(1)
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("Error: The argument must be an integer.")
        sys.exit(1)
    main(arg)

# (c) Mia Muessig

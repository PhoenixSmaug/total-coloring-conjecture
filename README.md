# Verification of the Total Coloring Conjecture for small graphs

One of the most famous open problem in Graph Theory is the Total Coloring Conjecture. For a total coloring we color all vertices and edges of a graph, such that no adjacent vertices, no adjacent edges and no edge and one of its endpoints have the same color. The conjecture claims that any graph $G$ has a total coloring using $\Delta(G) + 2$ differen colors, where $\Delta(G)$ is the maximum degree of a vertex in $G$. Despite being more than 60 years old, it has only been proven in some restricted cases, for example in [(Kostochka, 1996)](https://doi.org/10.1016/0012-365X(95)00286-6) for graphs with $\Delta(G) \leq 5$.

Recently Markus Kirchweger, Tomáš Peitl and Stefan Szeider sucessfully used their [SAT Modulo Symmetry solver](https://sat-modulo-symmetries.readthedocs.io) to disprove the existence of small counter-examples for similar conjectures as [this publication list](https://sat-modulo-symmetries.readthedocs.io/en/latest/publications/) demonstrates. As described [here](https://doi.org/10.24963/ijcai.2023/216 (Paper explaining co-certificates)), the solver uses co-certificates to efficiently deal with coNP complete constraints. This allows the easy encoding of properties like being an unsatisfiable SAT instance or not having a total coloring with $k$ colors, which unless $NP = coNP$ would require exponentially many constraints. While this could also be done using general QBF solvers like [caqe](https://github.com/ltentrup/caqe), their SAT Modulo Symmetry solver drastically outperforms state of the art QBF solvers in its domain of problems.



(c) Mia Müßig

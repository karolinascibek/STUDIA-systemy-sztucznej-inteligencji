from blok1.lab1.decision_system import DecisionSystem
from blok1.lab2.graph_smiley import GraphSmiley


system = DecisionSystem()

# -- lab2 --

# graph = GraphSmiley()
# graph.display(0, 0, 16)

# wykresy

system.load_samples("lab2/iris.txt", "\t")
system.load_headers("lab2/iris-type.txt", '\t')
system.show()
# system.display()







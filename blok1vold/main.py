from blok1.lab1.decision_system import DecisionSystem
system = DecisionSystem()
# system.load_samples("lab1/wartosci.txt", " ")
# system.load_headers("lab1/atrybuty.txt", " ")
# system.display()

# system.view_the_graph_smial(0, 0, 16)
system.load_samples("lab2/iris.txt", "\t")
system.load_headers("lab2/iris-type.txt", '\t')
system.show()
# system.display()
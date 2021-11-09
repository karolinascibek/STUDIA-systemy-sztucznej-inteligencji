from blok1.lab1.decision_system import DecisionSystem
from blok1.lab3.k_means import KMeans


system = DecisionSystem()

# -- lab1 --

# system.load_samples("lab1/wartosci.txt")
# system.load_headers("lab1/atrybuty.txt")
# system.display()


# -- lab2 --
# system.view_the_graph_smial(0, 0, 16)
# system.load_samples("lab2/iris.txt", "\t")
# system.load_headers("lab2/iris-type.txt", '\t')
# # system.show()
# system.display()


# -- lab3 --
system.load_samples("lab3/spirala.txt", "   ")
system.load_headers("lab3/spirala-type.txt", ',')

# system.display()

# -- lab3.1 --
# samples = system.get_samples()
# samples_cov_to_number = system.samples_str_to_number(samples)
# print(samples_cov_to_number)

# -- lab3.2 --
samples = system.get_samples()
samples_cov_to_number = system.samples_str_to_number(samples)
alg = KMeans(samples_cov_to_number)
alg.k_means(iterations=11, m=4)

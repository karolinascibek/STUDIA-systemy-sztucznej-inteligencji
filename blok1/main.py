from blok1.lab1.decision_system import DecisionSystem
from blok1.lab3.k_means import KMeans
from  blok1.lab4.one_plus_one import OnePlusOne
from  blok1.lab4.mu_plus_lambda import MuPlusLambda
from blok1.lab3.c_means import CMeans
from blok1.lab2.graph_smiley import GraphSmiley


system = DecisionSystem()

# -- lab1 --

# system.load_samples("lab1/wartosci.txt")
# system.load_headers("lab1/atrybuty.txt")
#
# system.display()


# -- lab2 --
# graph = GraphSmiley()
# graph.display(0, 0, 16)
# system.load_samples("lab2/iris.txt", "\t")
# system.load_headers("lab2/iris-type.txt", '\t')
# system.show()
# system.display()


# -- lab3 --
system.load_samples("lab3/spirala.txt", "   ")
system.load_headers("lab3/spirala-type.txt", ',')

# system.display()

# -- lab3.1 --
samples = system.get_samples()
samples_cov_to_number = system.samples_str_to_number(samples)
# print(samples_cov_to_number)

# -- lab3.2 --
samples = system.get_samples()
samples_cov_to_number = system.samples_str_to_number(samples)

# alg = KMeans(samples_cov_to_number)
# alg.k_means(iterations=11, m=4)

# fcm = CMeans(samples_cov_to_number)
# fcm.c_means(3, iterations=20)

# -- lab 4.1 --
# opo = OnePlusOne()
# opo.one_plus_one()

# -- lab 4.2 --
# mpl = MuPlusLambda()
# mpl.mu_plus_lambda()




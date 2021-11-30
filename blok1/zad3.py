from blok1.lab1.decision_system import DecisionSystem
from blok1.lab3.k_means import KMeans
from blok1.lab3.c_means import CMeans


system = DecisionSystem()

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

alg = KMeans(samples_cov_to_number)
alg.k_means(iterations=10, m=2)

# fcm = CMeans(samples_cov_to_number)
# fcm.c_means(3, iterations=30)





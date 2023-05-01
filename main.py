import cec2017.functions as functions
from pygmo import *
import numpy as np
import time
from cec_prob import CECProb


problems = [CECProb(10, 9)]
results_str = ""

#itera os índices dos problemas
for p in range(3, 5):
    start = time.time()
    print(f"Problem: {p}. D:", end="")

    #itera as dimensões possíveis: 2 e 10
    for d in [2, 10]:
        print(f" {d} [", end="")

        #número de repetições de cada experimento: 51
        for i in range(5):
            algo = algorithm(de(gen=500*d, F=0.8, CR=0.9, variant=2, ftol=1e-20, xtol=1e-20))
            algo.set_verbosity(0)
            prob = problem(CECProb(d, p))
            pop = population(prob, 20)
            pop = algo.evolve(pop)
            uda = algo.extract(de)
            results_str = results_str +"\n"+ f"{p}\t{d}\t{pop.champion_f[0]}"
            print(f"|", end="")

        print("]", end="")

    print("\n", end="")
    end = time.time()
    print(f"Time elapsed: {end - start}")
        #print([x[2] for x in uda.get_log()])



results_str = results_str + "\n"
print(results_str)

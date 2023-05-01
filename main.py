import cec2017.functions as functions
from pygmo import *
import numpy as np
import time
from cec_prob import CECProb


def main():
    problems = [CECProb(10, 9)]
    results_str = ""
    pop_size = 20
    exec_num = 51
    budget = int(10000 / pop_size)

    #itera os índices dos problemas
    for p in range(6, 9+1):
        start = time.time()
        print(f"Problem: {p}. D:", end="", flush=True)

        #itera as dimensões possíveis: 2 e 10
        for d in [2, 10]:
            print(f" {d} [", end="", flush=True)

            #número de repetições de cada experimento: 51
            for i in range(exec_num):
                algo = algorithm(de(gen=budget*d, F=0.8, CR=0.9, variant=2, ftol=1e-06, xtol=1e-06))
                #todo: verificar por que colocar a mesma seed não está gerando o mesmo resultado
                # para o mesmo problema
                algo.set_seed(0)
                algo.set_verbosity(0)
                prob = problem(CECProb(d, p))
                pop = population(prob, pop_size)
                pop = algo.evolve(pop)
                uda = algo.extract(de)
                results_str = results_str + f"{p}\t{d}\t{pop.champion_f[0]}\n"
                print("|", end="", flush=True)

            print("]", end="", flush=True)

        print("\n")
        end = time.time()
        print(f"Time elapsed: {end - start}")
            #print([x[2] for x in uda.get_log()])

    with open("result.csv", mode="w") as file:
        file.write(results_str)

    print(results_str)


if __name__=="__main__":
    main()
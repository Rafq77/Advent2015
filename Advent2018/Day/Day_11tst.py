def sq(x):
    print(x)
    return x**4

import multiprocessing as mp



#   for result in pool.imap_unordered(delayed(testtm), powerset(all_turns),
                                     #chunksize=1000):


if __name__ == "__main__":
    
    pool = mp.Pool(processes=4)
    z = pool.map(sq,range(10))

import multiprocessing

def cpu_stress():
    while True:
        sum(i for i in range(1000000))

if __name__ == "__main__":
    for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=cpu_stress).start()




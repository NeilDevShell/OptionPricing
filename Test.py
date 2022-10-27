from Pricer import Pricer
from option import AmericanPutOption
import statistics

if __name__ == "__main__":
    option = AmericanPutOption(1, 1)
    pricer = Pricer(1, 0.01, rate=0.06, vol=0.2, path_size=10000)
    res = [pricer(option) for _ in range(10)]

    print(statistics.variance(res), statistics.mean(res))

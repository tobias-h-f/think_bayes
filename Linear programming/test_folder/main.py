import pandas as pd
import numpy as np


def main():
    print("Hello World!")
    df = pd.DataFrame(np.random.randn(10, 5))
    print(df)
    return df 


if __name__ == "__main__":
    main()
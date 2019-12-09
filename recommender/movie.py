import pandas as pd
import numpy as np
import os


def build_chart(genre):
    dataset = "./final_version.csv"
    dataset = os.path.join(os.path.abspath(os.path.dirname(__file__)), dataset)
    df = pd.read_csv(dataset, index_col=0)
    gen_movie = df[df['genre'] == 'Crime']
    return gen_movie.reindex(np.random.permutation(gen_movie.index)).head(24)




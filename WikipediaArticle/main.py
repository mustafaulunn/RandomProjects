from datetime import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import os
import random
import matplotlib
import matplotlib.pyplot as plt
import xgboost as xgboost
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_errorimport

xgboost as xgb
from surprise import Reader, Dataset
from surprise import BaselineOnly
from surprise import KNNBaseline
from surprise import SVD
from surprise import SVDpp
from surprise.model_selection import GridSearchCVdef

load_data():
netflix_csv_file = open("netflix_rating.csv", mode="w")
rating_files = ['combined_data_1.txt']
for file in rating_files:
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line.endswith(":"):
                movie_id = line.replace(":", "")
            else:
                row_data = []
                row_data = [item for item in line.split(",")]
                row_data.insert(0, movie_id)
                netflix_csv_file.write(",".join(row_data))
                netflix_csv_file.write('\n')

netflix_csv_file.close()
df = pd.read_csv('netflix_rating.csv', sep=",", names=["movie_id", "customer_id", "rating", "date"])
return dfnetflix_rating_df = load_data()
netflix_rating_df.head()


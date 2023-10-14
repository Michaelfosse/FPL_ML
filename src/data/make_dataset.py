import pandas as pd  # Import pandas library
from pathlib import Path
import os

#To change wd in Jupyter notebook
cwd = os.getcwd()
os.chdir(cwd)

#Load files
all_old_fixtures = pd.read_csv("../../data/raw/all_old_fixtures.csv", sep=";")
all_upcoming_fixtures = pd.read_csv("../../data/raw/all_upcoming_fixtures.csv")
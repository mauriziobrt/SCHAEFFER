from datasets import load_dataset
import numpy as np
import json
import pandas as pd
import os


directory = '*'

dataset = load_dataset("audiofolder", data_dir = directory)

print(dataset["train"][0])

dataset.push_to_hub("dbschaeffer/SCHAEFFER")
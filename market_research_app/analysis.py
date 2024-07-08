import pandas as pd
import numpy as np

def analyze_data(data):
    df = pd.DataFrame(data)
    # Perform analysis
    summary = df.describe()
    return summary

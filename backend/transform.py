import pandas as pd
import numpy as np

def transform_data(file):
    # Load file (assuming it's a CSV)
    data = pd.read_csv(file)
    
    # Example: Transforming data into vectors (this can be customized)
    transformed_data = data.apply(np.vectorize(str), axis=1)  # Placeholder transformation

    return transformed_data.to_dict(orient='records')

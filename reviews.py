import os
import pandas as pd

# Check if the file exists
data_path = 'data/winemag-data-130k-v2.csv.zip'
if not os.path.exists(data_path):
    print(f"File not found: {data_path}")
else:
    # Load the dataset
    df = pd.read_csv(data_path)

    # Summarize the data by country
    summary = df.groupby('country').agg(
        count=('country', 'size'),
        points=('points', 'mean')
    ).reset_index()

    # Save the summary to a new CSV file
    output_path = 'data/reviews-per-country.csv'
    summary.to_csv(output_path, index=False)

    print("Summary has been written to 'reviews-per-country.csv'")
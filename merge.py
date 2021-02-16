import pandas as pd
import glob
import os

extension = 'csv'
allFiles = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined = pd.concat([pd.read_csv(f) for f in allFiles])
# export
combined.to_csv("skiply.csv", index=False)

for file in allFiles:
    os.remove(file)

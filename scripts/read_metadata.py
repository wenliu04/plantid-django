import pandas as pd


df = pd.read_csv("data/metadata.csv", sep=';',usecols=['species_id', 'species'])
df = df.drop_duplicates().sort_values("species_id").reset_index(drop=True)
label2info = {
    i: (row["species_id"], row["species"])
    for i, row in df.iterrows()
}

label = 1517
species_id, latin_name = label2info[label]
print("预测结果：")
print("  Label:", label)
print("  Species ID:", species_id)
print("  Latin Name:", latin_name)

import pandas as pd
import matplotlib.pyplot as plt
import unicodedata 

# Read the CSV file
df = pd.read_csv("keystrokes.csv")

# Sort descending by count
df = df.sort_values("count", ascending=False)

def read_key_map(filename):
    keys = [r.strip() for r in open(filename, 'r')]
    return dict(zip(range(len(keys)), keys))

key_map = read_key_map("formatted-keycodes.txt")

def convert(key):
    c = chr(key)
    if not c.isprintable():
        c = key_map.get(key, "ukn")
    elif c.isspace():
        c = 'Space'
    return c 


# (Optional) Pick top N keys
print(df.shape[0])
df["char"] = df["key"].apply(lambda k : convert(k))
top_n = min(20, df.shape[0])
print(df[df["count"] > 0])
print(df.head(top_n))
# print(df["char"].value_counts())
df = df.head(top_n)
df = df.reset_index(drop=True)
print(df.shape)
print(df)

# Plot
plt.figure(figsize=(8, 12))
# plt.barh(df["key"], df["count"], color='skyblue')
plt.barh(df["char"], df["count"], color='skyblue', align='center') #, width=0.5)
plt.xlabel("Press Count")
plt.title(f"Top {top_n} Most Pressed Keys")
plt.gca().invert_yaxis()  # Most-used at top
plt.tight_layout()

# Save or display
# plt.savefig("keystats_plot.png", dpi=200)
plt.show()

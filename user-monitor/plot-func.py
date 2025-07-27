import pandas as pd
import matplotlib.pyplot as plt
import unicodedata 

# Read the CSV file
df = pd.read_csv("data/keystrokes.csv")

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

def gen_text():
    global df 
    # Sort descending by count
    df = df.sort_values("count", ascending=False)
    # df.to_csv("test.csv")
    with open("symbol-stats.csv", 'w') as f:
        for i in range(df.shape[0]):
            f.write(f'{df["char"].iloc[i]} {df["count"].iloc[i]}\n')

def gen_plot():
    # (Optional) Pick top N keys
    global df 

    # Plot
    plt.figure(figsize=(8, 12))
    # plt.barh(df["key"], df["count"], color='skyblue')
    plt.barh(df["char"], df["count"], color='skyblue', align='center') #, width=0.5)
    plt.xlabel("Press Count")
    plt.title(f"Top {top_n} Most Pressed Keys")
    plt.gca().invert_yaxis()  # Most-used at top
    plt.tight_layout()

    # Save or display
    plt.savefig("data/keystats_plot.png", dpi=200)
    #plt.show()

n = 50
print(df.shape[0])
df["char"] = df["key"].apply(lambda k : convert(k))
top_n = min(n, df.shape[0]) if n > 0 else df.shape[0]
print(df[df["count"] > 0])
print(df.head(top_n))
# Sort descending by count
df = df.sort_values("count", ascending=False)

# print(df["char"].value_counts())
df = df.head(top_n)
df = df.reset_index(drop=True)
print(df.shape)
print(df)

gen_plot()
gen_text()

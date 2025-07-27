#!/usr/bin/env python
limit = 1000
width = 1000
col_headings = ["Character", "No. of Presses", "Percentage", "% plot"]
offset = 5
with open("data/symbol-stats.csv", 'r') as sym:
    s = [i.strip().split(" ") for i in sym.readlines()]
    # print(s)
    m = int(max(s, key = lambda x : int(x[1]))[1])
    tot = sum([int(i[1]) for i in s])
    with open("data/ascii-plot.txt", 'w') as out:
        out.write((" " * offset).join(col_headings) + "\n")
        for i in range(min(1000, len(s))):
            char = s[i][0] + (len(col_headings[0]) + offset - len(s[i][0])) * " "
            presses = s[i][1] + (len(col_headings[1]) + offset - len(s[i][1])) * " "
            frac = float(int(s[i][1]))/tot
            percent_str = str(round(100*frac,2))
            percent = percent_str + "%" + (len(col_headings[2]) + offset - len(percent_str)) * " "
            pplot = int(frac * width) * ":"
            out.write(f'{char}{presses}{percent}{pplot}\n')

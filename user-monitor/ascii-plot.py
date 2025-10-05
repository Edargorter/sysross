#!/usr/bin/env python
from datetime import datetime 
width = 750
col_headings = ["Character", "No. of Presses", "Percentage", "% plot"]
offset = 5
time_format = "%Y-%m-%d %H:%M"

with open("data/time_start_end.txt", 'r') as tf:
    t = [int(i) for i in tf.readline().split(',')]
    start_time = datetime.fromtimestamp(t[0])
    st_formatted = start_time.strftime(time_format)
    end_time = datetime.fromtimestamp(t[1])
    et_formatted = end_time.strftime(time_format)
    duration = end_time - start_time

with open("data/symbol-stats.csv", 'r') as sym:
    s = [i.strip().split(" ") for i in sym.readlines()]
    m = int(max(s, key = lambda x : int(x[1]))[1])
    tot = sum([int(i[1]) for i in s])
    with open("data/ascii-plot.txt", 'w') as out:
        out.write(f"Key press stats: {st_formatted} - {et_formatted} ({duration.days} days {int(duration.total_seconds() / 3600) % 24}h {int(duration.total_seconds() / 60) % 60}m {int(duration.total_seconds()) % 60}s)\n\n")
        out.write(f"Total key presses >= {tot}\n\n")
        out.write((" " * offset).join(col_headings) + "\n")
        for i in range(min(1000, len(s))):
            char = s[i][0] + (len(col_headings[0]) + offset - len(s[i][0])) * " "
            presses = s[i][1] + (len(col_headings[1]) + offset - len(s[i][1])) * " "
            frac = float(int(s[i][1]))/tot
            percent_str = str(round(100*frac,2))
            percent = percent_str + "%" + (len(col_headings[2]) + offset - len(percent_str)) * " "
            pplot = int(frac * width) * ":"
            out.write(f'{char}{presses}{percent}{pplot}\n')

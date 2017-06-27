lines = []
with open("sample1.dat") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

print sorted(lines,reverse=True)[:3]
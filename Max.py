lines = [0]
with open("sample1.dat") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        if len(lines) > 3:
            lines.remove(min(lines))

print '\n'.join(lines)

lines = [0]
with open("sample1.dat") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        if len(lines) > 3:
            lines.remove(min(lines))

for i in range(len(lines)):
    for i in range(len(lines)-1):
        if lines[i] < lines[i+1]:
            lines[i+1], lines[i] = lines[i], lines[i+1]

print '\n'.join(lines)

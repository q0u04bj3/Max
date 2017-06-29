lines = [0]

def my_min(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

with open("sample1.dat") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
        if len(lines) > 3:
            lines.remove(my_min(lines))

print '\n'.join(lines)

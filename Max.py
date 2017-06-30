lines = [0]

def my_min(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val

def Max(file):
    with open(file) as file:
        for line in file:
            lines.append(line.strip('\n'))
            if len(lines) > 3:
                lines.remove(my_min(lines))

    return '\n'.join(lines)

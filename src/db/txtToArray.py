def dictionary_to_array(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                result.append(line)
    return result

def point_to_array(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                data = line.split()
                result.append([data[0], int(data[1])])
    return result

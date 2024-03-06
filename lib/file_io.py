def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.writelines(file_content)

    
def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.writelines(append_content)


def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as f:
        lines = f.readlines()
        return ''.join(lines)

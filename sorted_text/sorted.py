import os

txt_files = ['1.txt', '2.txt', '3.txt']
script_directory = os.path.dirname(os.path.abspath(__file__))

file_info = []

for filename in txt_files:
    file_path = os.path.join(script_directory, filename)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        file_lines = len(lines)
        file_info.append((filename, file_lines, lines))

file_info = sorted(file_info, key=lambda x: x[1])
result_file_path = os.path.join(script_directory, 'result.txt')

with open(result_file_path, 'w') as f:
    for info in file_info:
        f.write(f'{info[0]}\n')
        f.write(f'{info[1]}\n')
        f.write(''.join(info[2]))

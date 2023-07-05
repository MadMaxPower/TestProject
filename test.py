import os

dir_name =os.path.dirname(os.path.abspath(__file__))
pth_to_file = os.path.join(dir_name, 'main.py')
# print(pth_to_file)

os_command = f'python {pth_to_file}'

os.system(os_command)
import os

dir_name = ("c:\\python_test\\")

file_count = sum([len(files) for r, d, files in os.walk(dir_name)])
if file_count > 3
ks_folder = os.listdir(dir_name)
for item in ks_folder:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

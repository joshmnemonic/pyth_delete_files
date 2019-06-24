import os, smtplib

dir_name = ("c:\\python_test\\")

file_count = sum([len(files) for r, d, files in os.walk(dir_name)])
ks_folder = os.listdir(dir_name)
for item in ks_folder:
    if item.endswith(".txt") and file_count > 3:
        os.remove(os.path.join(dir_name, item))

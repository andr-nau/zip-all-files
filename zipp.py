import zipfile as zp
import os
import sys

main_path = os.getcwd()  #'D:\\test'

# Check if it is root directory. Can be dangerous.
if os.path.splitdrive(main_path)[1] == '\\':
    root = input('This is root directory. Are you sure to archive all files? y/n: ')
    if root in ('y', 'Y'):
        pass
    else:
        sys.exit()

files_to_arch = []

def listing_to_zip(path):
    """
    Input: directory path (string)
    Output: list (string) of full paths - list of all files in all dirs to archive.
    """
    
    files = os.listdir(path)
    
    for file in files:
        file_path = os.path.join(path, file)  # Join main dir path and relative file path
        
        if os.path.isdir(file_path) and ('archived' not in file_path):  # if dir - recurcively run function again
            listing_to_zip(file_path)
        
        elif os.path.splitext(file_path)[1] in ('.zip', '.rar', '.7z', '.py'):
            pass

        else:
            files_to_arch.append(file_path)
    
    return files_to_arch


list_to_arch = listing_to_zip(main_path)
print('Files to archiving: ', len(list_to_arch))

common_path = os.path.commonpath(list_to_arch)

output_path = os.path.commonpath(list_to_arch) + '-archived'

try:
    os.mkdir(output_path)
except OSError as error:
    print(error)
    input()


for file in list_to_arch:
    
    print('Init path: ', file)
    
    file_path, file_name = os.path.split(file)
    
    save_path = os.path.join(output_path, os.path.relpath(file_path, start=common_path))
    save_name = file_name + '.zip'
    zip_path = save_path + '\\' + save_name

    
    if not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)
    
    with zp.ZipFile(zip_path, 'w', zp.ZIP_DEFLATED, compresslevel=3) as myzip:
        myzip.write(file, arcname=file_name)

input()
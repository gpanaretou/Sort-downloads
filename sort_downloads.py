import os
from pathlib import Path


def get_directory():
    return Path('/home/george/Downloads')


def read_files(path):
    g = path.glob('*.*')
    files = [x for x in g if x.is_file()]
    if not files:
        exit('No files to sort, ending program.')

    return files


def get_extentions(list_of_paths):
    extentions = []
    
    for path in list_of_paths:
        suffix = path.suffix
        if suffix not in extentions:
            extentions.append(suffix)

    return extentions
        

def create_folders(extensions, path):
    extension_list = [x[1:] for x in extensions]
    
    for suffix in extension_list:
        if not (path / suffix.upper()).is_dir():
            (path/suffix.upper()).mkdir()


def move_files(extensions, path, files):
    extension_list = [x[1:] for x in extensions]
    directory_names = [x.upper() for x in extension_list]

    for file in files:
        suffix = file.suffix
        suffix_u = suffix[1:].upper()

        filename = file.name

        if (path/suffix_u/filename).is_file():
            version = filename.stem[-2]

            if version.isdigit():
                version = int(version) + 1
                new_filename = filename.stem + f' ({version})'
                new_filename = new_filename + suffix
                (path/suffix_u).replace(path/suffix_u/new_filename)
   
        else:
            (path/filename).replace(path/suffix_u/filename)

        
def main():

    print('\n')
    downloads_path = get_directory()
    files = read_files(downloads_path)
    extensions = get_extentions(files)

    create_folders(extensions, downloads_path)
    move_files(extensions, downloads_path, files)

    print('END OF PROGRAM \n')
    


if __name__ == "__main__":
    main()
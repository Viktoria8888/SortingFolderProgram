
from Settings import *
# dir = "/home/viktoria/Downloads"
def organize_folder(dir):
    files = os.listdir(dir)
    # I will not show hidden files
    # Hidden files are those that start with a dot (.)
    visible_files = [file for file in files if not file.startswith('.')]
    names_of_folders = {
        "pdf" : "Pdf Files",
        "jpg" : "Images",
        "png" : "Images",
        "mp3" : "Music",
        "zip" : "Zip Files"
    }
    files_types = defaultdict(list)
    valid_expressions = set(names_of_folders.keys())
    # Adding programming languages stuff
    for l in ["cpp", "py", "c", "rkt","java"]:
        names_of_folders[l] = "Code files"

    # Mapping folder names to corresponding files
    for file in visible_files:
        type = file.split(".")[-1]
        if type in valid_expressions:
            files_types[names_of_folders[type]].append(file)

    # Creating directories and moving files;
    for k, v in files_types.items():
        path = os.path.join(dir,k)
        if not os.path.exists(path):
            os.mkdir(path)
        for file in v:
            try:
                destination_path = os.path.join(path,file)
                if os.path.exists(destination_path):
                    base_name, ext = os.path.splitext(destination_path)
                    i = 1
                    while os.path.exists(destination_path):
                        destination_path = f"{base_name}_{i}{ext}"
                        i += 1
                source_path = os.path.join(dir,file)
                shutil.move(source_path,path)
            except FileExistsError:
                print(f"'{file}' already exists.")
            except shutil.Error as e:
                print(f"An error occurred: {e}")
organize_folder(dir)






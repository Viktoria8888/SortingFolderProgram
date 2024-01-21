
from Settings import *
# dir = "/home/viktoria/Downloads"
def organize_folder(dir):
    files = os.listdir(dir)
    # I will not show hidden files
    # Hidden files are those that start with a dot (.)
    visible_files = [file for file in files if not file.startswith('.')]
    names_of_folders = {
        ("pdf",) : "Pdf Files",
        ("jpg","png","jpeg") : "Images",
        ("mp3",) : "Music",
        ("zip",) : "Zip Files",
        ("txt", "docs") : "Text Files",
        ("cpp", "py", "c", "rkt","java","js", "ts"): "Code files",
        ("mp4",): "Movies"

    }
    extension_to_folder = {}
    for extensions, folder_name in names_of_folders.items():
        for extension in extensions:
            extension_to_folder[extension] = folder_name

    files_types = defaultdict(list)
    # Mapping folder names to corresponding files
    for file in visible_files:
        extension = file.split(".")[-1]
        if extension in extension_to_folder:
            folder_name = extension_to_folder[extension]
            files_types[folder_name].append(file)

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
# organize_folder(dir)






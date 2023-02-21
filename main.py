import os
import shutil

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
            ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
            ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
            ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}

def get_file_format(file_name):
    return os.path.splitext(file_name)[1].lower()

def get_directory(file_format):
    for directory, file_formats in DIRECTORIES.items():
        if file_format in file_formats:
            return directory
    return None

def organize_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_format = get_file_format(file_name)
            directory = get_directory(file_format)
            if directory is None:
                continue
            source_path = os.path.join(root, file_name)
            destination_dir = os.path.join(os.getcwd(), directory)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.copy(source_path, destination_path)
    print("SUDAH SEELSAI------")

if __name__ == "__main__":
    dir_path = "/home"
    organize_files(dir_path)

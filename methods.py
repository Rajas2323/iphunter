import shutil

def TransferImage(path):
    shutil.copy(path, "static")

    arr = path.split("\\")

    return "static/" + arr[-1]



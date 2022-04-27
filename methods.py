import shutil

def TransferImage(path):
    shutil.copy(path, "static/locationimages")

    arr = path.split("\\")

    return "static/locationimages/" + arr[-1]



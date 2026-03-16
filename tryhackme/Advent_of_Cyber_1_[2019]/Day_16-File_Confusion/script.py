import zipfile

with zipfile.ZipFile("final-final-compressed_1576527731602.zip") as zip_ref:
    zip_ref.extractall("unzipped/")

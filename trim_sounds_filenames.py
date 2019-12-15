import os

for root, dirs, files in os.walk('./sounds'):
    for f in files:
        filename, ext = os.path.splitext(f)
        new_filename = filename.strip() + ext
        if ext == '.mp3':
            new_filename = os.path.join(root, new_filename)
            old_filename = os.path.join(root, f)
            if ' ' in old_filename:
                print(old_filename)
            os.rename(old_filename, new_filename)

import os, shutil

def copy_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(src):
        src_full = os.path.join(src, item)
        dst_full = os.path.join(dst, item)
        if os.path.isfile(src_full):
            shutil.copy(src_full, dst_full)
        else:
            copy_recursive(src_full, dst_full)
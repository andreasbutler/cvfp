
import os

if __name__ == "__main__":
    path = "dataset5\\A"
    subdirs = [x[0] for x in os.walk(path)]
    for sd in subdirs:
        if sd != path:
            depth_dir = os.path.join("dataset5\\A_validate", sd[-1])
            try:
                os.stat(depth_dir)
            except:
                os.makedirs(depth_dir)
            files = os.listdir(sd)
            for i in range(25):
                f = files[i]
                os.rename(os.path.join(sd,f), os.path.join(depth_dir,f))
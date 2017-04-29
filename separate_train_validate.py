
import os
import numpy.random

if __name__ == "__main__":
    path = "CNN_input\\depth_data\\train"
    subdirs = [x[0] for x in os.walk(path)]
    for sd in subdirs:
        if sd != path:
            depth_dir = os.path.join("CNN_input\\depth_data\\test", sd[-3:])
            try:
                os.stat(depth_dir)
            except:
                os.makedirs(depth_dir)
            files = os.listdir(sd)
            size = int(0.2*len(files))
            i = 0
            while i < size:
                f = numpy.random.choice(files)
                try:
                    os.rename(os.path.join(sd,f), os.path.join(depth_dir,f))
                except:
                    i -= 1
                i += 1
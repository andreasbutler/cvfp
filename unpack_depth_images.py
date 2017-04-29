import os

if __name__ == "__main__":
    for i in range(1,6):
        for s in ["1-10", "11-20", "21-31"]:
            dir = "CNN_input\\subject" + str(i) + "\\class" + s
            target_dir = "CNN_input\\depth_data\\train"
            files = os.listdir(dir)
            dirs = [x[0] for x in os.walk("CNN_input")]
            for f in files:
                c = f[4:7]
                depth_dir = os.path.join(target_dir,c)
                try:
                    os.stat(depth_dir)
                except:
                    os.makedirs(depth_dir)
                os.rename(os.path.join(dir,f), os.path.join(depth_dir,f))
    # for d in dirs:
    #     print(d)
        # if sd != path:
        #     depth_dir = os.path.join("dataset5\\A_validate", sd[-1])
        #     try:
        #         os.stat(depth_dir)
        #     except:
        #         os.makedirs(depth_dir)
        #     files = os.listdir(sd)
        #     for i in range(25):
        #         f = files[i]
        #         os.rename(os.path.join(sd,f), os.path.join(depth_dir,f))
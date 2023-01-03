import glob
import os
import random
import shutil

# KSDD = 'KSDD'
# root_dir = 'E:/denso/mixed-segdec-net-comind2021-master/results/KSDD/N_33/FOLD_1/test_outputs'
# target_dir = 'Data1'
# full_sample = os.listdir(root_dir)
# for sample in full_sample:
#     folder = sample[13:18]
#     file = sample[19:28]
#     shutil.move(os.path.join(KSDD, folder, file), os.path.join(target_dir, 'Test', folder + '_' + file))
#
#
# samples = glob.glob(KSDD + '/*/*.jpg')
#
# for sample in samples:
#     folder = sample[5:10]
#     file = sample[11:21]
#     shutil.move(os.path.join(KSDD, folder, file), os.path.join(target_dir, 'Train', folder + '_' + file))
#     shutil.move(os.path.join(KSDD, folder, file[0:5] + '_label.bmp'), os.path.join(target_dir, 'Train', folder + '_' + file[0:5] + '_label.bmp'))
#
# errors = glob.glob(KSDD + '/*/*.jpg')
#
# for error in errors:
#     print(error)

root = "E:/KSDD"
samples = "Data/Test"

for sample in os.listdir(samples):
    if os.path.splitext(sample)[-1] == ".jpg":
        folder = sample[0:5]
        file = sample[6:11]
        if os.path.exists(os.path.join(root, "neg", folder, file + ".jpg")):
            os.rename(os.path.join(samples, folder + "_" + file + "_label.bmp"), os.path.join(samples, "F_" + folder + "_" + file + "_label.bmp"))
        elif os.path.exists(os.path.join(root, "pos", folder, file + ".jpg")):
            os.rename(os.path.join(samples, folder + "_" + file + "_label.bmp"), os.path.join(samples, "T_" + folder + "_" + file + "_label.bmp"))
        # if os.path.exists(os.path.join(root, "neg", folder, file + ".jpg")):
        #     shutil.copy(os.path.join(root, "neg", folder, file + "_label.bmp"),
        #                 os.path.join(samples, folder + "_" + file + "_label.bmp"))
        # elif os.path.exists(os.path.join(root, "pos", folder, file + ".jpg")):
        #     shutil.copy(os.path.join(root, "pos", folder, file + "_label.bmp"),
        #                 os.path.join(samples, folder + "_" + file + "_label.bmp"))

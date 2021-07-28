import numpy as np
import glob

# Number of points per sequence collected
no_points = 500

# Insert the directory where the data is saved here
dir = 'D:/SEP769_DeepLearning/'

files_no = glob.glob(dir + 'normal/*.csv')
folders_im = glob.glob(dir + 'imbalance/*')
train_data = np.empty((0, no_points,8), float)
test_data = np.empty((0, no_points,8), float)
i=0
for f_on in files_no:
    source_data = np.loadtxt(f_on, delimiter=",")
    for j in range(10*7):
        A = source_data[2000*j:2000*j+no_points,:]
        if (i%4 != 0):
            train_data = np.append(train_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)
        else:
            test_data = np.append(test_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)
    i=i+1
    print(i)

train_label = np.zeros(train_data.shape[0])
test_label = np.zeros(test_data.shape[0])

for folder in folders_im:
    i=0
    files_im = glob.glob( folder +'/*.csv')
    for f_im in files_im:
        source_data = np.loadtxt(f_im, delimiter=",")
        for j in range(10):
            A = source_data[2000*j:2000*j+no_points,:]
            if (i%4 != 0):
                train_data = np.append(train_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)
            else:
                test_data = np.append(test_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)
        i=i+1
        print(i)
    
train_label = np.append(train_label, np.ones(train_data.shape[0]-train_label.shape[0]), axis=0)
test_label = np.append(test_label, np.ones(test_data.shape[0]-test_label.shape[0]), axis=0)

train_reshaped = np.reshape(train_data,(-1,8))
test_reshaped = np.reshape(test_data,(-1,8))

np.savetxt(dir + "jul27data/train_data.txt", train_reshaped)
np.savetxt(dir + "jul27data/test_data.txt", test_reshaped)


np.savetxt(dir + "jul27data/train_label.txt", train_label)
np.savetxt(dir + "jul27data/test_label.txt", test_label)

print("Finished parsing the files")

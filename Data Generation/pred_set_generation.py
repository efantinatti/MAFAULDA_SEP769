import numpy as np
import glob
# Start here

no_points = 500;
choice = 1;
if choice == 1:
    files_no = glob.glob('C:/Users/Amir/Documents/Graduate School/SEP769/DeepLearning Project/normal/*.csv')
    folders_im = glob.glob('C:/Users/Amir/Documents/Graduate School/SEP769/DeepLearning Project/imbalance/*')
    pred_data = np.empty((0, no_points,8), float)
    i=0
    for f_on in files_no:
        if (i%4 == 0):
            source_data = np.loadtxt(f_on, delimiter=",")
            for j in range(1,11):
                A = source_data[20000*j:20000*j+no_points,:]
                pred_data = np.append(pred_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)

        i=i+1
        print(i)

    pred_label = np.zeros(pred_data.shape[0])
    
    for folder in folders_im:
        i=0
        files_im = glob.glob( folder +'/*.csv')
        for f_im in files_im:
            if (i%4 == 0):
                source_data = np.loadtxt(f_im, delimiter=",")
                for j in range(1,11):
                    A = source_data[20000*j:20000*j+no_points,:]
                    pred_data = np.append(pred_data,A.reshape(1, A.shape[0],A.shape[1]),axis=0)
            i=i+1
            print(i)
        
    pred_label = np.append(pred_label, np.ones(pred_data.shape[0]-pred_label.shape[0]), axis=0)
    pred_reshaped = np.reshape(pred_data,(-1,8))

    
    np.savetxt("pred_data.txt", pred_reshaped)

    np.savetxt("pred_label.txt", pred_label)
    
    print("Finished parsing the files")

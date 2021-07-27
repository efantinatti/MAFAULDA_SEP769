import numpy as np
import glob

no_points = 5000;
choice = 1;
if choice == 1:
    files_no = glob.glob('D:/SEP769_DeepLearning/normal/*.csv')
    folders_im = glob.glob('D:/SEP769_DeepLearning/imbalance/*')
    train_data = np.empty((0, no_points,8), float)
    test_data = np.empty((0, no_points,8), float)
    i=0
    for f_on in files_no:
        source_data = np.loadtxt(f_on, delimiter=",")
        for j in range(5*6):
            A = source_data[5000*j:5000*j+no_points,:]
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
            for j in range(5):
                A = source_data[5000*j:5000*j+no_points,:]
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
    
    np.savetxt("D:/SEP769_DeepLearning/jul26data/train_data.txt", train_reshaped)
    np.savetxt("D:/SEP769_DeepLearning/jul26data/test_data.txt", test_reshaped)
    

    np.savetxt("D:/SEP769_DeepLearning/jul26data/train_label.txt", train_label)
    np.savetxt("D:/SEP769_DeepLearning/jul26data/test_label.txt", test_label)
    
    print("Finished parsing the files")

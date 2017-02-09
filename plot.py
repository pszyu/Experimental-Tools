import matplotlib.pyplot as plt
import numpy as np
import os
import glob


# plot
def plot_from_file(file_name, dir):
    print "plotting " + file_name
    data = np.loadtxt(dir+file_name)
    data = 1 - data
    iter_per_epoch = 391
    plt.figure()
    plt.plot((iter_per_epoch*np.arange(start=1, stop=(len(data)+1))), data)
    plt.xlabel('iteration')

    """
    if file_name[-7:-4] == 'Acc':
        plt.ylabel('Accuracy')
    elif file_name[-7:-4] == 'oss':
        plt.ylabel('Loss')
    else:
        plt.ylabel('Weights Sum')
    """
    plt.ylabel('Error')
    plt.title(file_name[0:-4])
    plt.savefig(dir+'plots/'+file_name[0:-4])
    plt.close()


# retrieve the names of all files under the directory
def retrieve_file_names(dir):
    return [f for f in os.listdir(dir) if f[-3:] == 'txt']


# plot.py should be placed same level as the dir where data files are
def plot():
    dir = os.getcwd()+'/2017-01-31/'
    file_names = retrieve_file_names(dir)
    for file_name in file_names:
        plot_from_file(file_name, dir)

if __name__ == '__main__':
    plot()

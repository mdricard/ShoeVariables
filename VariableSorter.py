import os
import numpy as np

# Get the list of all files and directories
foot_strike = 'rearfoot'
fs = 'Rear'
folder = 'F:/Shoe_2023/'
sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
for i in range(len(sub_folders)):
    s = sub_folders[i]
    subject = s[1:]
#subject = '5'
path = 'F:/Shoe_2023/' + foot_strike + '/S' + subject
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)

correct_order = ['AnkleAtPKStiff', 'AnkleAtRON', 'AnkleJointStiffness', 'GRFImpulseNormRSK', 'GRFImpulseNormRSK', 'GRFImpulseNormRSK', 'KneeAtPeakStiff',	'KneeAtRON', 'KneeJointStiffness', 'PelvisHorVelMinus10', 'RightKneeImpulse', 'RightKneeImpulse', 'RightKneeImpulse', 'ShankVelRON']


def check_order():
    order = True
    for i in range(14):
        if var_names[i] != correct_order[i]:
            order = False
    return order


for file in range(len(dir_list)):
    filename = dir_list[file]
    trial = filename[7:9]
    shoe = filename[4:6]
    fn = path + '/' + filename
    all = np.genfromtxt(fn, dtype=str,  delimiter='\t', skip_header=1)
    var_names = all[0, 1:15]
    xyz = all[3, 1:15]
    val = all[4, 1:15]
    response = check_order()
    if response == False:
        text = input("Something is terribly wrong!")  # Python 3
    with open('F:/Shoe_2023/stats.csv', 'a') as stat_file:
        #stat_file.write('Subject, footstrike, Shoe, Trial, AnkleAtPKStiff, AnkleAtRON, AnkleJointStiffness, GRFImpulseNormRSK, GRFImpulseNormRSK, GRFImpulseNormRSK, KneeAtPeakStiff,	KneeAtRON, KneeJointStiffness, PelvisHorVelMinus10, RightKneeImpulse, RightKneeImpulse, RightKneeImpulse, ShankVelRON \n')
        stat_file.write(subject + ',' + fs + ',' + shoe + ',' + trial + ',' + val[0] + ',' + val[1] + ',' + val[2] + ',' + val[3] + ',' + val[4] + ',' + val[5] + ',' + val[6] + ',' + val[7] + ',' + val[8] + ',' + val[9] + ',' + val[10] + ',' + val[11] + ',' + val[12] + ',' + val[13] + ',' + '\n')
    stat_file.close()
    print(file)








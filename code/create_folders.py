import os
import numpy as np
import shutil
# Path for exported data i.e numpy arrays
DATA_PATH = os.path.join('MP_Data')

# Actions that we are try to detect
actions = []
for i in range(0, 10):
    actions.append(i)

def create():
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    for action in actions:
        folder_dir = os.path.realpath(os.path.join(DATA_PATH, str(action), ''))
        if not os.path.exists(folder_dir):
            # Create a new directory because it does not exist
            os.makedirs(folder_dir)

#create()
#
# origin = os.path.join('MP_Data')
# target = os.path.join('test')

def copy():
    for action in actions:
        for frame_no in range(1,31):
            origin = os.path.join('MP_Data',str(action),str(frame_no))+'.jpg'
            target = os.path.join('test',str(action),str(frame_no))+'.jpg'
            target_folder = os.path.join('test', str(action))

            if not os.path.exists(target_folder):
                # Create a new directory because it does not exist
                os.makedirs(target_folder)
                shutil.copy(origin, target)
            else:
                shutil.copy(origin,target)


copy()
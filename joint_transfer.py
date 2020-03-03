#saving transfer values in joint_transfer variable
#we have taken 30 frames
frames_num=30
count=0
joint_transfer =[]
for i in range(int(len(transfer_values)/frames_num)):
  inc=count+frames_num
  joint_transfer.append([transfer_values[count:inc],labels_train[count]])
  count=inc

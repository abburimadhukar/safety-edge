data=[]
target=[]
epoch_num=1000
batch_s=100
for i in joint_transfer : 
    data.append(i[0])
    target.append(np.array(i[1]))
#training the model
model.fit(data, target, epochs=epoch_num, batch_size=batch_s, verbose=1)
#now that the model is fully trained, save it 
model.save('samaritan.h5',overwrite=True)

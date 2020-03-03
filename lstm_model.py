from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM

n_chunks=30
chunk_size=2048
rnn_size=512

model=Sequential()
model.add(LSTM(rnn_size, input_shape=(n_chunks, chunk_size)))
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(50))
model.add(Activation('sigmoid'))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(loss='mean_squared_error',optimizer='adam', metrics=['accuracy'])

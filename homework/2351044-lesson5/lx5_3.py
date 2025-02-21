import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist


def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    size = 10000  # 测试集大小
    x_train = x_train[:size]  # 截取10000个样本
    y_train = y_train[:size]  # 截取10000个样本
    x_train = x_train.reshape(size, 28 * 28)  # 将 x_train 转换为 10000x784 的二维数组
    x_test = x_test.reshape(x_test.shape[0], 28 * 28)  # 将 x_test 转换为二维数组
    x_train = x_train.astype('float32')  # 转换为 float32 类型
    x_test = x_test.astype('float32')

    # 将类别向量转换为二进制类矩阵
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    x_train /= 255  # 将灰度值归一化
    x_test /= 255

    return (x_train, y_train), (x_test, y_test)


def run():
    # 加载数据
    (x_train, y_train), (x_test, y_test) = load_data()

    # 定义模型
    model = Sequential()
    units = 28 * 28
    # 定义输入层，全连接网络，输入维度是784，有units个神经元，激活函数是ReLU
    model.add(Dense(units=512, input_dim=units, activation='relu'))
    model.add(Dropout(0.2))

    # 定义隐藏层
    model.add(Dense(units=512, activation='relu'))
    model.add(Dropout(0.2))

    # 定义输出层，有10个神经元，也就是10个输出，激活函数是Softmax
    model.add(Dense(units=10, activation='softmax'))

    # 损失函数选择交叉熵，优化器选择Adam
    model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

    # 训练模型
    model.fit(x_train, y_train, batch_size=100, epochs=20, validation_data=(x_test, y_test))

    # 评估模型
    result = model.evaluate(x_train, y_train, batch_size=100)  # 批次数量设为100
    print('\nTrain Acc: %.2f%%' % (result[1] * 100))
    result = model.evaluate(x_test, y_test, batch_size=100)
    print('\nTest Acc: %.2f%%' % (result[1] * 100))


if __name__ == '__main__':
    run()

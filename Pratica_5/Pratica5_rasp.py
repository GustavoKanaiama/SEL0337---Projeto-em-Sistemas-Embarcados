from smbus import SMBus
from time import sleep


addr = 0x8
bus = SMBus(1)

flag = True

while flag:
    dado = bus.read_i2c_block_data(0x8, 0, 2)

    valor = dado[0]*256 + dado[1]

    print(valor)
    
    sleep(0.01)
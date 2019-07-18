#/etc/bin/env python

import argparse
import smbus

#Define i2c bus
bus_no = 1

def main():
    parser = argparse.ArgumentParser(description="Smbpbi command")
    parser.add_argument('address',type=lambda x: int(x,0), help='Slave Device address(7bits). For example: 0x4f')
    parser.add_argument('datain',type=lambda x: int(x,0),help='Data(32bits) to write in 0x5d register. For example: 0x00000000')
    parser.add_argument('command',type=lambda x: int(x,0),help='Command(32bits) to write in 0x5c register. For example: 0x80000002 for GPU temp read')
    args = parser.parse_args()
    #print args.address , args.datain ,args.command
    datain_list=[0x04]
    datain_list.append(args.datain/256/256/256)
    datain_list.append(args.datain/256/256%256)
    datain_list.append(args.datain/256%256)
    datain_list.append(args.datain%256)
    command_list=[0x04]
    command_list.append(args.command/256/256/256)
    command_list.append(args.command/256/256%256)
    command_list.append(args.command/256%256)
    command_list.append(args.command%256)
    #print datain_list
    #print command_list
    bus = smbus.SMBus(bus_no)
    #Write 5D data
    bus.write_i2c_block_data(args.address,0x5d,datain_list)
    #Write 5C command
    bus.write_i2c_block_data(args.address,0x5c,commnd_list)
    #Read 5C reg
    status= bus.read_i2c_block_data(args.address,0x5c,5)
    #Read 5D data
    data_back = bus.read_i2c_block_data(args.address,0x5d,5)
    print status
    print data_back
main()

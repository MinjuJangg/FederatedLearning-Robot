from Controller.Controller import *
import argparse
import time


parser = argparse.ArgumentParser()

parser.add_argument("-j", "--joint", type= str, required= False)

parser.add_argument("-p", "--position", type= int, required= False)

parser.add_argument("-i", "--intialize", type= int, required= False)

args = parser.parse_args()

if __name__ == "__main__":
    con = Controller("client2")

    if(args.intialize == 1):
        con.initialize()
    else:
        con.servo_control(args.joint, args.position)

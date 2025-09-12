#!/usr/bin/env python3

import time
from Utils.PCA9685 import *
from Utils.Constants import *
from Camera.Camera import *

class Controller():
    def __init__(self, clientName: str):
        """
        :param clientName:
        """

        self.clientName = clientName

        # self.camera = Camera()

        self.pwmController = PCA9685()
        # set optimal frequency
        self.pwmController.setPWMFreq(SERVO_FREQ)

        # joint moving range information
        self.jointGripperPosInfo = JOINT_POS_INFO[clientName]["gripper"]
        self.jointR1PosInfo = JOINT_POS_INFO[clientName]["r1"]
        self.jointR2PosInfo = JOINT_POS_INFO[clientName]["r2"]
        self.jointTPosInfo = JOINT_POS_INFO[clientName]["t"]

        # current position information
        self.jointGripperCurrentPos = JOINT_POS_INFO[clientName]["gripper"]["init"]
        self.jointR1CurrentPos = JOINT_POS_INFO[clientName]["r1"]["init"]
        self.jointR2CurrentPos = JOINT_POS_INFO[clientName]["r2"]["init"]
        self.jointTCurrentPos = JOINT_POS_INFO[clientName]["t"]["init"]

        # goal position information
        self.jointGripperInitPos = JOINT_POS_INFO[clientName]["gripper"]["init"]
        self.jointR1InitPos = JOINT_POS_INFO[clientName]["r1"]["init"]
        self.jointR2InitPos = JOINT_POS_INFO[clientName]["r2"]["init"]
        self.jointTInitPos = JOINT_POS_INFO[clientName]["t"]["init"]
        self.jointInitPos = {"gripper": self.jointGripperInitPos,
                             "r1": self.jointR1InitPos,
                             "r2": self.jointR2InitPos,
                             "t": self.jointTInitPos
                             }
        self.jointCurrentPos = self.jointInitPos
        print(self.jointCurrentPos)
    def servo_control(self, joint: str, goalPos: int) -> None:
        """
        :param joint: gripper, r1, r2, t
        :param goalPos:
        :return: void
        """

        servoPin = SERVO_PIN[joint]

        currentPos = self.jointCurrentPos[joint]


        if (goalPos >= currentPos):
            step = (goalPos - currentPos) // SERVO_MOVING_STEP
            for i in range(step):

                currentPos += SERVO_MOVING_STEP
                self.pwmController.setServoPulse(servoPin, currentPos)
                time.sleep(0.5)

                self.jointCurrentPos[joint] = currentPos


        else:
            step = (currentPos - goalPos) // SERVO_MOVING_STEP
            for i in range(step):

                currentPos -= SERVO_MOVING_STEP
                self.pwmController.setServoPulse(servoPin, currentPos)
                time.sleep(0.5)

                self.jointCurrentPos[joint] = currentPos


    def initialize(self) -> None:
        for joint in SERVO:
            servoPin = SERVO_PIN[joint]
            self.pwmController.setServoPulse(servoPin, self.jointInitPos[joint])
            self.jointCurrentPos[joint] = self.jointInitPos[joint]
            print(self.jointCurrentPos[joint])
            time.sleep(0.5)



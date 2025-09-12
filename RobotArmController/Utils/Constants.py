# client ip information
CLIENT_NETWORK_INFO = {
    "client1": dict(ip="192.168.0.22",
                    password="grom0419",
                    port=22),
    "client2": dict(ip="192.168.0.7",
                    password="grom0419",
                    port=5446),
    "client3": dict(ip="192.168.0.165",
                    password="grom0419",
                    port=5446),
    "client4": dict(ip="192.168.0.24",
                    password="grom0419",
                    port=5446),
}
# servo frequency
SERVO_FREQ = 50

# move by each step
SERVO_MOVING_STEP = 5

# servo information
SERVO = {"gripper", "r1", "r2", "t"}

# servo pin information
SERVO_PIN = {
    "gripper": 0,
    "r1": 3,
    "r2": 5,
    "t": 8
}

# joint position information
JOINT_POS_INFO = {
    "client1": dict(gripper={
        "init": 130
    }, r1={
        "init": 160
    }, r2={
        "init": 35,
    }, t={
        "init": 115
    }),
    "client2": dict(gripper={
        "init": 130
    }, r1={
        "init": 150
    }, r2={
        "init": 15
    }, t={
        "init": 100

    }),
    "client3": dict(gripper={
        "init": 150
    }, r1={
        "init": 150
    }, r2={
        "init": 150
    }, t={
        "init": 150
    }),
    "client4": dict(gripper={
        "init": 150
    }, r1={
        "init": 150
    }, r2={
        "init": 150
    }, t={
        "init": 150
    })
}

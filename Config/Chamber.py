ChamberList = [
        "ME11a",
        "ME12HV3",  
        "ME21HV1",  
        "ME22HV2",  
        "ME31HV1",  
        "ME32HV2",  
        "ME41HV1",  
        "ME42HV2",
        "ME11b",    
        "ME13HV1",  
        "ME21HV2",  
        "ME22HV3",  
        "ME31HV2",  
        "ME32HV3",  
        "ME41HV2",  
        "ME42HV3",
        "ME12HV1",  
        "ME13HV2",  
        "ME21HV3",  
        "ME22HV4",  
        "ME31HV3",  
        "ME32HV4",  
        "ME41HV3",  
        "ME42HV4",
        "ME12HV2",  
        "ME13HV3",  
        "ME22HV1",  
        "ME22HV5",  
        "ME32HV1",  
        "ME32HV5",  
        "ME42HV1", 
        "ME42HV5",
        ]

y_segment_dict = {
        "ME11": [-80.,80.],
        "ME12": [-80.,100.],  
        "ME21": [-100.,100.],  
        "ME22": [-180.,180.],  
        "ME31": [-100,120.],  
        "ME32": [-180.,180.],  
        "ME41": [-80.,100.],  
        "ME42": [-180.,180.],
        "ME13": [-100.,100.],  
        }

ChamberTypes = y_segment_dict.keys()

ChamberDict = {
    0: "ME11a",
    1: "ME11b",
    2: "ME12HV1",
    3: "ME12HV2",
    4: "ME12HV3",
    5: "ME13HV1",
    6: "ME13HV2",
    7: "ME13HV3",
    8: "ME21HV1",
    9: "ME21HV2",
    10: "ME21HV3",
    11: "ME31HV1",
    12: "ME31HV2",
    13: "ME31HV3",
    14: "ME41HV1",
    15: "ME41HV2",
    16: "ME41HV3",
    17: "ME22HV1",
    18: "ME22HV2",
    19: "ME22HV3",
    20: "ME22HV4",
    21: "ME22HV5",
    22: "ME32HV1",
    23: "ME32HV2",
    24: "ME32HV3",
    25: "ME32HV4",
    26: "ME32HV5",
    27: "ME42HV1",
    28: "ME42HV2",
    29: "ME42HV3",
    30: "ME42HV4",
    31: "ME42HV5",
    }

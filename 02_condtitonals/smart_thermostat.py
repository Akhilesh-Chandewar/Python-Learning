device_status = 'active'
device_temp = 38

if device_status :
    if device_temp > 35:
        print("High temperature")
    else:
        print("Normal temperature")
else:
    print("Device is off")
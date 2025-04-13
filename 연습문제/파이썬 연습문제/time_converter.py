import numpy as np

time_param = 12345

hour = int(time_param/3600)
# print(hour)

minute = int((time_param%3600)/60)
# print(minute)

second = (time_param%3600)%60
# print(second)

print(f"{time_param}초는 {hour}시간 {minute}분 {second}초입니다. ")

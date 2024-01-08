import math

def convert_time(second:int)->int:
    hour = math.floor(second/3600)
    hour_remainder = second%3600
    minute = math.floor(hour_remainder/60)
    minute_remainder = second%60
    strtime = f"{hour}h:{minute}m:{minute_remainder}s"
    return strtime

    
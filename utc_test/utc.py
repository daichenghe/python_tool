import time
import datetime
def utc2local(utc_st):

    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local2utc(local_st):
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

if __name__ == '__main__':
    year = int(time.strftime("%Y"))
    month = int(time.strftime("%m"))
    day = int(time.strftime("%d"))
    hour = int(time.strftime("%H"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    local_time = datetime.datetime(year, month, day, hour, minute, second)
    utc_time = local2utc(local_time)
    d1 = datetime.datetime(year, 1, 1)
    utc_sub = utc_time - d1 

    print (utc_sub)
    print (dir(datetime.timedelta))
    utc_str = utc_sub.__str__()
    utc_day_int = int(utc_str.split( )[0])
    print ("test")
    print (utc_day_int)
    utc_day_str = str(utc_day_int + 1)
    print (utc_day_str)


























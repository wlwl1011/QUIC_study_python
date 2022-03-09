import time

now = time.localtime()
print("현재 시간은 %d년 %d월 %d일 %d시 %d분 %d초 입니다." %
      (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

x = '100'
print("%s" % x)

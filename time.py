import datetime
x = datetime.datetime.now()
if x.hour < 12 :
    print("현재 시간은 {HOUR}시로 오전입니다.".format(HOUR = x.hour))
else :
    print("현재 시간은 {HOUR}시로 오후입니다.".format(HOUR= x.hour))
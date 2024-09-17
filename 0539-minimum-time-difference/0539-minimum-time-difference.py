class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # for i in range(1,len(timePoints)):
        #     if timePoints[i-1]<timePoints[i]:
        #         timePoints[i],timePoints[i-1]=timePoints[i-1],timePoints[i]
        # time=555
        # cur_sec=0
        # for i in timePoints:
        #     if int(i[:2])<=time:
        #         prev=time
        #         prev_sec=cur_sec
        #         time=int(i[:2])
        #         cur_sec=int(i[3:])
        # # print(prev,time)
        # # print(prev_sec,cur_sec)
        # if prev==0:
        #     prev=23
        # if time==0:
        #     time=23
        # if prev_sec==0:
        #     prev_sec=60
        # if cur_sec==0:
        #     cur_sec=60
        # print(prev,time)
        # print(prev_sec,cur_sec)
        # hr_dif=abs(prev-time)
        # min_dif=abs(prev_sec-cur_sec)
        # return (hr_dif*60)+min_dif
        lst=[]
        def conversion(time):
            hrs,minute=time.split(':')
            hrs,minute=int(hrs),int(minute)
            prev_hr=hrs
            
            if minute==0 and prev_hr==0:
                # minute=60
                hrs=24
            if hrs==0:
                hrs=0
            return (hrs*60)+minute
        for i in timePoints:
            lst.append(conversion(i))
        maxi=999999
        lst.sort()
        for i in range(1,len(lst)):
            if abs(lst[i-1]-lst[i])<maxi:
                maxi=abs(lst[i-1]-lst[i])
        # lst=lst[::-1]
        # print(lst)
        circular=(1440-lst[-1])+lst[0]
        return min(maxi,circular)
class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        while num>0:
            if num>=1000:
                res+="M"
                num=num-1000
            elif num>=900:
                res+="CM"
                num=num-900
            elif num>=500:
                res+="D"
                num=num-500
            elif num>=400:
                res+="CD"
                num=num-400
            elif num>=100:
                res+="C"
                num=num-100
            elif num>=90:
                res+="XC"
                num=num-90
            elif num>=50:
                res+="L"
                num=num-50
            elif num>=40:
                res+="XL"
                num=num-40
            elif num>=10:
                res+="X"
                num=num-10
            elif num>=9:
                res+="IX"
                num=num-9
            elif num>=5:
                res+="V"
                num=num-5
            elif num>=4:
                res+="IV"
                num=num-4
            else:
                res+="I"
                num=num-1
        return res
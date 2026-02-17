class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn<9:
            result=[]
            for hr in range(12):
                for minute in range(60):
                    hr_led=bin(hr).count('1')
                    minute_led=bin(minute).count('1')
                    
                    if hr_led+minute_led==turnedOn:
                        result.append(f"{hr}:{minute:02d}")
            return result
        else:
            return []
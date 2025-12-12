class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events_sorted = sorted(events, key=lambda e: (int(e[1]), 0 if e[0] == 'OFFLINE' else 1))

        mentions=[0]*numberOfUsers
        off_until=[0]*numberOfUsers
        online=[True]*numberOfUsers
        
        for etype,timestamp,data in events_sorted:

            for i in range(numberOfUsers):
                if not online[i] and int(timestamp)>=off_until[i]:
                    online[i]=True
                    off_until[i]=0

            if etype=='OFFLINE':
                user=int(data)
                online[user]=False
                off_until[user]=int(timestamp)+60

            else:
                if data=="ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif data=="HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    ids=data.split()
                    for i in ids:
                        a=int(i[2:])
                        mentions[a]+=1

        return mentions
                
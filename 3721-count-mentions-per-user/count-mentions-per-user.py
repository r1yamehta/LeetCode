class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events_sorted = sorted(events, key=lambda e: (int(e[1]), 0 if e[0] == 'OFFLINE' else 1))

        mentions=[0]*numberOfUsers
        off_until=[0]*numberOfUsers
        online=[True]*numberOfUsers
        
        for event in events_sorted:
            etype=event[0]
            timestamp=int(event[1])
            data=event[2]

            for i in range(numberOfUsers):
                if not online[i] and timestamp>=off_until[i]:
                    online[i]=True
                    off_until[i]=0

            if etype=='OFFLINE':
                user=int(data)
                online[user]=False
                off_until[user]=timestamp+60

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
                
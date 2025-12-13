class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        category = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {cat: i for i, cat in enumerate(category)}
        output = []
        for i in range(len(code)):
            if not isActive[i]:
                continue
            if businessLine[i] not in order:
                continue
            if not code[i]:
                continue

            if not re.fullmatch(r"[A-Za-z0-9_]+", code[i]):
                continue
            output.append((order[businessLine[i]], code[i]))

        output.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in output]



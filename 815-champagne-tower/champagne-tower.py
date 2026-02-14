class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        water=[poured]
        for row in range(1,query_row+1):
            new_water=[0.0] * (row+1)
            for glass in range(len(water)):
                overflow=max(0,water[glass]-1.)

                #left side
                new_water[glass] += overflow/2.
                new_water[glass+1] += overflow/2.
            water=new_water

        return min(1.0,water[query_glass])

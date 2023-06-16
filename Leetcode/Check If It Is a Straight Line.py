class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        flag = True

        def slopeFunction(x1,y1,x2,y2):
            if (x2-x1) == 0:
                slope = "infinity"
            else:
                slope = ((y2-y1)/(x2-x1))
            
            return slope

        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        slope = slopeFunction(x1,y1,x2,y2)

        for i in range(0,len(coordinates)-1):
            x1 = coordinates[i][0]
            y1 = coordinates[i][1]
            x2 = coordinates[i+1][0]
            y2 = coordinates[i+1][1]

            thisSlope = slopeFunction(x1,y1,x2,y2)

            if thisSlope != slope:
                flag = False

        return flag
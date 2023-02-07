class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        left = {"north":"west","west":"south","south":"east","east":"north"}
        right = {"north":"east","west":"north","south":"west","east":"south"}
        go = {"north":[0,1],"south":[0,-1],"east":[1,0],"west":[-1,0]}
        
        face = "north"
        position = [0,0]
        for instruction in instructions:
            if instruction == "L":
                face = left[face]
            elif instruction == "R":
                face = right[face]
            else:
                position[0] += go[face][0]
                position[1] += go[face][1]
                
        if position == [0,0] or face != "north":
            return True
        return False
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # + = right
        # - = left
        # smallest asteroid explode, if equal, then both
        res = []

        for asteroid in asteroids:
            
            # different direction
            while res and asteroid < 0 and res[-1] > 0:
                comp = abs(res[-1]) - abs(asteroid)
                
                # equal, both explode
                if comp == 0:
                    res.pop()
                    break
                # existing explodes
                elif comp < 0:
                    res.pop()
                # ours explodes
                elif comp > 0:
                    break
            
            # same direction
            else:
                res.append(asteroid)
            
        return res


                
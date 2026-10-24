class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:
                comp = abs(asteroid) - abs(st[-1])

                # ours get crushed
                if comp < 0:
                    break
                # crush the existing
                elif comp > 0:
                    st.pop()
                # we both get crushed
                else:
                    st.pop()
                    break
            else:
                st.append(asteroid)
        
        return st
            

                
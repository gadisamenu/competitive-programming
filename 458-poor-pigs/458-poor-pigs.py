class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rnd = minutesToTest//minutesToDie       
        return ceil(log(buckets,rnd+1))
      
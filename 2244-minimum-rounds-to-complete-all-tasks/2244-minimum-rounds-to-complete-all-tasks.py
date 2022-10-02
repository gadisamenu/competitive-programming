class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count_tsk_dft = Counter(tasks)
        _round = 0
        for task in count_tsk_dft:
            cur_rnd = 0
            cur_rnd = count_tsk_dft[task]// 3
            v= count_tsk_dft[task]%3
            if v > 0:
                if v == 1 and  not cur_rnd: return -1
                cur_rnd += 1
                     
            _round += cur_rnd
        
        return _round
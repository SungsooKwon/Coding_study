def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums))

    def get_rank(count):
        if count >= 2:
            return 7 - count
        else:
            return 6
        
    best = get_rank(match_count + zero_count)
    worst = get_rank(match_count)
    
    return [best, worst]
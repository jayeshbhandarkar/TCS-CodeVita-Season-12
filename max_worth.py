def cal_worth(str):
    return sum(ord(char) - ord('a') + 1 for char in str)

def max_worth(num_str, num_cont, str_lst, str_cst, contradiction, budget):
    str_worth = [cal_worth(s) for s in str_lst]
    
    conflict = [0] * num_str
    str_idx = {s: i for i, s in enumerate(str_lst)}
    for s1, s2 in contradiction:
        i1, i2 = str_idx[s1], str_idx[s2]
        conflict[i1] |= (1 << i2)
        conflict[i2] |= (1 << i1)
    
    sort_str = sorted(range(num_str), key=lambda i: -str_worth[i]/str_cst[i])
    
    def is_valid(mask):
        for i in range(num_str):
            if mask & (1 << i):
                if mask & conflict[i]:
                    return False
        return True
    
    best_worth = 0
    def backtrack(pos, curr_mask, curr_cost, curr_worth):
        nonlocal best_worth
        
        if curr_cost > budget:
            return
        
        best_worth = max(best_worth, curr_worth)
        
        remaining_worth = sum(str_worth[sort_str[i]] 
                            for i in range(pos, num_str)
                            if curr_cost + str_cst[sort_str[i]] <= budget)
        if curr_worth + remaining_worth <= best_worth:
            return
            
        for i in range(pos, num_str):
            idx = sort_str[i]
            new_cost = curr_cost + str_cst[idx]
            if new_cost > budget:
                continue
                
            new_mask = curr_mask | (1 << idx)
            if curr_mask & conflict[idx]:
                continue
                
            backtrack(i + 1, new_mask, new_cost, 
                     curr_worth + str_worth[idx])
    
    backtrack(0, 0, 0, 0)
    return best_worth

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    num_str, num_cont = map(int, data[0].split())
    str_lst = data[1].strip().split()
    str_cst = list(map(int, data[2].strip().split()))
    contradiction = [tuple(line.strip().split()) for line in data[3:3 + num_cont]]
    budget = int(data[3 + num_cont].strip())
    
    ans = max_worth(num_str, num_cont, str_lst, str_cst, contradiction, budget)
    print(ans, end="")

if __name__ == "__main__":
    main()
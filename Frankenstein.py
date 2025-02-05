def min_orbs(recipes, target):
    memo = {}

    def cal_orbs(potion):
        if potion not in recipes:
            return 0
        
        if potion in memo:
            return memo[potion]
        
        total_orbs = float('inf')

        for components in recipes[potion]:
            orb_count = sum(cal_orbs(ingredient) for ingredient in components) + (len(components) - 1)
            total_orbs = min(total_orbs, orb_count)
        
        memo[potion] = total_orbs
        return total_orbs

    return cal_orbs(target)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    N = int(data[0])
    recipes = {}

    for i in range(1, N + 1):
        line = data[i]
        potion, components = line.split('=')
        components_list = components.split('+')
 
        if potion not in recipes:
            recipes[potion] = []
        recipes[potion].append(components_list)

    targ_potion = data[N + 1]
    
    result = min_orbs(recipes, targ_potion)
    print(result, end="")

if __name__ == "__main__":
    main()
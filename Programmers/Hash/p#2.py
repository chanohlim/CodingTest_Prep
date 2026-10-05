def solution(nums):
    answer = 0
    pokemon = set()
    
    k = len(nums) // 2
    
    for n in nums:
        pokemon.add(n)
        
    pokemon = list(pokemon)
    
    if len(pokemon) > k:
        return k
    else:
        return len(pokemon)
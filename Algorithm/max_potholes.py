def max_potholes(L1 : str, L2 : str) -> int:
    
    # assert isinstance(L1) and isinstance(L2)
    
    l = len(L1)
    max_potholes = 0
    
    converted_L1, converted_L2 = [], []
    
    forward_repair = l
    backward_repair = l
    
    temp = l
    x = 0
    y = 0
    
    converted_L1 = [1 if char == "X" else 0 for char in L1]
    converted_L2 = [1 if char == "X" else 0 for char in L2]
    
    if sum(converted_L1) == l or sum(converted_L2) == l:
        return l
    
    for i in range(l):
        temp -= converted_L1[i]
        x = converted_L1[i - 1] if i > 0 else 0
        
        # forward_repair = sum(converted_L1[i + 1 :]) + sum(converted_L2[:i])
        # backward_repair = sum(converted_L1[:i]) + sum(converted_L2[i + 1 :])
        
        forward_repair = forward_repair - converted_L1[i - 1] + (converted_L2[i - 1])
        backward_repair = backward_repair - converted_L2[i - 1] + (converted_L1[i - 1])
        
        local_max = max(forward_repair, backward_repair)
        
        print(forward_repair, backward_repair, local_max)
        
        if local_max > max_potholes:
            max_potholes = local_max
            
    return max_potholes

# Example usage
L1 = "X..X..X"
L2 = "XXXXX.X"
print(max_potholes(L1, L2))
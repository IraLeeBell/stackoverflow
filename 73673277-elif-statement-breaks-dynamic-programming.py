# This is the Robber problem where a thief cannot steal from two adjacent homes but wants to maximize loot.

# Example: input: arr = [2, 10, 3, 6, 8, 1, 7] output: 25 explanation: The greatest amount of money that a robber can get is 25, by the stealing the house 1, 4, and 6 (arr[1]+arr[4]+arr[6] = 10+8+7 = 25)

# The below is what the OP claims is the working code.

def rob(arr):
    arr = tuple(arr)
    memory = {} 
    
    def helper(i=0):
        if i >= len(arr):
            return 0 
            
        if i not in memory:
            steal = arr[i] + helper(i+2)
            skip = helper(i+1)
            memory[i] = max(steal, skip)
        
        return memory[i]
    
    return helper()

# I added these lines and the result is in fact 25
make_it_so = rob([2, 10, 3, 6, 8, 1, 7])
print(make_it_so)

# Then the OP said that the below code isn't working:

def rob2(arr):
    arr = tuple(arr)
    memory = {} 
    
    def helper(i=0):
        if i >= len(arr):
            return 0 
        
        # the below code doesn't work because it tries to find memory[0] which doesn't exist
        # elif memory[i]
        # you can assign position zero above to anumber and will get a different error (e.g. memory ={3}), but then change the set to a list to actually get the result of 3 (e.g. memory = [3]). This provides that the elif condition OP wrote is the problem. OP can use the get() method instead.. like shown below
        
        elif memory.get(i):
            return memory[i]
            
        else:
            steal = arr[i] + helper(i+2)
            skip = helper(i+1)
            memory[i] = max(steal, skip)
            return memory[i]
    
    return helper()


make_it_so = rob2([2, 10, 3, 6, 8, 1, 7])
print(make_it_so)

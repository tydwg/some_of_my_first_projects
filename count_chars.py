def count_chars(inp_str):
    results = {} # {}
    # if key (character) exists
    # increase counter 1 unit 
    # else create an item with key is character and 
    # value is 1
    for i in inp_str:
        if results.get(i):
            results[i] += 1
        else:
            results[i] = 1 
    return results

import numpy as np
from time import time
def polynomial_hash(s):
	hash_value = 0
	for i in range(len(s)):
		hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
	return hash_value
def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
	return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)


def rabin_karp_algorithm_multiple_2(patterns, text):
   

    p = len(patterns[0])  
    t = len(text)
    b = 26  
   

    pattern_hashes = [polynomial_hash(pattern) for pattern in patterns]
    text_hash = polynomial_hash(text[:p])

    occurrences = [0] * len(patterns)

    for i in range(t - p + 1):
        if i > 0:
            text_hash = polynomial_rolling_hash(text_hash, text[i - 1], text[i + p - 1], p)

        for j, pattern_hash in enumerate(pattern_hashes):
            if pattern_hash == text_hash:
                occurrences[j] += 1

    return occurrences
def rabin_karp_algorithm_multiple(pattern, text):
    occurences = [0 for i in range(len(pattern))]
    
    for i in range(len(pattern)):
        pattern_len= len(pattern[i])
        pattern_hash = polynomial_hash(pattern[i])
        current_string = text[:pattern_len]
        new_text= [char for char in text[pattern_len:]]
        previous_hash= polynomial_hash(current_string)
        if (pattern_hash== previous_hash):
                occurences[i]+=1
        for char in text[pattern_len:]:
            next_char = new_text.pop(0)
            previous_hash= polynomial_rolling_hash(previous_hash,current_string[0],next_char, pattern_len)
            if (pattern_hash== previous_hash):
                occurences[i]+=1
            current_string= current_string[1:]+ char
    return occurences
            
def brute_force_algorithm_multiple(patterns, text):
    occurrences = [0] * len(patterns)
    
    for i, pattern in enumerate(patterns):
        pattern_len = len(pattern)
        text_len = len(text)
        
        for j in range(text_len - pattern_len + 1):
            if text[j:j + pattern_len] == pattern:
                occurrences[i] += 1
    
    return occurrences
			
			
			
		 
        
	
    


patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEFABCABCCDE'*100000


# t1 = time()
# print(brute_force_algorithm_multiple(patterns, text))
# t2= time()
# print(rabin_karp_algorithm_multiple_2(patterns, text))
# t3 = time()

# print(f"Function vers1 takes {t2 - t1:.6f} seconds")
# print(f"Function vers1 takes {t3 - t2:.6f} seconds")
def rabin_karp_algorithm_2D(pattern, text):
    occurences= 0
    pattern_len= len(pattern[0])
    text_len= len(text)

    arr_hash_pattern = []
    for row in pattern:
         arr_hash_pattern.append(polynomial_hash(row))
    pattern_hash = 0
    for i in range(len(arr_hash_pattern)):
         pattern_hash+= arr_hash_pattern[i]* (10**(len(arr_hash_pattern)-i-1))
    
    text_hash= []
    for i in range(len(text)):
         mini_text_hash = []
         for j in range(len(text[0])- pattern_len+1):
              mini_text_hash.append(polynomial_hash(text[i][j:j+pattern_len]))

         text_hash.append(mini_text_hash)
              
    for i in range(text_len-len(pattern)+1):
         for j in range(len(text_hash[0])):
              
              text_hash_value= 0
              for k in range(len(pattern)):
                   text_hash_value+= text_hash[i+k][j] * (10**(len(pattern)-k-1))
              print(text_hash_value, pattern_hash)
              if text_hash_value == pattern_hash:
                   occurences +=1 
    return occurences
                   
              


t0 = time()

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']*1000
print(rabin_karp_algorithm_2D(pattern, text))

t1= time()
print("Run time", t1-t0)


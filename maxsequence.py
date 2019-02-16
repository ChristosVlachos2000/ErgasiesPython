from sys import maxsize 
  
# Function to find the maximum contiguous subarray 
# and print its starting and telos index 
def maxSequence(a,size): 
  
    max_mexri_stigmhs = -maxsize - 1
    max_teliko = 0
    arxi = 0
    telos = 0
    s = 0
  
    for i in range(0,size): 
  
        max_teliko += a[i] 
  
        if max_mexri_stigmhs < max_teliko: 
            max_mexri_stigmhs = max_teliko 
            arxi = s 
            telos = i 
  
        if max_teliko < 0: 
            max_teliko = 0
            s = i+1
  
    print (max_mexri_stigmhs) 
    j = arxi
    while j <= telos:
        print ("[", a[j], telos='' "]" )
        j = j + 1
     











       






































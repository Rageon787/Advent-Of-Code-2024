# Given 1000 reports (where each report is represted as a list of integers) 
# A report is safe if:
    # Increasing or decreasing, and  
    # The absolute Difference between adjacent elements is in the range [1, 3]
# Otherwise unsafe  
# Hence, find the number of safe reports 

def check(report):
    incr, decr = True, True                         # Booleans for whether a sequence increasing or decreasing 
     
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]            # Difference between adjacent elements 
        if diff < 1 or diff > 3:                    # If sequence is increasing but diff is in range (-inf, 1) U (3, inf)
            incr = False 
        if diff > -1 or diff < -3:                  # If sequence is decreasing but dif is in the range (-inf, -3) U (-1, inf)
            decr = False
    return incr or decr 
    
f = open("input.txt", "r")                   
reports = []                                        


for line in f:
    reports.append([int(x) for x in line.split()])  

safe = 0                                             
for report in reports:                               
    ok = False
    for i in range(len(report)):                    # for each i, remove A[i] and check if it satisfies the invariant
        ok |= check(report[0:i] + report[i+1:])     # Check if the array excluding A[i] satisfies the invariant  
    if ok:                                           
        safe += 1

    
print(safe)


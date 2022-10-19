
def problem1(l):
    for i in range(len(l) - 1):
    #accsess the length of the list 
        if l[i] == 7:
            if l[i + 1] ==7:
                return True 
    return False

def problem2(l):
    #excludes everything after a certain prime number in the list 
    total = 0
    for elem in l:
        if elem == 2 or elem == 3 or elem == 5 or elem == 7 or elem == 11:
            break
        #because of the nature of break technically we don't need else
        else:
            total = total + elem
    return total

def problem3(l):
    total = 0
    found2 = False
    
    for elem in l:
        if elem == 2:
            found2 = True

        if found2 == False:
            total = total + elem
            
        if found2 == True:
            if elem == 3:
                found2 == False
                
  
    return total

def main():
    l = [1, 2, 3, 7, 7]
    print(problem1(l))
    
    l = [1, 4, 2, 3, 6]
    print(problem2(l))

    l = [1, 3, 4, 2, 3, 8]
    print(problem3(l))
    
    
if __name__ == "__main__":
    main()

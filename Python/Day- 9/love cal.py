def calculate_love_score(name1, name2):
    list1= list(name1)
    list2= list(name2)
    
    count1 = 0
    count2 = 0
    
    n1=len(list1)
    n2=len(list2)
    
    for i in range(n1):
        if list1[i] in "trueloveTRUELOVE":
            count1 +=1 
            
    for i in range(n2):
        if list2[i] in "trueloveTRUELOVE":
            count2 += 1 
            
    score= (str(count1)+str(count2))
    return score
    
name1= input("Enter your name: ")
name2= input("Enter your patner's name: ")

print(calculate_love_score(name1,name2))
        

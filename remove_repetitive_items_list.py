# Python function to remove repetitive items from a list
def remv_rstring(lis):
    for i in lis:
        c = lis.count(i)
        if c > 1:
            while c != 1:
                lis.remove(i)
                c -= 1
    else:
        print(lis)
        
        
   
lis = [1, 2, 3, 2, 3, 4, 4, 4, 5, 5]    
remv_rstring(lis)
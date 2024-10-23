# import string
# def check_word(word):
#     for c in range(len(word)):
#         hyphen=0
#         punc= 0
#         if word == "!" or word == '.' or word == ',':
#             return True
#         else:
#             if word[c] in ["0","1","2","3","4","5","6","7","8","9"]:
#                 return False
#             if hyphen <= 1:
#                 if word[c] == "-":
#                     if c == 0:
#                         return False
#                     if c == len(word)-1:
#                         return False
#                     if word[c-1] not in "abcdefghijklmnopqrstuvwxyz":
#                         return False

#                     else:
#                         if word[c+1] not in "abcdefghijklmnopqrstuvwxyz":
#                             return False
#                     hyphen +=1
#             else:
#                 return False
                
#             if punc <=1:
#                 if word[c] in ['!','.',',']:
#                     if c==0:
#                         return False
#                     if word[c-1] not in "abcdefghijklmnopqrstuvwxyz":
#                         return False
#                     if c!=len(word)-1:
#                         return False
#                 punc += 1
#             else:
#                 return False
        
#     # print(f"{word} is correct")
#     return True
                
            
                
        
# string= input()

# bits = string.split()
# total=0
# for x in bits:
#     if (check_word(x)):
#         total += 1
# print(total)


#----------------------------------------------

maximum=0
def pos(intervals:list,start):
    global maximum
    all_possi=0
    max=0
    for i in range(start,len(intervals)):
        for j in range(start,len(intervals)):
            if i != j:
                if intervals[i][1]<= intervals[j][0]:
                    max+=1
                    if pos(intervals,j):
                        
                        maximum += 1
                        return True
                    
    return False
                
    


clubs=int(input())
intervals=[]
for _ in range(clubs):
    inter = intervals.append([int(a) for a in input().split()])
pos(inter,0)
print (maximum)
    

      
    
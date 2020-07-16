
import random
epoch = 1000


'''
融合怪进化出圣盾剧毒的概率
'''
def each_times(evols):
    s = 0
    for ep in range(epoch):
        a = 0
        b = 0
        #print(random.randint(1,7))
        for evl in range(evols):
            
            t = random.randint(1,7) 
            if t == 1:
                a = 1
            if t == 2:
                b = 1
            if a+b == 2:
                s+=1
                break
    return s/epoch
print("========================")
print("融合怪进化出圣盾剧毒的概率")

for i in range(1,10):
     print(i,":",each_times(i))   

def each_choise(evols):
    s = 0
    for ep in range(epoch):
        a = 0
        b = 0
        #print(random.randint(1,7))
        for evl in range(evols):
            
            l= random.sample(list(range(7)),3)
            
            if 1 in l and a == 0:
                a = 1
                continue
            if 2 in l and b == 0:
                b = 1
               
                    
            
        if a+b == 2:
            s+=1
            
    return s/epoch
print("========================")
print("巨壳龙进化出圣盾剧毒的概率")

for i in range(1,10):
     print(i,":",each_choise(i))    

'''
三连找巨壳龙概率
共14
野兽：4
鱼人：1
龙：  2
机械：2
海盗：2
恶魔：1
融合怪、猎妈
'''
def find(evols):
    s = 0
    for ep in range(epoch):

        cnt = 0
        #print(random.randint(1,7))
        for evl in range(evols):

            l = random.sample(list(range(1,13)),k = 3)
            #print(l)
            if 1 in l:
                cnt+=1
            if cnt >= 2:
                s+=1
                break
      
       
    return s/epoch
 
print("========================")
print("三连找巨壳龙概率")
# print("ban野兽")
# for i in range(1,10):
#     prob = 1-(7/10)**i
#     print(i,"次三连:",prob)
print("ban恶魔")
for i in range(1,10):
    prob = 1-(10/13)**i
    print(i,"次三连:",prob)
print("ban龙、机械、海盗")
for i in range(1,10):
    prob = 1-(9/12)**i
    print(i,"次三连:",prob)
print("========================")
print("三连找两条巨壳龙概率")
for i in range(1,10):
     print(i,"次三连:",":",find(i))   

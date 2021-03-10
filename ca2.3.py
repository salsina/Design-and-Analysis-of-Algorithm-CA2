
def is_k_similar(list1,list2,k):
    num = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            num +=1
    if num <= k:
        return True
    return False


def is_in_dict(s,dictionary):
    list1 = s.split()
    if len(dictionary) == 0:
        return False
    for i in dictionary:
        for j in range(len(list1)):
            if i[j] != list1[j]:
                return False
    return True 
def list_to_string(l):
    s = ""
    for i in l:
        s +=str(i)+" "
    return s


n_l = [int(x) for x in input().split()]
n = n_l[0]
l = n_l[1]
donbale = [int(x) for x in input().split()]
num_of_qs = int(input())
questions = []
for i in range(num_of_qs):
     inp = int(input())
     questions.append(inp)
     
     
zir_donbale = []
i=0
while (i + l) <= n:
   zir_donbale.append(donbale[i:i+l])
   i+=1
   
for k in range(len(questions)):
    answer = ""
    dictionary = {}
    if questions[k] == l:
        for i in range(n-l+1):
            answer += str(n-2) + " "
    else:
        for i in range(len(zir_donbale)):
            ans = 0
            data = list_to_string(zir_donbale[i])
            if not is_in_dict(data , dictionary):
                for j in range(len(zir_donbale)):
                    if i != j:
                        if is_k_similar(zir_donbale[i],zir_donbale[j],questions[k]) == True:
                            ans +=1
                dictionary[data] = ans
            else:
                ans = dictionary[data]
            answer += str(ans)+" "
    print(answer)
                    
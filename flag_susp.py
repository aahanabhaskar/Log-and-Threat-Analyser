logs=[]
with open("logs.txt","r") as f:
    data=f.readlines()
    for i in data:
        logs.append(i.strip())
    # print(logs)
def make_dict(logs):
    sus={}
    for l in logs:
        if "Login Failed by" in l:
            rev=l.split(" ")
            sus[rev[6]]=sus.get(rev[6],0)+1
    print(sus)
    return sus
c=make_dict(logs)
print(c)
def flag_susp(c):
    for u in c:
        if c[u]>=5:
            print(u,"Is Suspicious")
flag_susp(c)
import random
IP_ad=["198.90.2.x","96.78.250.x","84.65.x.121","59.33.x.123","45.69.84.x","35.89.20.x","35.x.98.230","79.51.x.0"]
day=['Nov 2','Nov 3']
ti=['13:45:56','01:23:12','4:08:49','15:42:32','09:47:32']
att_ip=['12.45.67.x','98.x.123.49']
logs=[]
#Where att_ip refers to suspicious IP addresses and IP_ad refers to valid ip address; 4 total cases have  been taken into account 
#1 is where successful login due to valid ip,2 is failed login due to att IP,3 is accidental failed login by valid IP and 4 is good login by sus IP

def log_gen():
    for i in range(200):
        ip=random.choice(IP_ad)
        dat=random.choice(day)
        tim=random.choice(ti)
        log_entry=dat+" "+tim+" "+"Login Success by"+" "+ip
        logs.append(log_entry)
    for j in range(20):
        dat=random.choice(day)
        tim=random.choice(ti)
        ipno=random.choice(att_ip)
        log_entry=dat+" "+tim+" "+"Login Failed by"+" "+ipno
        logs.append(log_entry)
    for k in range(4):
        dat=random.choice(day)
        ip=random.choice(IP_ad)
        tim=random.choice(ti)
        log_entry=dat+" "+tim+" "+"Login Failed by"+" "+ip
        logs.append(log_entry)
    for w in range(2):
        dat=random.choice(day)
        tim=random.choice(ti)
        ipno=random.choice(att_ip)
        log_entry=dat+" "+tim+" "+"Login Success by"+" "+ipno
        logs.append(log_entry)
    return logs
log_gen()
random.shuffle(logs)
def sortlogs_bydate(logs):
    lognew=[]
    for s in logs:
        rem=s.split(" ")
        if rem[1]=='2':
            lognew.append(s)
        else:
            continue
    for o in logs:
        rem1=o.split(" ")
        if rem1[1]=='3':
            lognew.append(o)
        else:
            continue
    return lognew
val=sortlogs_bydate(logs)
# print(val)
def print_logs(val):
    for p in val:
        print(p)
        print(" ")
# print_logs(val)
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
def log_textfile(lognew):
    fileob=open("logs.txt","w")
    for i in lognew:
        # fileob.write(i+"\n")
        fileob.write(i)
    fileob.close()
log_textfile(val)

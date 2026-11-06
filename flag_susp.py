import csv
def write_report(counts, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Failed Attempts", "Status"])
        for ip, count in counts.items():
            if count >= 5:
                status = "Suspicious"
            else:
                status = "OK"
            writer.writerow([ip, count, status])
logs=[]
file=input("Enter file name with extension: ")
def read_logs(file):
    try:
        with open(file,"r") as f:
            data=f.readlines()
            for i in data:
                logs.append(i.strip())
    # print(logs)
    except FileNotFoundError:
        print("File is either missing or misspelt")
        return []
    # return logs
read_logs(file)
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
            print(u,"is Suspicious")
flag_susp(c)
write_report(c, "log_report.csv")
print("Report saved to log_report.csv")
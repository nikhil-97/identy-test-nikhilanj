with open("dataq2.log","r") as f:
	s = f.readlines()
s = [i.strip("\n") for i in s]
bal = 0
for t in s:
	trans,amt = t.split(' ')
	amt = int(amt)
	
	if(trans=='D'):
		bal = bal + amt
	elif(trans=='W'):
		bal = bal - amt

print("Available balance : ",bal)
with open("dataq2.log","a") as f:
	f.write("\nAvailable balance : %s\n"%str(bal))
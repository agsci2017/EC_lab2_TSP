import sys
import copy

f=open("TSP_template.py","r")

s = f.read()

bash = open("best.sh","w")

for i in range(0,16):
	for j in range(0,16):
		
		tmps=copy.deepcopy(s)
		tmps=tmps.replace("SEED1",str(i))
		tmps=tmps.replace("SEED2",str(j))
		
		ftmp = open("TSP_seed_"+str(i)+"_"+str(j)+".py","w")
		ftmp.write(tmps)
		ftmp.close()
		
		bash.write("python3 TSP_seed_{}_{}.py &\n".format(i,j))
		
		if (-2+i+j*14)%5==0:
			bash.write("wait\n")

bash.write("wait\n")


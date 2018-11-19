import sys
import copy

f=open("TSP_template.py","r")

s = f.read()

bash = open("best.sh","w")

for i in range(0,17):
		
	tmps=copy.deepcopy(s)
	tmps=tmps.replace("SEED1",str(i))
	tmps=tmps.replace("SEED2",str(i))
	
	ftmp = open("TSP_seed_"+str(i)+".py","w")
	ftmp.write(tmps)
	ftmp.close()
	
	bash.write("python3 TSP_seed_{}.py &\n".format(i))
	
	if (i+1)%6==0:
		bash.write("wait\n")

bash.write("wait\n")


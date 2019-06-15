import sys
import re
registers=("eax","ebx","ecx","edx","edi","esp","ebp")
#mov add sub lea xor
def istemp(oprand):
	return "ebp-" in oprand and "+" in oprand
def used_rightvalue(inst,oprand):
	if oprand not in inst[1]:
		return False
	if len(inst[1])==1:
		return True
	if inst[0] in ("add","sub","xor","jg","jge","je","jne","jle","jl"):
		return True
	if inst[0] in ("mov","lea"):
		return inst[1][1]==oprand
	return False
def used_leftvalue(inst,oprand):
	if oprand not in inst[1]:
		return False
	if len(inst[1])==1:
		return True
	if inst[0] in ("add","sub","xor","jg","jge","je","jne","jle","jl"):
		return False
	if inst[0] in ("mov","lea"):
		return inst[1][0]==oprand
	return True
	
def isreg(regname):
	return regname in registers
def opt_block(block):
	if block == []:
		return
	tmp=[_.strip().split(" ",1) for _ in block]
	tmp=[(_[0],_[1].split(",") if len(_)>1 else []) for _ in tmp]
	i,j=0,1
	res=[tmp[i]]
	while j<len(tmp):
		P=tmp[i]
		N=tmp[j]
		#print(P,N)
		#mov [addr],eax
		#mov eax,[addr]
		if P[0]=="mov" and  N[0]=="mov" and isreg(P[1][1]) and P[1][0]==N[1][1]:
			if P[1][1]==N[1][0]:
				#print("\t;")
				j+=1
			else:
				res.append((N[0],[N[1][0],P[1][1]]))
				i,j=j,j+1
		#mov [addr],eax
		#push [addr]
		elif P[0]=="mov" and N[0]=="push" and P[1][0]==N[1][0] and isreg(P[1][1]):
			res.append((N[0],[P[1][1]]))
			i,j=j,j+1
		else:
			res.append(N)
			i,j=j,j+1
	#print(res)
	#for _ in res:
	#	print("\t{} {}".format(_[0],",".join(_[1])))
	tmp=[]
	for i in range(len(res)):
		P=res[i]
		if len(P[1])<=1 or P[0][0]=="j" or istemp(P[1][0]) == False:
			tmp.append(P)
			continue
		flag=False# add if flag is True
		for j in range(i+1,len(res)):
			if used_rightvalue(res[j],P[1][0]):
				flag=True
				break
			if used_leftvalue(res[j],P[1][0]):
				break
		if flag:
			tmp.append(P)
		else:
			pass
			#print("\t;")
	for _ in tmp:
		print("\t{} {}".format(_[0],",".join(_[1])))
def opt_code(codesegment):
	buf=[]
	for _ in codesegment:
		if _=="":
			continue
		if _[0] == "\t":
			buf.append(_)
		if _[0] != "\t" or _[:2] == "\tj":
			opt_block(buf)
			buf=[]
		if _[0] != "\t":
			print(_)
def optimize(prog):
	st=prog.find("code segment use32\nassume cs:code,ds:data\n")+len("code segment use32\nassume cs:code,ds:data\n")
	ed=prog.find("\ncode ends")
	print(prog[:st])
	opt_code(prog[st:ed].split("\n"))
	print(prog[ed:])
	return
if __name__=="__main__":
	try:
		f=open(sys.argv[1],"r")
		prog=f.read().strip()
		f.close()
	except:
		prog=[]
		while True:
			try:
				prog.append(input())
			except:
				break
		prog="\n".join(prog)
	optimize(prog)
	# st=prog.find("code segment use32\nassume cs:code,ds:data\n")+len("code segment use32\nassume cs:code,ds:data\n")
	# ed=prog.find("\ncode ends")
	# print(prog[:st])
	# opt_code(prog[st:ed].split("\n"))
	# print(prog[ed:])

import sys
type_datasegment={"int":"dd","char":"db","int*":"dd","float":"dd","double":"dq"}
type_codesegment={"int":"dword ptr ","char":"byte ptr ","int*":"dword ptr "}
jcondition={">":"jg",">=":"jge","==":"je","!=":"jne","<=":"jle","<":"jl"}
revop={">":"<=",">=":"<","==":"!=","!=":"==","<=":">","<":">="}
brspace=8
label_index=0
func_name=""
reserve_size=0
def new_label():
	global label_index
	label_index+=1
	return func_name+"_masm32_L"+str(label_index)
def parse_data(data):
	assert(data[:13]=="global_var = ")
	print("data segment use32")
	data=eval(data[13:])
	for _ in data:
		if _[3]==None:#mormal global var
			print("\t{} {}".format("data_"+str(_[1]),type_datasegment[_[0]]),end=" ")
			if _[2][0]:#array
				print(_[2][1],"dup(0)")
			else:
				print("0")
		else:#format string
			count_end_0ah=0
			strctx=str(_[3],encoding="ascii").strip("\"")
			assert(len(strctx)>0)
			while len(strctx)>1 and strctx[-2:]=="\\n":
				count_end_0ah+=1
				strctx=strctx[:-2]
			if len(strctx)==0:
				fmt=print(",".join(["0ah,0dh"]*count_end_0ah))
			else:
				fmt=",0ah,0ah,".join(["\"{}\"".format(_) for _ in strctx.split("\\n")])+",0ah,0dh"*count_end_0ah
			print("\t{} {} {}".format(str(_[1]),"db",fmt+",0,'$'"))
	print("data ends")
	return
def get_oprand(oprand):
	if type(oprand)==int:
		return oprand
	assert(len(oprand)==2)
	assert(len(oprand[1])==3)
	if oprand[1][0]==True:#isglobal or temp
		if oprand[1][2]==None:#global
			return type_codesegment[oprand[1][1]]+"[{}]".format("data_"+oprand[0])
		elif oprand[1][2]>=0:#temp var
			return type_codesegment[oprand[1][1]]+"[ebp-{}+{}]".format(reserve_size,oprand[1][2])
		else:
			assert(False)
	elif oprand[1][0]==False:#para or local var
		if oprand[1][2]>=0:#para
			return type_codesegment[oprand[1][1]]+"[ebp+{}+{}]".format(brspace,oprand[1][2])
		else:#local var
			return type_codesegment[oprand[1][1]]+"[ebp-{}]".format(-oprand[1][2])
	else:
		assert(False)
def parse_inst(inst):
	assert(len(inst)==4)
	if inst[0] in ("+","-"):
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\t{} eax,{}".format("add" if inst[0]=="+" else "sub",get_oprand(inst[2])))
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="*":
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\timul {}".format(get_oprand(inst[2])))
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="%" or inst[0]=="/":
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tcdq")
		print("\tmov ecx,{}".format(get_oprand(inst[2])))
		print("\tidiv ecx")
		print("\tmov {},{}".format(get_oprand(inst[3]),"eax" if inst[0]=="/" else "edx"))
	elif inst[0]==":=":
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="[]:=":
		temp=inst[3].split("[")
		temp[1]=temp[1][:-1]#remove "]"
		temp=[eval(_) for _ in temp]
		destbase=get_oprand(temp[0])
		destoff=get_oprand(temp[1])
		print("\tlea ebx,{}".format(destbase))
		print("\tmov edi,{}".format(destoff))
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tmov dword ptr [ebx+edi*4],eax")
	elif inst[0]==":=[]":
		destbase=get_oprand(inst[1])
		destoff=get_oprand(inst[2])
		print("\tlea ebx,{}".format(destbase))
		print("\tmov edi,{}".format(destoff))
		print("\tmov eax,dword ptr [ebx+edi*4]")
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="(*):=":
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tmov ebx,{}".format(get_oprand(inst[3])))
		print("\tmov dword ptr [ebx],eax")
	elif inst[0]==":=(*)":
		print("\tmov ebx,{}".format(get_oprand(inst[1])))
		print("\tmov eax,dword ptr [ebx]")
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0][0]=="j":
		if inst[0]=="j":
			print("\tjmp {}".format(inst[3]))
		elif inst[0]=="j==" or inst[0]=="j!=":
			print("\tmov eax,{}".format(get_oprand(inst[1])))
			print("\tcmp eax,{}".format(get_oprand(inst[2])))
			print("\t{} {}".format(jcondition[inst[0][1:]],inst[3]))
		else:
			assert(False)
	elif inst[0] in jcondition.keys():
		print("\txor edi,edi")
		print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tcmp eax,{}".format(get_oprand(inst[2])))
		label_end=new_label()
		print("\t{} {}".format(jcondition[revop[inst[0]]],label_end))
		print("\tinc edi")
		print(label_end+":")
		print("\tmov {},edi".format(get_oprand(inst[3])))
	elif inst[0] in ("++","--"):
		print("\t{} {}".format("inc" if inst[0]=="++" else "dec",get_oprand(inst[3])))
	elif inst[0] in ("[]++","[]--"):
		temp=inst[3].split("[")
		temp[1]=temp[1][:-1]#remove "]"
		temp=[eval(_) for _ in temp]
		destbase=get_oprand(temp[0])
		destoff=get_oprand(temp[1])
		print("\tlea ebx,{}".format(destbase))
		print("\tmov edi,{}".format(destoff))
		print("\t{} dword ptr [ebx+edi*4]".format("inc" if inst[0]=="++" else "dec"))
	elif inst[0]==":=(&)":
		print("\tlea eax,{}".format(get_oprand(inst[1])))
		print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="arg":
		if type(inst[1])==tuple and inst[1][1][1]=="char[]":
			print("\tpush offset [{}]".format(inst[1][0]))
		else:
			print("\tpush {}".format(get_oprand(inst[1])))
	elif inst[0]=="call":
		call_name=inst[1]
		if call_name in ("printf","exit","scanf"):
			call_name="crt_{}".format(call_name)
		print("\tcall {}".format(call_name))
		if inst[3]!=None:
			print("\tmov {},eax".format(get_oprand(inst[3])))
	elif inst[0]=="ret":
		if inst[1]!=None:
			print("\tmov eax,{}".format(get_oprand(inst[1])))
		print("\tjmp {}".format(func_name+"_masm32_exit_label"))
	else:
		print(inst)
		assert(False)
def parse_ctx(ctx,para_size):
	print("\tpush ebp")
	print("\tmov ebp,esp")
	if reserve_size==0:
		pass
	elif reserve_size==4:
		print("\tpush ecx")
	else:
		print("\tsub esp,"+str(reserve_size))
	for _ in ctx:
		try:
			inst=eval(_)
		except:#label
			print(_)
		else:
			parse_inst(inst)
	print(func_name+"_masm32_exit_label:")
	if func_name=="main":
		print("\tpush 0")
		print("\tcall crt_exit")
	print("\tmov esp,ebp")
	print("\tpop ebp")
	print("\tretn "+str(para_size))
	return
def parse_func(func):
	print(func[0])
	assert(func[0][-5:]==" proc")
	global func_name,label_index
	label_index=0
	func_name=func[0][:-5]
	assert(func[-2][:12]=="para_size = ")
	para_size=int(func[-2][12:])
	assert(func[-3][:11]=="var_size = ")
	var_size=int(func[-3][11:])
	assert(func[-4][:16]=="max_temp_size = ")
	max_temp_size=int(func[-4][16:])
	#func[1] is local_para list, useless
	#func[-5] is local var list, useless
	global reserve_size
	reserve_size=var_size+max_temp_size
	parse_ctx(func[1:][:-4][1:][:-1],para_size)
	print(func[-1])
def parse_code(code):
	print("code segment use32")
	print("assume cs:code,ds:data")
	for _ in code:
		parse_func([ele.strip() for ele in _.split("\n")])
	print("code ends")
	print("end main")
	return
def parse_prog(prog):
	print(".386")
	print(".model flat,stdcall")
	print("include msvcrt.inc")
	print("includelib msvcrt.lib")
	parse_data(prog[-1])
	parse_code(prog[:-1])
	return 
if __name__ == "__main__":
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
		prog='\n'.join(prog)
	prog=[_.strip() for _ in prog.split(">"*9)]
	parse_prog(prog)

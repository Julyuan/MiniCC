import copy
import queue
import math
import sys

symbol_table = {}

type_size={"int":4,"char":1,"int*":4,"float":4,"double":8}
global_var=[]
local_var=[]
local_para=[]
temp_var_count=queue.PriorityQueue()
max_temp_size=0
label_count=0
label_func=""
type_func=""
string_name=set()
def get_string_name(cstring):
	s="".join(chr(_) if _ in b"qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_0123456789" else "" for _ in cstring)
	if len(s)==0:
		s="QAQ"
	s="a"+s.upper()
	i=0
	while s in string_name:
		s=s+"_"+str(i)
		i+=1
	string_name.add(s)
	return s
def new_temp_var():
	global temp_var_count,max_temp_size
	temp=temp_var_count.get()
	max_temp_size=max(max_temp_size,temp*4)
	if temp_var_count.empty():
		temp_var_count.put(temp+1)
	return ("temp_var_"+str(temp*4),(True,"int",temp*4-4))
def ret_temp_var(var_name):
	if type(var_name)==tuple and type(var_name[0])==str and var_name[0][:9]=="temp_var_":
		temp_var_count.put(int(var_name[0][9:])//4)
	return
def new_label():
	global label_count
	label_count+=1
	return label_func+"_L"+str(label_count)
#		|...
#		|local n-1
#new bp	|local n
#		|ebp
#		|ret addr
#		|para 0
#^		|para 1
#|		|para 2
#old sp	----
#h
def find_addr(expression):#(isglobal or temp,type,byte_baseaddr(origin bp related if local, and meaningless if global))
	if type(expression)!=str:
		return (None,None,None)
	global local_var,local_para,global_var
	for i in range(len(local_var)):
		if local_var[i][1]==expression:
			return (False,local_var[i][0],local_var[i][3])
	for i in range(len(local_para)):
		if local_para[i][1]==expression:
			return (False,local_para[i][0],local_para[i][3])
	for _ in global_var:
		if _[1]==expression:
			return (True,_[0],None)
	# print(local_para)
	print('Semantic Error: Cannot find address for expression:', expression)
	assert(False)
def parse_identifier_expression(identifier_expression):
	assert(identifier_expression[0]=="identifier-expression")
	assert(len(identifier_expression)==2)
	global local_var
	return (identifier_expression[1],find_addr(identifier_expression[1]))
def parse_int_expression(int_expression):
	assert(int_expression[0]=="int-expression")
	assert(len(int_expression)==2)
	return int_expression[1]
def calc_array_index(arrayExpression):
	assert(arrayExpression[0]=="arrayExpression")
	return parse_expression(arrayExpression[2])
def parse_assignExpression(assignExpression):
	assert(assignExpression[0]=="assignExpression")
	#print(assignExpression)
	if assignExpression[1][0]=="identifier-expression":
		left_value=parse_identifier_expression(assignExpression[1])
	elif assignExpression[1][0]=="arrayExpression":
		idx=calc_array_index(assignExpression[1])
	elif assignExpression[1][0]=="removeref":
		assert(assignExpression[1][1][0]=="identifier-expression")
		left_value=(assignExpression[1][1][1],find_addr(assignExpression[1][1][1]))
		#left_value=parse_expression(assignExpression[1])
	else:
		print(assignExpression)
		assert(False)
	right_value1=parse_expression(assignExpression[2])
	if assignExpression[1][0]=="identifier-expression":
		print("\t"+str((":=",right_value1,None,left_value)))
	elif assignExpression[1][0]=="arrayExpression":
		print("\t"+str(("[]:=",right_value1,None,"{}[{}]".format((assignExpression[1][1][1],find_addr(assignExpression[1][1][1])),idx))))
		ret_temp_var(idx)
	elif assignExpression[1][0]=="removeref":
		print("\t"+str(("(*):=",right_value1,None,left_value)))
		ret_temp_var(left_value)
	else:
		assert(False)
	return right_value1
def parse_binary_expression(binary_expression):
	assert(binary_expression[0]=="binary-expression")
	left_value=new_temp_var()
	if binary_expression[1]=="&&" or binary_expression[0]=="||":
		label_temp=new_label()
		label_end=new_label()
		right_value1=parse_expression(binary_expression[2])
		print("\t"+str((":=",right_value1,None,left_value)))
		ret_temp_var(right_value1)
		if binary_expression[1]=="&&":
			print("\t"+str(("j==",left_value,0,label_temp)))
		elif binary_expression[1]=="||":
			print("\t"+str(("j!=",left_value,0,label_temp)))
		right_value2=parse_expression(binary_expression[3])
		print("\t"+str((":=",right_value2,None,left_value)))
		ret_temp_var(right_value2)
		print(label_temp+":")
		print("\t"+str(("j==",left_value,0,label_end)))
		print("\t"+str((":=",1,None,left_value)))
		print(label_end+":")
	else:
		right_value1=parse_expression(binary_expression[2])
		right_value2=parse_expression(binary_expression[3])
		print("\t"+str((binary_expression[1],right_value1,right_value2,left_value)))
		ret_temp_var(right_value1)
		ret_temp_var(right_value2)
	return left_value
def parse_group_expression(group_expression):
	assert(group_expression[0]=="group-expression")
	assert(len(group_expression)==2)
	return parse_expression(group_expression[1])
def parse_optionalElseStatement(optionalElseStatement,label_start="continue???",label_end="break???"):
	assert(optionalElseStatement[0]=="optionalElseStatement")
	assert(len(optionalElseStatement)==2)
	if optionalElseStatement[1]==None:
		return
	elif(optionalElseStatement[1][0]=="statement"):
		parse_statement(optionalElseStatement[1],label_start,label_end)
	return
def parse_functioncallExpression(functioncallExpression):
	assert(functioncallExpression[0]=="functioncallExpression")
	assert(len(functioncallExpression)==3)
	assert(functioncallExpression[2][0]=="argumentExpressionList")
	assert(len(functioncallExpression[2])==2)
	for _ in functioncallExpression[2][1][::-1]:
		right_value1=parse_expression(_)
		print("\t"+str(("arg",right_value1,None,None)))
		ret_temp_var(right_value1)
	if type_func=="void":
		print("\t"+str(("call",functioncallExpression[1],None,None)))
		return None
	else:
		left_value=new_temp_var()
		print("\t"+str(("call",functioncallExpression[1],None,left_value)))
		return left_value
	assert(False)
	#print(functioncallExpression)
def parse_selfoperatorExpression(selfoperatorExpression):
	assert(selfoperatorExpression[0]=="selfoperatorExpression")
	assert(len(selfoperatorExpression)==3)
	right_value1=parse_expression(selfoperatorExpression[1])
	left_value=new_temp_var()
	print("\t"+str((":=",right_value1,None,left_value)))
	ret_temp_var(right_value1)
	operator=selfoperatorExpression[2]
	assert(operator=="++" or selfoperatorExpression[2]=="--")
	if selfoperatorExpression[1][0]=="identifier-expression":
		print("\t"+str((operator,None,None,selfoperatorExpression[1][1])))
	elif selfoperatorExpression[1][0]=="arrayExpression":
		idx=calc_array_index(selfoperatorExpression[1])
		print("\t"+str(("[]"+operator,None,None,"{}[{}]".format(selfoperatorExpression[1][1][1],idx))))
		ret_temp_var(idx)
	return left_value
def parse_compositeExpression(compositeExpression):
	assert(compositeExpression[0]=="compositeExpression")
	right_value1=parse_expression((\
		"binary-expression",\
		compositeExpression[2][:-1],\
		compositeExpression[1],\
		compositeExpression[3]))#calc op result
		
	if compositeExpression[1][0]=="identifier-expression":
		left_value=parse_identifier_expression(compositeExpression[1])
		print("\t"+str((":=",right_value1,None,left_value)))
		ret_temp_var(left_value)
	elif compositeExpression[1][0]=="arrayExpression":
		idx=calc_array_index(compositeExpression[1])
		print("\t"+str(("[]:=",right_value1,None,"{}[{}]".format((compositeExpression[1][1][1],find_addr(compositeExpression[1][1][1])),idx))))
		ret_temp_var(idx)
	else:
		assert(False)
	return right_value1
def parse_getaddrExpression(getaddrExpression):
	assert(getaddrExpression[0]=="getaddrExpression")
	assert(len(getaddrExpression)==2)
	#assert(getaddrExpression[1][0]=="identifier-expression") thought commet, still in use
	right_value1=parse_identifier_expression(getaddrExpression[1])
	left_value=new_temp_var()
	print("\t"+str((":=(&)",right_value1,None,left_value)))
	ret_temp_var(right_value1)
	return left_value
def parse_minus(minus):
	assert(minus[0]=="minus")
	assert(len(minus)==2)
	#print(minus)
	left_value=new_temp_var()
	right_value2=parse_expression(minus[1])
	print("\t"+str(("-",0,right_value2,left_value)))
	ret_temp_var(right_value2)
	return left_value
def parse_stringExpression(stringExpression):
	assert(stringExpression[0]=="stringExpression")
	assert(len(stringExpression)==2)
	strctx=bytes(stringExpression[1],encoding="ascii")
	strname=get_string_name(strctx)
	global global_var
	global_var.append(("char",strname,(True,None),strctx))
	return (strname,(strctx,"char[]",len(strctx)+1))
def parse_expression(expression):
	if expression[0]=="binary-expression":
		return parse_binary_expression(expression)
	elif expression[0]=="assignExpression":
		return parse_assignExpression(expression)
	elif expression[0]=="int-expression":
		return parse_int_expression(expression)
	elif expression[0]=="identifier-expression":
		return parse_identifier_expression(expression)
	elif expression[0]=="group-expression":
		return parse_group_expression(expression)
	elif expression[0]=="arrayExpression":
		return parse_arrayExpression(expression)
	elif expression[0]=="removeref":
		return parse_removeref(expression)
	elif expression[0]=="functioncallExpression":
		return parse_functioncallExpression(expression)
	elif expression[0]=="selfoperatorExpression":
		return parse_selfoperatorExpression(expression)
	elif expression[0]=="compositeExpression":
		return parse_compositeExpression(expression)
	elif expression[0]=="getaddrExpression":
		return parse_getaddrExpression(expression)
	elif expression[0]=="minus":
		return parse_minus(expression)
	elif expression[0]=="stringExpression":
		return parse_stringExpression(expression)
	print(expression)
	assert(False)
	return
def parse_ifstatement(ifstatement,label_start="continue???",label_end="break???"):
	assert(ifstatement[0]=="ifStatement")
	right_value1=parse_expression(ifstatement[1])
	label_true=new_label()
	label_false=new_label()
	label_end=new_label()
	print("\t"+str(("j!=",right_value1,0,label_true)))
	ret_temp_var(right_value1)
	print("\t"+str(("j",None,None,label_false)))
	print(label_true+":")
	parse_statement(ifstatement[2],label_start,label_end)
	print("\t"+str(("j",None,None,label_end)))
	print(label_false+":")
	parse_optionalElseStatement(ifstatement[3],label_start,label_end)
	#print("\t"+"else part...")
	print(label_end+":")
	return
def parse_arrayExpression(arrayExpression):	
	assert(arrayExpression[0]=="arrayExpression")
	left_value=new_temp_var()
	assert(arrayExpression[1][0]=="identifier-expression")
	right_value2=parse_expression(arrayExpression[2])
	print("\t"+str((":=[]",(arrayExpression[1][1],find_addr(arrayExpression[1][1])),right_value2,left_value)))
	ret_temp_var(right_value2)
	return left_value
def parse_removeref(removeref):
	assert(removeref[0]=="removeref")
	assert(len(removeref)==2)
	right_value1=parse_expression(removeref[1])
	left_value=new_temp_var()
	print("\t"+str((":=(*)",right_value1,None,left_value)))
	ret_temp_var(right_value1)
	return left_value
def parse_expressionStatement(expressionStatement):	
	assert(expressionStatement[0]=="expressionStatement")
	assert(len(expressionStatement)==2)
	if expressionStatement[1]==";":#empty
		return None
	else:
		return parse_expression(expressionStatement[1])
	return
def parse_returnStatement(returnStatement):
	assert(returnStatement[0]=="returnStatement")
	assert(len(returnStatement)==2)
	#print(returnStatement)
	right_value1=parse_expression(returnStatement[1])
	print("\t"+str(("ret",right_value1,None,None)))
	ret_temp_var(right_value1)
	return
def parse_forStatement(forStatement):
	assert(forStatement[0]=="forStatement")
	assert(len(forStatement)==5)
	assert(forStatement[1][0]=="optionalExpression")#i=0
	assert(forStatement[2][0]=="optionalExpression")#i<=n
	assert(forStatement[3][0]=="optionalExpression")#i++
	if forStatement[1][1]==None:
		pass
	else:
		parse_expression(forStatement[1][1])
	label_start=new_label()
	label_end=new_label()
	print(label_start+":")
	if forStatement[2][1]==None:
		pass
	else:
		right_value1=parse_expression(forStatement[2][1])
		print("\t"+str(("j==",right_value1,0,label_end)))
		ret_temp_var(right_value1)
	parse_statement(forStatement[4],label_start,label_end)
	if forStatement[3][1]==None:
		pass
	else:
		ret_temp_var(parse_expression(forStatement[3][1]))
	print("\t"+str(("j",None,None,label_start)))
	print(label_end+":")
	return
	#for _ in forStatement:
	#	print(_)
def parse_whileStatement(whileStatement):
	assert(whileStatement[0]=="whileStatement")
	assert(len(whileStatement)==3)
	label_start=new_label()
	label_end=new_label()
	print(label_start+":")
	right_value1=parse_expression(whileStatement[1])
	print("\t"+str(("j==",right_value1,0,label_end)))
	ret_temp_var(right_value1)
	parse_statement(whileStatement[2],label_start,label_end)
	print("\t"+str(("j",None,None,label_start)))
	print(label_end+":")
	return	
def parse_statement(statement,label_start="continue???",label_end="break???"):
	assert(statement[0]=="statement")
	assert(len(statement)==2)
	if statement[1][0]=="ifStatement":
		parse_ifstatement(statement[1],label_start,label_end)
	elif statement[1][0]=="expressionStatement":
		ret_temp_var(parse_expressionStatement(statement[1]))
	elif statement[1][0]=="returnStatement":
		parse_returnStatement(statement[1])
	elif statement[1][0]=="forStatement":
		parse_forStatement(statement[1])
	elif statement[1][0]=="whileStatement":
		parse_whileStatement(statement[1])
	elif statement[1][0]=="compoundStatement":
		parse_compoundStatement(statement[1],label_start,label_end)
	elif statement[1]=="breakStatement":
		print("\t"+str(("j",None,None,label_end)))
	elif statement[1]=="continueStatement":
		print("\t"+str(("j",None,None,label_begin)))
	else:
		print(statement[1])
		assert(False)
	return
def parse_localDeclaration(localDeclaration):
	assert(localDeclaration[0]=="localDeclaration")
	assert(len(localDeclaration)==2)
	ret=[]
	if localDeclaration[1][0]=="staticVariableDeclaration":#local var
		staticdec=localDeclaration[1]
		var_type=staticdec[1][1]
		for _ in staticdec[2][1]:
			if len(_)==2:
				ret.append((var_type,_[1],(False,1),-type_size[var_type]))#type name (isarray arraysize)
			else:#pointer
				ret.append((var_type+_[1][1][0],_[2],(False,1),-type_size[var_type+_[1][1][0]]))
	elif localDeclaration[1][0]=="staticVariableArrayDeclaration":#local var(arr)
		staticdec=localDeclaration[1]
		ret.append((staticdec[1][1],staticdec[2][1],(True,staticdec[3]),-type_size[staticdec[1][1]]*staticdec[3]))
	return ret
def parse_localDeclarations(localDeclarations):
	assert(localDeclarations[0]=="localDeclarations")
	assert(len(localDeclarations)==2)
	ret=[]
	for _ in localDeclarations[1]:
		ret+=parse_localDeclaration(_)
	#print(local_var)
	return ret
def parse_optionalLocalDeclarations(optionalLocalDeclarations):
	assert(optionalLocalDeclarations[0]=="optionalLocalDeclarations")
	if optionalLocalDeclarations[1]==None:
		return []
	elif optionalLocalDeclarations[1][0]=="localDeclarations":
		return parse_localDeclarations(optionalLocalDeclarations[1])
	else:
		assert(False)
	return
def parse_statementList(statementList,label_start="continue???",label_end="break???"):
	assert(statementList[0]=="statementList")
	assert(len(statementList)==2)
	for _ in statementList[1]:
		parse_statement(_,label_start,label_end)
	return
def parse_optionalStatementList(optionalStatementList,label_start="continue???",label_end="break???"):
	assert(optionalStatementList[0]=="optionalStatementList")
	if(optionalStatementList[1][0]=="statementList"):
		parse_statementList(optionalStatementList[1],label_start,label_end)
	else:
		assert(False)
def parse_compoundStatement(compoundStatement,label_start="continue???",label_end="break???"):
	assert(compoundStatement[0]=="compoundStatement")
	assert(len(compoundStatement)==3)
	global local_var
	new_local_var=parse_optionalLocalDeclarations(compoundStatement[1])
	for _ in new_local_var[::-1]:
		if(len(local_var)==0):
			local_var=[_]
		else:
			#print(_)
			local_var=[(_[0],_[1],_[2],_[3]+local_var[0][3])]+local_var
	#local_var=new_local_var+local_var
	parse_optionalStatementList(compoundStatement[2],label_start,label_end)
	#local_var=local_var[len(new_local_var):]
	#for _ in compoundStatement[1:]:
	#	#print(_)
	#	if _[0]=="optionalLocalDeclarations":
	#		parse_optionalLocalDeclarations(_)
	#	elif _[0]=="optionalStatementList":
	#		parse_optionalStatementList(_)
def parse_parameter(parameter):
	assert(parameter[0]=="parameter")
	global local_para
	if type(parameter[2][1])==tuple:#ref
		var_type=parameter[1][1]+parameter[2][1][1][0]
		var_name=parameter[2][2]
	else:
		var_type=parameter[1][1]
		var_name=parameter[2][1]
	if len(local_para)==0:
		local_para.append((var_type,var_name,(False,1),0))#type name info base
	else:
		local_para.append((var_type,var_name,(False,1),local_para[-1][3]+type_size[local_para[-1][0]]*local_para[-1][2][1]))
def parse_parameterList(parameterList):	
	assert(parameterList[0]=="parameterList")
	global local_para
	local_para=[]
	for _ in parameterList[1]:
		parse_parameter(_)
def parse_parameters(parameters, label_func):
	assert(parameters[0]=="parameters")
	global local_para
	if(parameters[1]=="void"):
		local_para=[]
	elif parameters[1][0]=="parameterList":
		parse_parameterList(parameters[1])
	else:
		assert(False)
	print("local_para =",local_para)
	global symbol_table
	symbol_table.setdefault(label_func, {}).setdefault('local_para', local_para)
	return
def parse_functionDeclaration(functionDeclaration):#1-> return type 2->name 3->para 4->body
	assert(functionDeclaration[0]=="functionDeclaration")
	global label_func,label_count,temp_var_count,max_temp_size,type_func,local_var
	type_func=functionDeclaration[1]
	label_func=functionDeclaration[2]
	label_count=0
	max_temp_size=0
	temp_var_count.put(1)
	print(label_func,"proc")
	parse_parameters(functionDeclaration[3], label_func)
	assert(functionDeclaration[4][0]=="compoundStatement")
	local_var=[]#empty here
	parse_compoundStatement(functionDeclaration[4])
	print("local_var =",local_var)
	print("max_temp_size =",max_temp_size)
	print("var_size =",-local_var[0][3] if len(local_var)>0 else 0)
	print("para_size =",local_para[-1][3]+type_size[local_para[-1][0]]*local_para[-1][2][1] if len(local_para)>0 else 0)
	while not temp_var_count.empty():
		temp_var_count.get()
		#print(temp_var_count.get(),end="$$")
	print(label_func,"endp")
	print(">"*9)
	global symbol_table
	symbol_table.setdefault(label_func, {}).setdefault('local_var', local_var)

def parse_staticVariableDeclaration(staticVariableDeclaration):
	assert(staticVariableDeclaration[0]=="staticVariableDeclaration")
	assert(len(staticVariableDeclaration)==3)
	assert(staticVariableDeclaration[2][0]=="declaratorList")
	global global_var
	var_type=staticVariableDeclaration[1][1]
	for _ in staticVariableDeclaration[2][1]:
		if len(_)==2:#
			global_var.append((var_type,_[1],(False,1),None))#int a
		else:#pointer
			global_var.append((var_type+_[1][1][0],_[2],(False,1),None))#int *a
	#print(staticVariableDeclaration)
	return
def parse_staticVariableArrayDeclaration(staticVariableArrayDeclaration):
	assert(staticVariableArrayDeclaration[0]=="staticVariableArrayDeclaration")
	assert(len(staticVariableArrayDeclaration)==4)
	global global_var
	global_var.append((\
	staticVariableArrayDeclaration[1][1],\
	staticVariableArrayDeclaration[2][1],\
	(True,staticVariableArrayDeclaration[3]),\
	None))
	#print(staticVariableArrayDeclaration)
	return
def parse_declaration(declaration):
	assert(declaration[0]=="declaration")
	if declaration[1][0]=="functionDeclaration":
		parse_functionDeclaration(declaration[1])
	elif declaration[1][0]=="staticVariableDeclaration":
		parse_staticVariableDeclaration(declaration[1])
	elif declaration[1][0]=="staticVariableArrayDeclaration":
		parse_staticVariableArrayDeclaration(declaration[1])
	else:
		assert(False)
def parse_declarationList(declarationList):
	assert(declarationList[0]=="declarationList")
	for _ in declarationList[1]:
		parse_declaration(_)
	global global_var
	print("global_var =",global_var)
	global symbol_table
	symbol_table.setdefault('global', {}).setdefault('global_var', global_var)

def parse_program(program):
	assert(program[0]=="program")
	if program[1][0]=="declarationList":
		parse_declarationList(program[1])
	else:
		assert(False)
if __name__ == "__main__":
	try:
		f=open(sys.argv[1],"r")
		prog=f.read().strip()
		f.close()
	except:
		prog=input().strip()
	parse_program(eval(prog))

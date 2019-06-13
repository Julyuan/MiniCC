.386
.model flat,stdcall
include msvcrt.inc
includelib msvcrt.lib
data segment use32
	data_i dd 0
	aDN db "%d\n",0,'$'
data ends
code segment use32
assume cs:code,ds:data
go proc
	push ebp
	mov ebp,esp
	sub esp,16
	xor edi,edi
	mov eax,dword ptr [ebp+8+0]
	cmp eax,1
	jne go_masm32_L1
	inc edi
go_masm32_L1:
	mov dword ptr [ebp-16+0],edi
	mov eax,dword ptr [ebp-16+0]
	cmp eax,0
	jne go_L1
	jmp go_L2
go_L1:
	mov eax,1
	mov dword ptr [ebp-4],eax
	jmp go_L3
go_L2:
	xor edi,edi
	mov eax,dword ptr [ebp+8+0]
	cmp eax,2
	jne go_masm32_L2
	inc edi
go_masm32_L2:
	mov dword ptr [ebp-16+0],edi
	mov eax,dword ptr [ebp-16+0]
	cmp eax,0
	jne go_L4
	jmp go_L5
go_L4:
	mov eax,1
	mov dword ptr [ebp-4],eax
	jmp go_L6
go_L5:
	mov eax,dword ptr [ebp+8+0]
	sub eax,1
	mov dword ptr [ebp-16+4],eax
	push dword ptr [ebp-16+4]
	call go
	mov dword ptr [ebp-16+4],eax
	mov eax,dword ptr [ebp+8+0]
	sub eax,2
	mov dword ptr [ebp-16+8],eax
	push dword ptr [ebp-16+8]
	call go
	mov dword ptr [ebp-16+8],eax
	mov eax,dword ptr [ebp-16+4]
	add eax,dword ptr [ebp-16+8]
	mov dword ptr [ebp-16+0],eax
	mov eax,dword ptr [ebp-16+0]
	mov dword ptr [ebp-4],eax
go_L6:
go_L3:
	mov eax,dword ptr [ebp-4]
	jmp go_masm32_exit_label
go_masm32_exit_label:
	mov esp,ebp
	pop ebp
	retn 4
go endp
main proc
	push ebp
	mov ebp,esp
	push ecx
	push 10
	call go
	mov dword ptr [ebp-4+0],eax
	mov eax,dword ptr [ebp-4+0]
	mov dword ptr [data_i],eax
	push dword ptr [data_i]
	push offset [aDN]
	call crt_printf
	mov dword ptr [ebp-4+0],eax
	mov eax,0
	jmp main_masm32_exit_label
main_masm32_exit_label:
	push 0
	call crt_exit
	mov esp,ebp
	pop ebp
	retn 0
main endp
code ends
end main

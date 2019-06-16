.386
.model flat,stdcall
include msvcrt.inc
includelib msvcrt.lib
data segment use32
	data_f dd 0
	data_k dd 0
	aDN db "%d",0ah,0dh,0,'$'
	aDN_0 db "%d",0ah,0dh,0,'$'
data ends
code segment use32
assume cs:code,ds:data

go proc
	push ebp
	mov ebp,esp
	sub esp,24
	xor edi,edi
	mov eax,dword ptr [ebp+8+4]
	cmp eax,0
	jle go_masm32_L1
	inc edi
go_masm32_L1:
	mov eax,edi
	cmp eax,0
	jne go_L1
	jmp go_L2
go_L1:
	mov eax,dword ptr [ebp+8+4]
	sub eax,1
	push eax
	push dword ptr [ebp+8+0]
	call go
	mov dword ptr [ebp-24+4],eax
	mov eax,dword ptr [ebp+8+4]
	imul dword ptr [ebp-24+4]
	mov dword ptr [ebp-4],eax
	jmp go_L3
go_L2:
	mov eax,1
	mov dword ptr [ebp-4],eax
go_L3:
	mov ebx,dword ptr [ebp+8+0]
	mov eax,dword ptr [ebx]
	add eax,dword ptr [ebp-4]
	mov ebx,dword ptr [ebp+8+0]
	mov dword ptr [ebx],eax
	mov eax,dword ptr [data_k]
	add eax,dword ptr [ebp-4]
	mov dword ptr [data_k],eax
	mov eax,dword ptr [ebp-4]
	jmp go_masm32_exit_label
go_masm32_exit_label:
	mov esp,ebp
	pop ebp
	retn 8
go endp
main proc
	push ebp
	mov ebp,esp
	push ecx
	mov eax,0
	mov dword ptr [data_k],eax
	push 5
	lea eax,dword ptr [data_k]
	push eax
	call go
	mov dword ptr [data_f],eax
	push eax
	push offset [aDN]
	call crt_printf
	push dword ptr [data_k]
	push offset [aDN_0]
	call crt_printf
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

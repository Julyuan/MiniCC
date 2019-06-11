.386
.model flat,stdcall
include msvcrt.inc
includelib msvcrt.lib
data segment use32
	data_i dd 0
	data_ans dd 0
	aD db "%d",0ah,0dh,0,'$'
data ends
code segment use32
assume cs:code,ds:data
gcd proc
	push ebp
	mov ebp,esp
	sub esp,8
	xor edi,edi
	mov eax,dword ptr [ebp+8+4]
	mov ebx,0
	cmp eax,ebx
	jne gcd_masm32_L1
	inc edi
gcd_masm32_L1:
	mov eax,edi
	mov dword ptr [esp+0],eax
	mov eax,dword ptr [esp+0]
	mov ebx,0
	cmp eax,ebx
	jne gcd_L1
	jmp gcd_L2
gcd_L1:
	mov eax,dword ptr [ebp+8+0]
	mov dword ptr [ebp-4],eax
	jmp gcd_L3
gcd_L2:
	mov eax,dword ptr [ebp+8+0]
	cdq
	mov ecx,dword ptr [ebp+8+4]
	idiv ecx
	mov dword ptr [esp+0],edx
	push dword ptr [esp+0]
	push dword ptr [ebp+8+4]
	call gcd
	mov dword ptr [esp+0],eax
	mov eax,dword ptr [esp+0]
	mov dword ptr [ebp-4],eax
gcd_L3:
	mov eax,dword ptr [ebp-4]
	jmp gcd_masm32_exit_label
gcd_masm32_exit_label:
	mov esp,ebp
	pop ebp
	retn 8
gcd endp
main proc
	sub esp,12
	push 36
	push 9
	call gcd
	lea dword ptr [esp+4],dword ptr [esp+4]
	mov dword ptr [esp+4],eax
	push 6
	push 666
	call gcd
	mov dword ptr [esp+8],eax
	mov eax,dword ptr [esp+4]
	imul dword ptr [esp+8]
	mov dword ptr [esp+0],eax
	mov eax,dword ptr [esp+0]
	mov dword ptr [data_ans],eax
	push dword ptr [data_ans]
	push offset [aD]
	call crt_printf
	mov dword ptr [esp+0],eax
	mov eax,0
	jmp main_masm32_exit_label
main_masm32_exit_label:
	push 0
	call crt_exit
main endp
code ends
end main

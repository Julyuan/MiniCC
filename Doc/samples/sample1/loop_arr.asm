.386
.model flat,stdcall
include msvcrt.inc
includelib msvcrt.lib
data segment use32
	aFDDN db "f[%d]=%d",0ah,0dh,0,'$'
data ends
code segment use32
assume cs:code,ds:data
main proc
	push ebp
	mov ebp,esp
	sub esp,60
	mov eax,0
	mov dword ptr [ebp-44],eax
main_L1:
	xor edi,edi
	mov eax,dword ptr [ebp-44]
	cmp eax,10
	jge main_masm32_L1
	inc edi
main_masm32_L1:
	mov dword ptr [ebp-60+0],edi
	mov eax,dword ptr [ebp-60+0]
	cmp eax,0
	je main_L2
	xor edi,edi
	mov eax,dword ptr [ebp-44]
	cmp eax,1
	jg main_masm32_L2
	inc edi
main_masm32_L2:
	mov dword ptr [ebp-60+0],edi
	mov eax,dword ptr [ebp-60+0]
	cmp eax,0
	jne main_L3
	jmp main_L4
main_L3:
	lea ebx,dword ptr [ebp-40]
	mov edi,dword ptr [ebp-44]
	mov eax,dword ptr [ebp-44]
	mov dword ptr [ebx+edi*4],eax
	jmp main_L5
main_L4:
	mov eax,dword ptr [ebp-44]
	sub eax,1
	mov dword ptr [ebp-60+8],eax
	lea ebx,dword ptr [ebp-40]
	mov edi,dword ptr [ebp-60+8]
	mov eax,dword ptr [ebx+edi*4]
	mov dword ptr [ebp-60+4],eax
	mov eax,dword ptr [ebp-44]
	sub eax,2
	mov dword ptr [ebp-60+12],eax
	lea ebx,dword ptr [ebp-40]
	mov edi,dword ptr [ebp-60+12]
	mov eax,dword ptr [ebx+edi*4]
	mov dword ptr [ebp-60+8],eax
	mov eax,dword ptr [ebp-60+4]
	add eax,dword ptr [ebp-60+8]
	mov dword ptr [ebp-60+0],eax
	lea ebx,dword ptr [ebp-40]
	mov edi,dword ptr [ebp-44]
	mov eax,dword ptr [ebp-60+0]
	mov dword ptr [ebx+edi*4],eax
main_L5:
	mov eax,dword ptr [ebp-44]
	add eax,1
	mov dword ptr [ebp-60+0],eax
	mov eax,dword ptr [ebp-60+0]
	mov dword ptr [ebp-44],eax
	jmp main_L1
main_L2:
	mov eax,0
	mov dword ptr [ebp-44],eax
main_L6:
	xor edi,edi
	mov eax,dword ptr [ebp-44]
	cmp eax,9
	jg main_masm32_L3
	inc edi
main_masm32_L3:
	mov dword ptr [ebp-60+0],edi
	mov eax,dword ptr [ebp-60+0]
	cmp eax,0
	je main_L7
	lea ebx,dword ptr [ebp-40]
	mov edi,dword ptr [ebp-44]
	mov eax,dword ptr [ebx+edi*4]
	mov dword ptr [ebp-60+0],eax
	push dword ptr [ebp-60+0]
	push dword ptr [ebp-44]
	push offset [aFDDN]
	call crt_printf
	mov dword ptr [ebp-60+0],eax
	mov eax,dword ptr [ebp-44]
	add eax,1
	mov dword ptr [ebp-60+0],eax
	mov eax,dword ptr [ebp-60+0]
	mov dword ptr [ebp-44],eax
	jmp main_L6
main_L7:
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

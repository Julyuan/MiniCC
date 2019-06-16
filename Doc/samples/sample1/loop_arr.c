int main(void){
	int i;
	int f[10];
	for(i=0;i<10;i+=1)
		if(i<=1)
			f[i]=i;
		else
			f[i]=f[i-1]+f[i-2];
	for(i=0;i<=9;i+=1)
		printf("f[%d]=%d\n",i,f[i]);
	return 0;
}

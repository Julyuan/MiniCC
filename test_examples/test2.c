int i;

int go(int a){
    int g;
    if(a==1){
        g = 1;
    }else{
        if(a==2){
            g = 1;
        }else{
            g = go(a-1) + go(a-2);
        }
    }
    return g;
}

int main(void)
{
    i=go(10);
    printf("%d\n",i);
    return 0;
}
int f;
int k;

int go(int* b, int a)
{
    int fk;
    double t;
    int g;
    if(a > 0){
        g = a * go(b, a-1);
    }else{
        g = 1;
    }
    *b = *b + g;
    k = k + g;
    return g;
}

int main(void)
{
    k = 0;
    f = go(&k, 5);
    printf("%d\n", f);
    printf("%d\n", k);
    return 0;
}
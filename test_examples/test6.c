int ans;

int gcd(int a, int b)
{
    int g;
    if(b==0){
        g = a;
    }else{
        g = gcd(b, a % b);
    }
    return g;
}

int main(void)
{
    ans = gcd(9, 36) * gcd(3, 6);
    printf("%d\n", ans);
    return 0;
}
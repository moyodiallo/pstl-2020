#include <stdio.h>
#include <stdlib.h>

unsigned long long gamma(unsigned long long n, unsigned long long p);
unsigned long long somme_gamma(unsigned long long n, unsigned long long p);

int main(int argc, char** argv){

    if(argc != 3){
        printf("cmd <n> <p>");
        exit(EXIT_FAILURE);
    }

    unsigned long long n = atol(argv[1]);
    unsigned long long p = atol(argv[2]); 

    printf("Gamma = %llu",gamma(n,p));

    return 0;
}

unsigned long long gamma(unsigned long long n, unsigned long long p){
    if(n == 0)
        return p+1;
    else if(n == 1)
        return (p*p) + p + 1;
    else 
        return somme_gamma(n,p); 
}

unsigned long long somme_gamma(unsigned long long n, unsigned long long p){
    unsigned long long som = 0;
    for (size_t i = 0; i < n-1; i++)
    {
        som+= (gamma(i,p)*gamma(n-1-i,p+1));
    }
    return som;
}

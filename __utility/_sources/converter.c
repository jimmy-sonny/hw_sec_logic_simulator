#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    
    FILE *fpin, *fpout;
    
    fpin = fopen("output_readable.txt", "r");
    if (fpin == NULL){
        printf("ERROR:: file output_readable.txt does not exist\n");
        return 1;
    }
    
    fpout = fopen("output_readable_proc.txt", "w");
    if (fpout == NULL){
        printf("ERROR:: file output_readable_proc.txt not created\n");
        return 1;
    }
    
    double hd_prob;
    double sign_prob;
    int nsr;
    int nik;
    int nio;
    
    while (fscanf(fpin, "%lf %lf %d %d %d", &hd_prob, &sign_prob, &nsr, &nik, &nio) != EOF) {
        fprintf(fpout, "%f %f %d %d\n", fabs(0.5-hd_prob), fabs(0.5-sign_prob), nsr, nik);
    }
    
    printf("INFO:: conversion finished\n");
    return 0;
}
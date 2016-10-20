#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    
    FILE *fpin, *fpout_hd, *fpout_sig_prob, *fpout_20;
    
    fpin = fopen("output_readable_proc_sorted.txt", "r");
    if (fpin == NULL){
        printf("ERROR:: file output_readable_proc_sorted.txt does not exist\n");
        return 1;
    }
    
    fpout_hd = fopen("best_hd.txt", "w");
    if (fpout_hd == NULL){
        printf("ERROR:: file best not created\n");
        return 1;
    }
    
    fpout_sig_prob = fopen("best_sig_prob.txt", "w");
    if (fpout_sig_prob == NULL){
        printf("ERROR:: file best not created\n");
        return 1;
    }
    
    fpout_20 = fopen("best_20.txt", "w");
    if (fpout_20 == NULL){
        printf("ERROR:: file best not created\n");
        return 1;
    }
    
    float hd_prob;
    float sign_prob;
    int nsr_20;
    int nik;
    
    int temp = -1;
    while (fscanf(fpin, "%f %f %d %d", &hd_prob, &sign_prob, &nsr_20, &nik) != EOF) {
        if (nik > temp){
            fprintf(fpout_hd, "%f %d\n", fabs(0.5-hd_prob), nik);
            fprintf(fpout_sig_prob, "%f %d\n", fabs(0.5-sign_prob), nik);
            fprintf(fpout_20, "%d %d\n", nsr_20, nik);
            temp = nik;
        }

    }
    
    printf("INFO:: print best finished\n");
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){

    FILE *fpin, *fpout_hd, *fpout_sig_prob;
    FILE *fpout_20, *fpout_01;

    float hd_prob;
    float sign_prob;
    int nsr_20;
    int nik;
    int nsr_01;

    // HAMMING DISTANCE
    fpin = fopen("output_readable_proc_sorted_k4k1.txt", "r");
    if (fpin == NULL){ printf("ERROR:: file output_readable_proc_sorted_k4k1.txt does not exist\n"); return 1; }

    fpout_hd = fopen("best_hd.txt", "w");
    if (fpout_hd == NULL){ printf("ERROR:: file best not created\n"); return 1; }

    int temp = -1;
    while (fscanf(fpin, "%f %f %d %d %d", &hd_prob, &sign_prob, &nsr_20, &nik, &nsr_01) != EOF) {
        if (nik > temp){ fprintf(fpout_hd, "%f %d\n", fabs(0.5-hd_prob), nik); temp = nik; }
    }

    fclose(fpin);
    fclose(fpout_hd);


    // SIGNAL PROBABILITY
    fpin = fopen("output_readable_proc_sorted_k4k2.txt", "r");
    if (fpin == NULL){ printf("ERROR:: file output_readable_proc_sorted_k4k2.txt does not exist\n"); return 1; }

    fpout_sig_prob = fopen("best_sig_prob.txt", "w");
    if (fpout_sig_prob == NULL){ printf("ERROR:: file best not created\n"); return 1; }

    temp = -1;
    while (fscanf(fpin, "%f %f %d %d %d", &hd_prob, &sign_prob, &nsr_20, &nik, &nsr_01) != EOF) {
        if (nik > temp){ fprintf(fpout_sig_prob, "%f %d\n", fabs(0.5-sign_prob), nik); temp = nik; }
    }

    fclose(fpin);
    fclose(fpout_sig_prob);


    // Rare signal 0.20
    fpin = fopen("output_readable_proc_sorted_k4k3.txt", "r");
    if (fpin == NULL){ printf("ERROR:: file output_readable_proc_sorted_k4k3.txt does not exist\n"); return 1; }

    fpout_20 = fopen("best_20.txt", "w");
    if (fpout_20 == NULL){ printf("ERROR:: file best not created\n"); return 1; }

    temp = -1;
    while (fscanf(fpin, "%f %f %d %d %d", &hd_prob, &sign_prob, &nsr_20, &nik, &nsr_01) != EOF) {
        if (nik > temp){ fprintf(fpout_20, "%d %d\n", nsr_20, nik); temp = nik; }
    }

    fclose(fpin);
    fclose(fpout_20);


    // Rare signal 0.01
    fpin = fopen("output_readable_proc_sorted_k4k5.txt", "r");
    if (fpin == NULL){ printf("ERROR:: file output_readable_proc_sorted_k4k5.txt does not exist\n"); return 1; }

    fpout_01 = fopen("best_01.txt", "w");
    if (fpout_01 == NULL){ printf("ERROR:: file best not created\n"); return 1; }

    temp = -1;
    while (fscanf(fpin, "%f %f %d %d %d", &hd_prob, &sign_prob, &nsr_20, &nik, &nsr_01) != EOF) {
        if (nik > temp){ fprintf(fpout_01, "%d %d\n", nsr_01, nik); temp = nik; }
    }

    fclose(fpin);
    fclose(fpout_01);

    printf("INFO:: print best finished\n");
    return 0;
}

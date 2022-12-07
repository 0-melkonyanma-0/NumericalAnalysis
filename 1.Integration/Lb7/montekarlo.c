#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <math.h>


void fill_zero(float *array,int size){
	for(int i = 0; i < size;++i){
		array[i] = 0.;
	}
}

float uniform(){
	return (float)rand()/(float)RAND_MAX;
}

int main()
{
	srand(time(NULL));
	int M = 3;
	int interval[3][2] = {
							{1,2},
							{2,4},
							{1,5}
						};
	float exprement[] = {1e4,1e6,1e8};
	int func_exponent[] = {1,0,0};
	float integral_res[3];
	fill_zero(integral_res,M);

	for(int i = 0; i < M ;++i){
		float sum = 0.;
		float res = 1.;
		for(int k = 0; k < M ;++k){
			if(func_exponent[k] != 0){
				for(int j = 0; j < exprement[i];++j){
					sum += interval[k][0] + powl((interval[k][1] -
                                            interval[k][0])*uniform(),exprement[i]);
				}
			}	
			res *= (interval[k][1]-interval[k][0]);
			continue;
		}
		integral_res[i] = res;
	}

	for(int i = 0; i < M ;++i){
		printf("%f ", integral_res[i]);
	}

	// for(int j = 0; j < M ;++j){
	// 	for(int i = 0; i < exprement[j] ;++i){
	// 	float a = (float)rand()/(float)RAND_MAX;

	// 	// printf("%f\n",a);
	// 	}
	// }
	return 0;

}

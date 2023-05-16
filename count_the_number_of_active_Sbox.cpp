#include"linear_part_of_some_block_cipher.h"
#define round 7          //Number of encryption rounds 
#define bound 36          //Preset maximum total number of active S-boxes
 


int main()
{
	unsigned _int32 i=0,j=0;
	unsigned _int16 a=0;
	unsigned _int16 L=0,temp[round]={0},sum=0,flag=bound,number_of_input=0,record_number_of_sbox[100][round]={0},difference[100][2]={0};
	for(i=0x1;i<0x10000;i++)              //Traverse all input patterns
	{
		a=i;
		for(j=0;j<round;j++)
		{
			a=Midori(a);                 //Target ciphers
			//printf("%x\n",a);
			L=weight(a);
			temp[j]=L;                                  //The array temp[] is used to store the number of active S-boxes per round
			sum+=L;                                     //sum is used to count the total number of active S-boxes
			
			
			                           

		}
		
		if(sum<=flag)
		{
			flag=sum;
			printf("Total number of active S-boxes after %d rounds is %d,the input pattern is 0x%x, the output pattern is 0x%x, the order of active S-boxes is: ",round,sum,i,a);
			for(j=0;j<round;j++)
				printf("%d, ",temp[j]);
			printf("\n");
		}
		sum=0;		
	}
	
	
	return 0;
}
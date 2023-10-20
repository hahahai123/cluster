#include<stdio.h>
#include<time.h>
#include<iostream.h>
#include<stdlib.h>
const int S[16]={0xc,0xa,0xd,0x3,0xe,0xb,0xf,0x7,0x8,0x9,0x1,0x5,0x0,0x2,0x4,0x6};
const int P[16]={0xf,0xc,0xd,0xe,0xa,0x9,0x8,0xb,0x6,0x5,0x4,0x7,0x1,0x2,0x3,0x0};
const int Q[16]={0xc,0xa,0xf,0x5,0xe,0x8,0x9,0x2,0xb,0x3,0x7,0x4,0x6,0x0,0x1,0xd};
const int RC3[32]={0x1,0x4,0x2,0x5,0x6,0x7,0x3,0x1,0x4,0x2,0x5,0x6,0x7,0x3,0x1,0x4,
				0x2,0x5,0x6,0x7,0x3,0x1,0x4,0x2,0x5,0x6,0x7,0x3,0x1,0x4,0x2,0x5};
const int RC4[32]={0x1,0x8,0x4,0x2,0x9,0xc,0x6,0xb,0x5,0xa,0xd,0xe,0xf,0x7,0x3,0x1,
				0x8,0x4,0x2,0x9,0xc,0x6,0xb,0x5,0xa,0xd,0xe,0xf,0x7,0x3,0x1,0x8};



//CRAFT



int TK[4][16];

void Initialize_key(int Key1[], int Key2[])
{
	
	int Tweak[16]={0};
	int i=0,j=0;
	for(i=0;i<16;i++)
	{
		TK[0][i]=Key1[i]^Tweak[i];
		TK[1][i]=Key2[i]^Tweak[i];
		TK[2][i]=Key1[i]^Tweak[Q[i]];
		TK[3][i]=Key2[i]^Tweak[Q[i]];
	}

	
}

void Round(int r, int Stt[])
{
	
	int i=0;
	for(i=0;i<4;i++)//MixColumn
	{
		Stt[i]^=(Stt[i+8]^Stt[i+12]);
		Stt[i+4]^=Stt[i+12];
	}

	int ind=r;
	

	Stt[4]^=RC4[ind];//AddConstant
	Stt[5]^=RC3[ind];

	for(i=0;i<16;i++)//AddTweakey
		Stt[i]^=TK[ind%4][i];

	if(r!=31)
	{
		int Temp[16];
		for(int i=0;i<16;i++)//Permutation
			Temp[P[i]]=Stt[i];

		for(i=0;i<16;i++)//SBox
			Stt[i]=S[Temp[i]];
	}
}

int main()
{

	printf("CRAFT\n");
	FILE *fp;
	FILE *fp1;
	fp1=fopen("data1","rb");
	unsigned _int64 m=0,m1=0,c=0,c1=0,temp=0,key1=0,key2=0;
	unsigned _int8 Stt[16]={0},Stt1[16]={0},count=0,Key1[16]={0},Key2[16]={0};
	int r=0,i=0,j=0,k=0,flag=0,sum=0;
	for(k=0;k<1000;k++)
	{
		
		if(fp1==NULL)
			{
				printf("Can't open the file\n");
				exit(EXIT_FAILURE);
			}
		fread(&key1,sizeof(unsigned _int64),1,fp1);
		fread(&key2,sizeof(unsigned _int64),1,fp1);
		
		printf("%I64x,%I64x:",key1,key2);
		for(j=0;j<16;j++)
			{
				Key1[j]=(key1>>(60-4*j))&0xf;
				Key2[j]=(key2>>(60-4*j))&0xf;
			}
		Initialize_key(Key1,Key2,4);
		count=0;
		fp=fopen("data","rb");
		for(i=0;i<0x80000000;i++)
		{
			c=0;
			c1=0;
			if(fp==NULL)
			{
				printf("Can't open the file\n");
				exit(EXIT_FAILURE);
			}
			fread(&m,sizeof(unsigned _int64),1,fp);
			m1=m^0xa0a0a00000a0a;  //
			//m=m^key1^key2;
			//m1=m1^key1^key2;
			for(j=0;j<16;j++)
			{
				Stt[j]=(m>>(60-4*j))&0xf;
				Stt1[j]=(m1>>(60-4*j))&0xf;
			}
			for(r=0;r<4;r++)
			{
				Round(r,Stt);
				Round(r,Stt1);
			}
			for(j=0;j<16;j++)
			{
				c^=unsigned _int64(Stt[j])<<(60-4*j);
				c1^=unsigned _int64(Stt1[j])<<(60-4*j);
				
			}
			temp=c^c1;
			if(temp==0xaa00a00)
			{
				count++;
			}
			
		}
		fclose(fp);
		if(count!=0)
			flag++;
		sum+=count;
		printf("	i=%d,count=%d,sum=%d\n",k,count,sum);
	}
	fclose(fp1);
	printf("%d,%d",flag,sum);
	system("pause");
	return 0;
}



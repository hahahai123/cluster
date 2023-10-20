#include<stdio.h>
#include<time.h>
#include<iostream.h>
#include<stdlib.h>
const int S[16]={0xc,0xa,0xd,0x3,0xe,0xb,0xf,0x7,0x8,0x9,0x1,0x5,0x0,0x2,0x4,0x6};
const int P[16]={0,10,5,15,14,4,11,1,9,3,12,6,7,13,2,8};

const unsigned _int8 a[19][16] =
	{
		0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,
		0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,
		1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,
		0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,
		0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,
		1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,
		0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,
		0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,
		1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,
		0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,
		0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,
		0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,
		0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,
		1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,
		1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,0,
		0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,
		0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,
		0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,
		0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,

	};



//Midori



int TK[4][16];

void Initialize_key(unsigned _int8 Key1[], unsigned _int8 Key2[],int r)
{
	
	
	int i=0,j=0;
	for(i=0;i<r;i++)
	{
		if((i%2)==0)
		{
			for(j=0;j<16;j++)
				TK[i][j]=Key1[j]^a[i][j];
		}
		else
		{
			for(j=0;j<16;j++)
				TK[i][j]=Key2[j]^a[i][j];
		}
	}
	
}

void Round(int r, unsigned _int8 Stt[])
{
	
	int i=0;
	for(i=0;i<16;i++)//SBox
		Stt[i]=S[Stt[i]];
	int Temp[16]={0};
	if(r!=15)
	{
		for(int i=0;i<16;i++)//Permutation
			Temp[i]=Stt[P[i]];

		for(i=0;i<16;i=i+4)//MixColumn
		{
			Stt[i]=Temp[i+1]^Temp[i+2]^Temp[i+3];
			Stt[i+1]=Temp[i]^Temp[i+2]^Temp[i+3];
			Stt[i+2]=Temp[i]^Temp[i+1]^Temp[i+3];
			Stt[i+3]=Temp[i]^Temp[i+1]^Temp[i+2];
		}
		for(i=0;i<16;i++)//AddTweakey
			Stt[i]^=TK[r][i];
	}

	
}

int main()
{
	printf("Midori\n");
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
			m1=m^0x2000200000200020;  //
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
			if(temp==0x0222022222022202)
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





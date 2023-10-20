#include<stdio.h>
#include<time.h>
#include<iostream.h>
#include<stdlib.h>
const int S[16]={0xc,0x6,0x9,0x0,0x1,0xa,0x2,0xb,0x3,0x8,0x5,0xd,0x4,0xe,0x7,0xf};
const int P[16]={9,15,8,13,10,14,12,11,0,1,2,3,4,5,6,7};
const int RC0[32]={0x1,0x3,0x7,0xf,0xf,0xe,0xd,0xb,0x7,0xf,0xe,0xc,0x9,0x3,0x7,0xe,
				0xd,0xa,0x5,0xb,0x6,0xc,0x8,0x0,0x1,0x2,0x5,0xb,0x7,0xe,0xc,0x8};
const int RC1[32]={0x0,0x0,0x0,0x0,0x1,0x3,0x3,0x3,0x3,0x2,0x1,0x3,0x3,0x3,0x2,0x0,
				0x1,0x3,0x3,0x2,0x1,0x2,0x1,0x3,0x2,0x0,0x0,0x0,0x1,0x2,0x1,0x3};



//CRAFT



int TK[32][16];

void Initialize_key(int Key[],int r)
{
	int i=0,j=0;
	for(i=0;i<16;i++)
	{
		TK[0][i]=Key[i];
	}
	for(i=1;i<r;i++)
	{
		for(j=0;j<16;j++)
		{
			TK[i][j]=TK[i-1][P[j]];
		}
	}
	
}

void Round(int r, int Stt[])
{
	
	int i=0;
	for(i=0;i<16;i++)//SBox
		Stt[i]=S[Stt[i]];

	Stt[0]^=RC0[r];//AddConstant
	Stt[4]^=RC1[r];
	Stt[8]^=0x2;

	for(i=0;i<8;i++)   //Addtk
	{
		Stt[i]=Stt[i]^TK[r][i];
	}
	
	int Temp[16]={0};    //shiftrow
	for(i=0;i<4;i++)
	{
		Temp[i]=Stt[i];
		Temp[i+4]=Stt[((i+3)%4)+4];
		Temp[i+8]=Stt[((i+2)%4)+8];
		Temp[i+12]=Stt[((i+1)%4)+12];
	}	
	for(i=0;i<4;i++)//MixColumn
	{
		Stt[i]=Temp[i]^Temp[i+8]^Temp[i+12];
		Stt[i+4]=Temp[i];
		Stt[i+8]=Temp[i+4]^Temp[i+8];
		Stt[i+12]=Temp[i]^Temp[i+8];
	}	

	
}

int main()
{
	
	FILE *fp;
	FILE *fp1;
	fp1=fopen("data1","rb");
	unsigned _int64 m=0,m1=0,c=0,c1=0,temp=0,key=0;
	int Stt[16]={0},Stt1[16]={0},count=0,Key[16]={0},flag=0,sum=0;
	int r=0,i=0,j=0,k=0;
	for(k=0;k<1000;k++)
	{
		
		if(fp1==NULL)
			{
				printf("Can't open the file\n");
				exit(EXIT_FAILURE);
			}
		fread(&key,sizeof(unsigned _int64),1,fp1);
		//fread(&key2,sizeof(unsigned _int64),1,fp1);
		
		printf("%I64x:",key);
		for(j=0;j<16;j++)
			{
				Key[j]=(key>>(60-4*j))&0xf;
			}
		Initialize_key(Key,6);
		count=0;
		fp=fopen("data","rb");
		for(i=0;i<0x80000000;i++)   //0x80000000
		{
			c=0;
			c1=0;
			if(fp==NULL)
			{
				printf("Can't open the file\n");
				exit(EXIT_FAILURE);
			}
			fread(&m,sizeof(unsigned _int64),1,fp);
			m1=m^0x100000010110;
			for(j=0;j<16;j++)
			{
				Stt[j]=(m>>(60-4*j))&0xf;
				Stt1[j]=(m1>>(60-4*j))&0xf;
			}
			for(r=0;r<6;r++)
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
			if(temp==0x5555050000550555)
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



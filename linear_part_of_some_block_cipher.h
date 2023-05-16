#include<stdio.h>

int rotation(unsigned _int16 a,int t)     //4-bit left rotation
{
	a=((a<<t)&0xf)^((a>>(4-t))&0xf);
	return a;
}

int weight(unsigned _int16 a)           //Calculate the weight of 16-bit vector
{
	int count=0,i;
	for(i=0;i<16;i++)
	{
		if(((a>>i)&1)==1)
			count++;
	}
	return count;
}


int CRAFT(unsigned _int16 a)         //the linear part of CRAFT-64
{
	unsigned _int16 b[4]={0},d[4]={0};

	b[0]=(a>>12)&0xf;
	b[1]=(a>>8)&0xf;
	b[2]=(a>>4)&0xf;
	b[3]=a&0xf;

	d[0]=b[0]^b[2]^b[3];
	d[1]=b[1]^b[3];
	d[2]=b[2];
	d[3]=b[3];

	b[0]=rotation(d[0],1);
	b[1]=((d[1]<<2)&0x8)^((d[1]>>2)&0x2)^(d[1]&0x5);
	b[2]=((d[2]<<2)&0x8)^((d[2]>>2)&0x2)^(d[2]&0x5);
	b[3]=rotation(d[3],3);

	d[0]=b[3];
	d[1]=b[2];
	d[2]=b[1];
	d[3]=b[0];

	a=(d[0]<<12)^(d[1]<<8)^(d[2]<<4)^d[3];
	
	return a;
}

int Midori(unsigned _int16 a)    //the linear part of Midori-64
{
	unsigned _int16 b[4]={0},d[4]={0};

	b[0]=(a>>12)&0xf;
	b[1]=(a>>8)&0xf;
	b[2]=(a>>4)&0xf;
	b[3]=a&0xf;

	d[0]=(b[0]&0x8)^((b[2]<<2)&0x4)^(b[1]&0x2)^((b[3]>>2)&0x1);
	d[1]=((b[2]<<2)&0x8)^(b[0]&0x4)^((b[3]>>2)&0x2)^(b[1]&0x1);
	d[2]=((b[1]<<1)&0x8)^((b[3]<<1)&0x4)^((b[0]<<1)&0x2)^((b[2]>>3)&0x1);
	d[3]=((b[3]<<3)&0x8)^((b[1]>>1)&0x4)^((b[2]>>1)&0x2)^((b[0]>>1)&0x1);

	b[0]=d[1]^d[2]^d[3];
	b[1]=d[0]^d[2]^d[3];
	b[2]=d[0]^d[1]^d[3];
	b[3]=d[0]^d[1]^d[2];
			
	a=(b[0]<<12)^(b[1]<<8)^(b[2]<<4)^b[3];

	return a;
}

int SKINNY(unsigned _int16 a)    //the linear part of SKINNY-64
{
	unsigned _int16 b[4]={0},d[4]={0};

	b[0]=(a>>12)&0xf;
	b[1]=(a>>8)&0xf;
	b[2]=(a>>4)&0xf;
	b[3]=a&0xf;

	b[1]=rotation(b[1],1);
	b[2]=rotation(b[2],2);
	b[3]=rotation(b[3],3);

	d[0]=b[0]^b[2]^b[3];
	d[1]=b[0];
	d[2]=b[1]^b[2];
	d[3]=b[0]^b[2];

	a=(d[0]<<12)^(d[1]<<8)^(d[2]<<4)^d[3];

	return a;
}


#include <stdio.h>
#include <string.h>
char p[1024];
double epoch[6] = {2019,10,29,6,43,40};
double pos[6] = {-2754345.1308808499,4694375.4283943009,3314127.1950564152,-0.017269137546180629,0.028483990070880948,\
0.0094418283500022002};
int num = 14;
char test = 0;
char test_d[20];
 void main()
 {
	double dms1[2] = {20.0,60.0};
	for(int j = 0;j<10000;j++)
	{
		sprintf(test_d,"%010.7lf",dms1[0] + dms1[1] / 60.0);
		printf("%s\n",test_d);
	}
	return;
//	sprintf(p, "$GPGGA,%f,%02.0f%02.0f%05.2f,%02.0f%010.7f,%s",		
//		test,7.0,24.0,0.0,31.0,255.0,"\0");
	double test = 10.12345678901234567890;
	sprintf(p,"%10.7f",test);
	printf("%s",p);
	sprintf(p,"%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\
\n", \
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai",\
	"dai","dai","dai","dai","dai","dai","dai","dai","dai","dai"\
	);
	printf("%s\n",p);
	for (int j=0;j<sizeof(p);j++)
	{
		//printf("p[%d] = %d\n",j,p[j]);
	}
 }
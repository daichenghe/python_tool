#include "com.h" 
#define BUFFER_SIZE 1200      /*最大缓存区*/
char *pstr[]={"NO1\n","NO2\n","NO3\n","NO4\n"}; 
int main(int argc, char *argv[])
{
	int fd;
	int i;
	char read_buffer[BUFFER_SIZE];
	int read_buffer_size;
	//打开串口
	fd = open_port(0);
	//设置串口
    if(set_com_config(fd, 115200, 8, 'N', 1) < 0) /* 配置串口 */ 
    { 
        perror("set_com_config"); 
        return 1; 
    } 
	//发送数据
	int rc,nread=0;
    fd_set rset;
    struct timeval tv;
    unsigned char buf[1024] = {0};
    int read_status = 0;
	int portfd = -1;
	portfd = fd;
	printf("fd = %d\n",fd);
#if 1
    while(1)
    {
        FD_ZERO(&rset);
        FD_SET(fd,&rset);

        tv.tv_sec = 15;
        tv.tv_usec = 0;

        rc = select(fd+1,&rset,NULL,NULL,&tv);
        if(rc == -1)
        {
            continue;
        }
        if(rc == 0)
        {
            continue;
        }
        else
        {
			memset(buf,0, sizeof(buf));
			read_buffer_size = read(fd, buf, sizeof(buf));		
			printf("read_buffer_size = %d\n",read_buffer_size);
			printf("read[%d][%s]\n",  read_buffer_size,buf);
            //nread = read(fd,buf,sizeof(buf));   
            if(nread == -1)
            {
                perror("read");
                usleep(10*1000);
                continue;
            }
            if(nread == 0)
            {
                printf("nread==0\n");
                usleep(10*1000);
                continue;
            }
			write(fd, buf, read_buffer_size);
			
        }
		//usleep(5*1000);
    }//END_while
#endif
#if 0
	do{
		do{
			memset(read_buffer,0, BUFFER_SIZE);
			read_buffer_size = read(fd, read_buffer, BUFFER_SIZE);				
		}while(!read_buffer_size);
		write(fd, read_buffer, read_buffer_size);
		printf("read[%d][%s]\n",  read_buffer_size,read_buffer);
	}while(1);
#endif
	close(fd);
	return 0;
}

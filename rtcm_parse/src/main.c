#include "tool.h"
#include "RingBuffer.h"
#include <stdio.h>
#include <stdlib.h>

#define F_PATH  "./rtcm_data"
rtcm_t rtcm_to_save_data ;
int count = 0;
int all_d3 = 0;
int valid_data = 0;
int useful_data = 0;
void main()
{
	FILE* fs = fopen(F_PATH,"rb");
    char ch = 0;
	while(1)
	{
        if(fs!=NULL)
        {
		    ch=fgetc(fs);
        }
        //printf("ch = %x\n",ch);
        count ++;
        if(feof(fs))
		{
			printf("file end\n");
            printf("all_d3 = %d\n",all_d3);
            printf("valid_data = %d\n",valid_data);

            printf("useful_data = %d\n",useful_data);
            printf("count = %d",count);
			//return;
            fclose(fs);
		}
        //else
        {
            int ret_val = input_rtcm3_data(&rtcm_to_save_data, ch);
            if (ret_val == 1)    //完整数据
            {
                valid_data++ ;
                printf("type = %d\n",rtcm_to_save_data.type);
                switch (rtcm_to_save_data.type)
                {

                    case 1006:
                        //printf("rev!\r\n");
                    case 1001:
                    case 1002:
                    case 1003:
                    case 1004:
                    case 1005:
                    
                    case 1007:
                    case 1008:
                    case 1009:
                    case 1010:
                    case 1011:
                    case 1012:
                    case 1013:
                    case 1019:
                    case 1020:
                    case 1021:
                    case 1022:
                    case 1023:
                    case 1024:
                    case 1025:
                    case 1026:
                    case 1027:
                    case 1029:
                    case 1030:
                    case 1031:
                    case 1032:
                    case 1033:
                    case 1034:
                    case 1035:
                    case 1037:
                    case 1038:
                    case 1039:
                    case 1042:
                    case 1044:
                    case 1045:
                    case 1046:
                    case 63:
                    case 4001:
                    case 1071:
                    case 1072:
                    case 1073:
                    case 1074:      //时间
                    case 1075:
                    case 1076:
                    case 1077:
                    case 1081:
                    case 1082:
                    case 1083:
                    case 1084:
                    case 1085:
                    case 1086:
                    case 1091:
                    case 1092:
                    case 1093:
                    case 1094:
                    case 1095:
                    case 1096:
                    case 1097:
                    case 1101:
                    case 1102:
                    case 1103:
                    case 1104:
                    case 1105:
                    case 1106:
                    case 1107:
                    case 1111:
                    case 1112:
                    case 1113:
                    case 1114:
                    case 1115:
                    case 1116:
                    case 1117:
                    case 1121:
                    case 1122:
                    case 1123:
                    case 1124:
                    case 1125:
                    case 1126:
                    case 1127:
                    case 1230:
                    case 1087:
                        useful_data++;
						//printf("receive!\n");
                        break;
                    default:
                        break;
                }
			}
		}
	}
}


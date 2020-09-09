#include "handle_data.h"


/*
 *去除字符串右端空格
 */
char *strtrimr(char *pstr)
{
    int i;
    i = strlen(pstr) - 1;
    while(isspace(pstr[i]) && (i >= 0))
    { pstr[i--] = '\0'; }
    return pstr;
}
/*
 *去除字符串左端空格
 */
char *strtriml(char *pstr)
{
    int i = 0, j;
    j = strlen(pstr) - 1;
    while(isspace(pstr[i]) && (i <= j))
    { i++; }
    if(0 < i)
    { strcpy(pstr, &pstr[i]); }
    return pstr;
}
/*
 *去除字符串两端空格
 */
char *strtrim(char *pstr)
{
    char *p;
    p = strtrimr(pstr);
    return strtriml(p);
}


/*
 *从文件的一行读出key或value,返回item指针
 *line--从配置文件读出的一行
 */
int  get_item_from_line(char *line,  ITEM *item)  
{
    char *p = strtrim(line);
    int len = strlen(p);
    if(len <= 0)
    {
        return 1;//空行
    }
    else if(p[0] == '#')
    {
        return 2;
    }
    else
    {
        char *p2 = strchr(p, '=');
        *p2++ = '\0';
        item->key = (char *)malloc(strlen(p) + 1);
        item->value = (char *)malloc(strlen(p2) + 1);
        strcpy(item->key, p);
        strcpy(item->value, p2);

    }
    return 0;//查询成功
}


int file_to_items(const char *file,  ITEM *items,  int *num)
{
    char line[2048];
    FILE *fp;
    fp = fopen(file, "r");
    if(fp == NULL)
    { return 1; }
    int i = 0;
    while(fgets(line, 2047, fp))
    {
        char *p = strtrim(line);
        int len = strlen(p);
        if(len <= 0)
        {
            continue;
        }
        else if(p[0] == '#')
        {
            continue;
        }
        else
        {
            char *p2 = strchr(p, '=');
            /*这里认为只有key没什么意义*/
            if(p2 == NULL)
            { continue; }
            *p2++ = '\0';
            items[i].key = (char *)malloc(strlen(p) + 1);
            items[i].value = (char *)malloc(strlen(p2) + 1);
            strcpy(items[i].key, p);
            strcpy(items[i].value, p2);

            i++;
        }
    }
    (*num) = i;
    fclose(fp);
    return 0;
}

FILE *read_conf_pre(const char *file)
{
    FILE *fp =NULL ;
    fp = fopen(file, "r");
    return fp;

}
int read_conf_ok(FILE *fp)
{
    fclose(fp);
    fp= NULL;
}

long  read_timer_value(const char *key,  FILE *fp)    
{
    char line[2048];
    int value = 0;
    if(fp == NULL)
    {
        return -1;
    }
    //fgets(line, 2047, fp);
    if(fgets(line, 2047, fp) != NULL)
    {
        ITEM item;

        get_item_from_line(line, &item);
		
		//printf("item.key = %s\n",item.key);
		//printf("item.value = %s\n",item.value);
		//printf("key = %s\n",key);
        if(strcmp(item.key, key) == 0)
        {
			//printf("match\n");
            value = atoi(item.value);
            //printf("value = %lf\n",value);
            free(item.key);
            free(item.value);
            //break;
        }
        else
        {
            //printf("not match\n");
        }
    }
    else
    {
        printf("file end\n");
    }
    
    return value;
}


float read_ins_value(const char *key,  FILE *fp)    
{
    char line[2048];
    float value = 0;
    int rec = -1;
    if(fp == NULL)
    {
        return -1;
    }
    if(fgets(line, 2047, fp) != NULL)
    {
        ITEM item;

        get_item_from_line(line, &item);
		
		//printf("item.key = %s\n",item.key);
		//printf("item.value = %s\n",item.value);
		//printf("key = %s\n",key);
        if(strcmp(item.key, key) == 0)
        {
            value = atof(item.value);
            free(item.key);
            free(item.value);
            //break;
        }
        else
        {
            printf("not match\n");
        }
    }
    else
    {
        printf("file end\n");
    }
    
    return value;
}


void read_gps_data(const char *key,  FILE *fp,char* gps_data)    //read_conf_value("avm3dscreen_width",     fp)
{
    char line[2048];
    float value = 0;
    if(fp == NULL)
    {
        return -1;
    }
    //fgets(line, 2047, fp);
    if(fgets(line, 2047, fp) != NULL)
    {
        ITEM item;

        get_item_from_line(line, &item);
		
		//printf("item.key = %s\n",item.key);
		//printf("item.value = %s\n",item.value);
		//printf("key = %s\n",key);
        if(strcmp(item.key, key) == 0)
        {
            //value = atof(item.value);
            strcpy(gps_data,item.value);
            free(item.key);
            free(item.value);
            //break;
        }
        else
        {
            printf("not match\n");
        }
    }
    else
    {
        printf("file end\n");
    }
    //return value;
}

FILE *write_conf_pre(const char *file)
{
    FILE *fp;
    fp = fopen(file, "w");
    return fp;

}
int write_conf_value(const char *key, float value, FILE *fp)
{
    char a[30] = {'\0'};

    sprintf(a, "%.4f", value);
    fprintf(fp, "%s=%s\n", key, a);
    return 0;
}

int write_conf_ok(FILE *fp)
{
    fclose(fp);
}
Target = ./rtcm_parse
INC += -I./
APPDIR=./

ARFLAGS = rcs
LIBS = 


ifndef TG
	#TG=ARM
	TG=PC
endif

ifeq "$(TG)" "PC"
CC = gcc -std=c99
CPP = gcc -std=c99
AR = ar
else
CC = arm-none-eabi-gcc -std=c99
CPP = arm-none-eabi-gcc  -std=c99
AR = arm-none-eabi-ar
CFLAGS += -mcpu=cortex-m4
endif


ifndef CFG
	CFG=Debug
	#CFG=Release
endif

ifndef TEST
	TEST=ENABLE
	#CFG=Release
endif

ifeq "$(CFG)" "Debug"
#CFLAGS += -w -o2
CFLAGS +=  -MMD  -w
else
CFLAGS += -W
CFLAGS += -o1
endif


ODJ_DIR:= $(shell mkdir -p build)
OUTDIR = ./build



#find all the sub-directory
VPATH=$(foreach dir,$(shell find . -type d),$(shell echo $(dir):))
#include all the sub-directory
INCLS=$(foreach dir,$(subst :, ,$(VPATH)),$(shell echo -I./$(dir)))
INC += $(INCLS)
#INC+= -I./include/


#find all .c and produce .o
C_SRC_PATH = $(foreach dir,$(subst :, ,$(VPATH)),$(wildcard $(dir)/*.c))
COBJS = $(subst .c,.o,$(C_SRC_PATH))
#find all .cxx and produce .o
CPP_SRC_PATH = $(foreach dir,$(subst :, ,$(VPATH)),$(wildcard $(dir)/*.cxx))
CPPOBJS = $(subst .cxx,.o,$(CPP_SRC_PATH))

OBJ=$(COBJS) $(CPPOBJS)

# 手动添加文件
#COMMON_OBJ = $(OUTDIR)/hello.o  
#$(Target) : $(SRCS)
#	gcc  -I $(INC) -o2 $(Target)   $(SRCS)  $(LIBS) -g

#OBJ=$(COMMON_OBJ)

COMPILE = @$(CC)  $(INC) $(LIBS)    $(CFLAGS) -c $<   -o  $@                              #"$(OUTDIR)/$(*F).o"

CDEF = $(OBJ:.o=.d)

all: $(Target)

$(OBJ):
# Pattern rules



#$(OUTDIR)/%.o : $(APPDIR)/%.c
#	@echo ""
#	@echo "->>>>>>>> compile " $@
#	$(COMPILE)


$(COBJS):%.o:%.c
	@echo ""
	@echo "->>>>>>>> compile " $@
	$(COMPILE)
        

LINK =	@$(CC) $(OBJ) $(LIBS) $(INC)  -o $(Target)



# Build rules
$(Target): $(OUTDIR)  $(OBJ)
	$(LINK)
#	cp $(Target) ./
	@echo "->>>>>>>> gen " $(Target)
ifeq "$(CFG)" "Debug"
	@echo "Debug" 
else
	@echo "Release" 
endif
	@echo "+++++++++++++++++++++++++"
	@echo "+++++++++++++++++++++++++"
clean:            
	rm $(Target) $(OBJ) $(CDEF)


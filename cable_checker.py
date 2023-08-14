import RPi.GPIO as gpio
import time as local

gpio.setmode(gpio.BOARD)

####################   GPIO DECLARATION ###################

LED_GREEN_OUT = 27
LED_RED_OUT = 28

# connector 1 TX GPIO config
CAN_H = 3
CAN_L = 5
LV = 7
BROWN_GND = 11
HV = 13
BLACK_GND = 15

#connector 2 RX GPIO config
CAN_H_RX1 = 19
CAN_L_RX1 = 21
LV_RX1 = 23
BROWN_GND_RX1 = 29
HV_RX1 = 31
BLACK_GND_RX1 = 33

#connector 3 RX GPIO config
CAN_H_RX2 = 12
CAN_L_RX2 = 16
LV_RX2 = 18
BROWN_GND_RX2 = 22
HV_RX2 = 24
BLACK_GND_RX2 = 26

#########################################################

####################   GPIO SETUP #######################
# setup TX pins
gpio.setup(CAN_H, gpio.OUT)
gpio.setup(CAN_L, gpio.OUT)
gpio.setup(LV, gpio.OUT)
gpio.setup(BROWN_GND, gpio.OUT)
gpio.setup(HV, gpio.OUT)
gpio.setup(BLACK_GND, gpio.OUT)

#setup RX1 pins
gpio.setup(CAN_H_RX1, gpio.IN)
gpio.setup(CAN_L_RX1, gpio.IN)
gpio.setup(LV_RX1, gpio.IN)
gpio.setup(BROWN_GND_RX1, gpio.IN)
gpio.setup(HV_RX1, gpio.IN)
gpio.setup(BLACK_GND_RX1, gpio.IN)

#setup RX2 pins
gpio.setup(CAN_H_RX2, gpio.IN)
gpio.setup(CAN_L_RX2, gpio.IN)
gpio.setup(LV_RX2, gpio.IN)
gpio.setup(BROWN_GND_RX2, gpio.IN)
gpio.setup(HV_RX2, gpio.IN)
gpio.setup(BLACK_GND_RX2, gpio.IN)

#LED
gpio.setup(LED_GREEN_OUT, gpio.OUT)
gpio.setup(LED_RED_OUT, gpio.OUT)

#########################################################

################## GPIO_TX ##############################

#local variable declaration
CAN_H_TX_US = 2000 #units in us  
CAN_L_TX_US = 4000 #units in us 
LV_TX_US = 6000 #units in us 
BROWN_GND_TX_US = 8000 #units in us 
HV_TX_US = 10000 #units in us
BLACK_GND_TX_US = 12000 #units in us 

#local variable declaration
CAN_H_TX_start = 0 #units in us  
CAN_L_TX_start = 0 #units in us 
LV_TX_start = 0 #units in us 
BROWN_GND_TX_start = 0 #units in us 
HV_TX_start = 0 #units in us
BLACK_GND_TX_start = 0 #units in us 

#local variable declaration
CAN_H_TX_end = 0 #units in us  
CAN_L_TX_end = 0 #units in us 
LV_TX_end = 0 #units in us 
BROWN_GND_TX_end = 0 #units in us 
HV_TX_end = 0 #units in us
BLACK_GND_TX_end = 0 #units in us 

def GPIO_TX(time_us):
    timestamp = int(time_us)
    #CAN_H
    if(CAN_H_TX_start == 0):
        if(timestamp - CAN_H_TX_end > 2000):
            CAN_H_TX_start = timestamp
            CAN_H_TX_end = 0
            gpio.output(CAN_H, gpio.HIGH)
    elif(timestamp - CAN_H_TX_start > CAN_H_TX_US):
        CAN_H_TX_end = timestamp
        CAN_H_TX_start = 0
        gpio.output(CAN_H, gpio.LOW)

    #CAN_L
    if(CAN_L_TX_start == 0):
        if(timestamp - CAN_L_TX_end > 2000):
            CAN_L_TX_start = timestamp
            CAN_L_TX_end = 0
            gpio.output(CAN_L, gpio.HIGH)
    elif(timestamp - CAN_L_TX_start > CAN_L_TX_US):
        CAN_L_TX_end = timestamp
        CAN_L_TX_start = 0
        gpio.output(CAN_L, gpio.LOW)

    #LV
    if(LV_TX_start == 0):
        if(timestamp - LV_TX_end > 2000):
            LV_TX_start = timestamp
            LV_TX_end = 0
            gpio.output(LV, gpio.HIGH)
    elif(timestamp - LV_TX_start > LV_TX_US):
        LV_TX_end = timestamp
        LV_TX_start = 0
        gpio.output(LV, gpio.LOW)

    #BROWN_GND
    if(BROWN_GND_TX_start == 0):
        if(timestamp - BROWN_GND_TX_end > 2000):
            BROWN_GND_TX_start = timestamp
            BROWN_GND_TX_end = 0
            gpio.output(BROWN_GND, gpio.HIGH)
    elif(timestamp - BROWN_GND_TX_start > BROWN_GND_TX_US):
        BROWN_GND_TX_end = timestamp
        BROWN_GND_TX_start = 0
        gpio.output(BROWN_GND, gpio.LOW)

    #HV
    if(HV_TX_start == 0):
        if(timestamp - HV_TX_end > 2000):
            HV_TX_start = timestamp
            HV_TX_end = 0
            gpio.output(HV, gpio.HIGH)
    elif(timestamp - HV_TX_start > HV_TX_US):
        HV_TX_end = timestamp
        HV_TX_start = 0
        gpio.output(HV, gpio.LOW)

    #BLACK_GND
    if(BLACK_GND_TX_start == 0):
        if(timestamp - BLACK_GND_TX_end > 2000):
            BLACK_GND_TX_start = timestamp
            BLACK_GND_TX_end = 0
            gpio.output(BLACK_GND, gpio.HIGH)
    elif(timestamp - BLACK_GND_TX_start > BLACK_GND_TX_US):
        BLACK_GND_TX_end = timestamp
        BLACK_GND_TX_start = 0
        gpio.output(BLACK_GND, gpio.LOW)


#########################################################

################## GPIO_RX1 ##############################

#local variable declaration
CAN_H_RX1_start = 0 #units in us  
CAN_L_RX1_start = 0 #units in us 
LV_RX1_start = 0 #units in us 
BROWN_GND_RX1_start = 0 #units in us 
HV_RX1_start = 0 #units in us
BLACK_GND_RX1_start = 0 #units in us 

#local variable declaration
CAN_H_RX1_end = 0 #units in us  
CAN_L_RX1_end = 0 #units in us 
LV_RX1_end = 0 #units in us 
BROWN_GND_RX1_end = 0 #units in us 
HV_RX1_end = 0 #units in us
BLACK_GND_RX1_end = 0 #units in us 

def GPIO_RX1(time_us):
    timestamp = int(time_us)
    #CAN_H
    if(gpio.input(CAN_H)):
        if(CAN_H_RX1_start == 0):
            CAN_H_RX1_start = timestamp
    else :
        if(CAN_H_RX1_start != 0):
            CAN_H_RX1_end = timestamp - CAN_H_RX1_start
            CAN_H_RX1_start = 0

    #CAN_L
    if(gpio.input(CAN_L)):
        if(CAN_L_RX1_start == 0):
            CAN_L_RX1_start = timestamp
    else :
        if(CAN_L_RX1_start != 0):
            CAN_L_RX1_end = timestamp - CAN_L_RX1_start
            CAN_L_RX1_start = 0
    #LV
    if(gpio.input(LV)):
        if(LV_RX1_start == 0):
            LV_RX1_start = timestamp
    else :
        if(LV_RX1_start != 0):
            LV_RX1_end = timestamp - LV_RX1_start
            LV_RX1_start = 0

    #BROWN_GND
    if(gpio.input(BROWN_GND)):
        if(BROWN_GND_RX1_start == 0):
            BROWN_GND_RX1_start = timestamp
    else :
        if(BROWN_GND_RX1_start != 0):
            BROWN_GND_RX1_end = timestamp - BROWN_GND_RX1_start
            BROWN_GND_RX1_start = 0

    #HV
    if(gpio.input(HV)):
        if(HV_RX1_start == 0):
            HV_RX1_start = timestamp
    else :
        if(HV_RX1_start != 0):
            HV_RX1_end = timestamp - HV_RX1_start
            HV_RX1_start = 0

    #BLACK_GND
    if(gpio.input(BLACK_GND)):
        if(BLACK_GND_RX1_start == 0):
            BLACK_GND_RX1_start = timestamp
    else :
        if(BLACK_GND_RX1_start != 0):
            BLACK_GND_RX1_end = timestamp - BLACK_GND_RX1_start
            BLACK_GND_RX1_start = 0

#########################################################

################## GPIO_RX2 ##############################

#local variable declaration
CAN_H_RX2_start = 0 #units in us  
CAN_L_RX2_start = 0 #units in us 
LV_RX2_start = 0 #units in us 
BROWN_GND_RX2_start = 0 #units in us 
HV_RX2_start = 0 #units in us
BLACK_GND_RX2_start = 0 #units in us 

#local variable declaration
CAN_H_RX2_end = 0 #units in us  
CAN_L_RX2_end = 0 #units in us 
LV_RX2_end = 0 #units in us 
BROWN_GND_RX2_end = 0 #units in us 
HV_RX2_end = 0 #units in us
BLACK_GND_RX2_end = 0 #units in us 

def GPIO_RX2(time_us):
    timestamp = int(time_us)
    #CAN_H
    if(gpio.input(CAN_H)):
        if(CAN_H_RX2_start == 0):
            CAN_H_RX2_start = timestamp
    else :
        if(CAN_H_RX2_start != 0):
            CAN_H_RX2_end = timestamp - CAN_H_RX2_start
            CAN_H_RX2_start = 0

    #CAN_L
    if(gpio.input(CAN_L)):
        if(CAN_L_RX2_start == 0):
            CAN_L_RX2_start = timestamp
    else :
        if(CAN_L_RX2_start != 0):
            CAN_L_RX2_end = timestamp - CAN_L_RX2_start
            CAN_L_RX2_start = 0
    #LV
    if(gpio.input(LV)):
        if(LV_RX2_start == 0):
            LV_RX2_start = timestamp
    else :
        if(LV_RX2_start != 0):
            LV_RX2_end = timestamp - LV_RX2_start
            LV_RX2_start = 0

    #BROWN_GND
    if(gpio.input(BROWN_GND)):
        if(BROWN_GND_RX2_start == 0):
            BROWN_GND_RX2_start = timestamp
    else :
        if(BROWN_GND_RX2_start != 0):
            BROWN_GND_RX2_end = timestamp - BROWN_GND_RX2_start
            BROWN_GND_RX2_start = 0

    #HV
    if(gpio.input(HV)):
        if(HV_RX2_start == 0):
            HV_RX2_start = timestamp
    else :
        if(HV_RX2_start != 0):
            HV_RX2_end = timestamp - HV_RX2_start
            HV_RX2_start = 0

    #BLACK_GND
    if(gpio.input(BLACK_GND)):
        if(BLACK_GND_RX2_start == 0):
            BLACK_GND_RX2_start = timestamp
    else :
        if(BLACK_GND_RX2_start != 0):
            BLACK_GND_RX2_end = timestamp - BLACK_GND_RX2_start
            BLACK_GND_RX2_start = 0

#########################################################

###################### DECISION MAKING ##################

CAN_H_STATUS = 0
CAN_L_STATUS = 0
LV_STATUS = 0
BROWN_GND_STATUS = 0
HV_STATUS = 0
BLACK_GND_STATUS = 0

def process_states():
    #CAN_H    
    if((abs(CAN_H_RX1_end - CAN_H_TX_US) < 500) and (abs(CAN_H_RX2_end - CAN_H_TX_US) < 500)):
        CAN_H_STATUS = 1;
    else:
        CAN_H_STATUS = 0;   

    #CAN_L    
    if((abs(CAN_L_RX1_end - CAN_L_TX_US) < 500) and (abs(CAN_L_RX2_end - CAN_L_TX_US) < 500)):
        CAN_L_STATUS = 1;
    else:
        CAN_L_STATUS = 0;  

    #LV    
    if((abs(LV_RX1_end - LV_TX_US) < 500) and (abs(LV_RX2_end - LV_TX_US) < 500)):
        LV_STATUS = 1;
    else:
        CAN_H_STATUS = 0;  

    #BROWN_GND    
    if((abs(BROWN_GND_RX1_end - BROWN_GND_TX_US) < 500) and (abs(BROWN_GND_RX2_end - BROWN_GND_TX_US) < 500)):
        BROWN_GND_STATUS = 1;
    else:
        BROWN_GND_STATUS = 0;  

    #HV    
    if((abs(HV_RX1_end - HV_TX_US) < 500) and (abs(HV_RX2_end - HV_TX_US) < 500)):
        HV_STATUS = 1;
    else:
        HV_STATUS = 0;  

    #BLACK_GND    
    if((abs(BLACK_GND_RX1_end - BLACK_GND_TX_US) < 500) and (abs(BLACK_GND_RX2_end - BLACK_GND_TX_US) < 500)):
        BLACK_GND_STATUS = 1;
    else:
        BLACK_GND_STATUS = 0;  

    if((CAN_H_STATUS + CAN_L_STATUS + LV_STATUS + BROWN_GND_STATUS + HV_STATUS + BLACK_GND_STATUS) == 6):
        gpio.output(LED_GREEN_OUT, gpio.HIGH)
        gpio.output(LED_RED_OUT, gpio.LOW)
    else :
        gpio.output(LED_GREEN_OUT, gpio.LOW)
        gpio.output(LED_RED_OUT, gpio.HIGH)

#########################################################

while(True):
    time_now = int(local.time_ns()/1000)
    GPIO_TX(str(time_now))
    GPIO_RX1(str(time_now))
    GPIO_RX2(str(time_now))
    process_states()
    local.sleep(100/1000000); #sleep for 100us



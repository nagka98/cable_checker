## CABLE CHECKER PROGRAM

###ALGORITHM
- total 18 Gpio pins connected to Y cable with 6 pins each
- 18 GPIO pins are divided to 3 groups where one group sends out pulses and remaining observes pulses
- total 6 pulses with differential width of 2 ms to each other
- if GPIO counterpart reads exact width with 500us Tolerance, thats a proper connection
- proper connection is indicated with LED_GREEN, otherwise LED_RED

###HOW TO USE
- please include this in bashrc script, this would trigger program during powerup

###DISCLAIMER
- The code is written without any actual HW and other debugging tools, There might be minor warnings and issues during exectution
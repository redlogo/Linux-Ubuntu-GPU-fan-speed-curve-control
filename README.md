# Linux-Ubuntu-GPU-fan-speed-curve-control
this is a project that manages to tune the GPU fan speed as a function of temperature in Linux Ubuntu env

ALWAYS BE CAREFUL IF WANT TO PLAY WITH GPU FAN SPEED!

SCRIPTS MAY NOT BE WORKING DUE TO ENV ISSUES! 

DO NOT RELY ON IT UNLESS WHAT IS DOING BY THESE SCRIPTS IS TOTALLY UNDERSTOOD!

IF GPU IS RUNNING BUT FAN SPEED IS LOWER THAN IT SHOULD BE, THERE CAN BE SERIOUS CONSEQUENCE! BE WARE OF HOW TO SET PROPER FAN SPEED! DON'T DO THESE SCRIPTS UNLESS THESE CAN BE HANDLED FOR SURE! THESE SCRIPTS AND THIS REPOSITORY HAVE DEFINITELY NO RESPONSIBILITY FOR ANY MAL-FUNCTION OF POSSIBLE GPU DAMAGE AND HARDWARE DAMAGE AND ANY OTHER ISSUES AT ALL!

Manual:

fan-speed-curve-new-design.csv and fan-speed-curve-current.csv saves all the temperature v.s. fan-speed profile. First column is temperature, second column is GPU fan-speed.
1. change the fan-speed-curve-new-design.csv to get what is desired.
2. run in terminal 'python GPU-fan-control-tune-curve.py' to check if those changes in temperature-fan-speed curve is desired, a figure will be plotted (python matplotlib is required), and further tune the fan-speed-curve-new-design.csv and run the tune-curve.py again to get the desired results.
3. run in terminal 'python GPU-fan-control-deployment.py' to get the newer version of GPU-fan-control-execute.sh, at the same time, a figure of deployment conditions will be plotted (python matplotlib is required).
4. GPU-fan-control-execute.sh is the bash command to tell GPU when to speed up fan-speed and when to slow down.
5. hints: make the curve smooth will be much better than abrupt changes in fan-speed.

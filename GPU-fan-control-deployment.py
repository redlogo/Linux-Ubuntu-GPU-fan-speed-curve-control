"""RedLogo PERSONAL GPU fan speed curve tuning project
on Linux Ubuntu, GPU: GTX 1080 Ti"""
import matplotlib.pyplot as plt
import numpy as np
import os

os.system('rm -f fan-speed-curve-current.csv')
os.system('cp fan-speed-curve-new-design.csv fan-speed-curve-current.csv')
os.system('sleep 1')

new_profile_temperature = np.array([])
new_profile_fan_speed = np.array([])

fan_speed_curve_file_new_design = open('fan-speed-curve-current.csv', 'r')
for line in fan_speed_curve_file_new_design:
    line = line.strip()
    if line:
        line_split = line.split(',')
        new_profile_temperature = np.append(new_profile_temperature, line_split[0])
        new_profile_fan_speed = np.append(new_profile_fan_speed, line_split[1])
fan_speed_curve_file_new_design.close()

command_file = open('GPU-fan-control-execute.sh', 'w+')
command_file.write('#!/bin/bash\n')
# while do control. do this all the time
command_file.write('while true; do\n')
# sense the gpu temperature, thanks lots of trials/documentations from the website on how to use nvidia-smi
command_file.write('\tGTX1080Ti_temperature=$(nvidia-smi '
                   '--query-gpu=temperature.gpu --format=csv,noheader,nounits)\n\n')
command_file.write('\tcase "${GTX1080Ti_temperature}" in\n')
command_file.write('\t\t0[0-9])\n')
command_file.write('\t\t\tfan_speed="15"\n')
command_file.write('\t\t\t;;\n')
for i in range(len(new_profile_temperature)):
    command_file.write('\t\t' + new_profile_temperature[i] + ')\n')
    command_file.write('\t\t\tfan_speed="' + new_profile_fan_speed[i] + '"\n')
    command_file.write('\t\t\t;;\n')
command_file.write('\t\t' + '*' + ')\n')
command_file.write('\t\t\tfan_speed="' + '100' + '"\n')
command_file.write('\t\t\t;;\n')
command_file.write('\tesac\n\n')
# in case accidentally turn off the GPUFanControlState, make this parameter to be 1 every sense-and-set period
command_file.write('\tnvidia-settings -a "[gpu:0]/GPUFanControlState=1" >/dev/null\n')
command_file.write('\tnvidia-settings -a "[fan-0]/GPUTargetFanSpeed=${fan_speed}" >/dev/null\n\n')
command_file.write('\tsleep 1s\n\n')
command_file.write('done')
command_file.close()
# this is a must
os.system('chmod +x GPU-fan-control-execute.sh')

fig = plt.figure()
plt.plot(new_profile_temperature, new_profile_fan_speed, 'gx-', ms=5)
plt.title('RedLogo Linux Ubuntu GPU fan speed curves deployment - '
          'close this window and run execute.sh file to get it working!')
plt.legend(['fan speed profile has been be deployed'])
horizontal_lines = np.linspace(0, 100, 21)
for item in horizontal_lines:
    plt.axhline(item, color='grey', lw=0.5)
vertical_lines = np.linspace(0, 80, 41)
for item in vertical_lines:
    plt.axvline(item, color='grey', lw=0.5)
plt.xticks(np.arange(0, 82, 2))
plt.yticks(np.arange(0, 105, 5))

fig_manage = plt.get_current_fig_manager()
fig_manage.window.setGeometry(0, 0, 1500, 900)
plt.show()

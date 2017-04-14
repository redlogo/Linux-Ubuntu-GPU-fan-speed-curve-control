"""RedLogo PERSONAL GPU fan speed curve tuning project
on Linux Ubuntu, GPU: GTX 1080 Ti"""
import matplotlib.pyplot as plt
import numpy as np

old_profile_temperature = np.array([])
old_profile_fan_speed = np.array([])
new_profile_temperature = np.array([])
new_profile_fan_speed = np.array([])

fan_speed_curve_file_current = open('fan-speed-curve-current.csv', 'r')
for line in fan_speed_curve_file_current:
    line = line.strip()
    if line:
        line_split = line.split(',')
        old_profile_temperature = np.append(old_profile_temperature, line_split[0])
        old_profile_fan_speed = np.append(old_profile_fan_speed, line_split[1])
fan_speed_curve_file_current.close()

fan_speed_curve_file_new_design = open('fan-speed-curve-new-design.csv', 'r')
for line in fan_speed_curve_file_new_design:
    line = line.strip()
    if line:
        line_split = line.split(',')
        new_profile_temperature = np.append(new_profile_temperature, line_split[0])
        new_profile_fan_speed = np.append(new_profile_fan_speed, line_split[1])
fan_speed_curve_file_new_design.close()

fig = plt.figure()
plt.plot(old_profile_temperature, old_profile_fan_speed, 'ro-', ms=5)
plt.plot(new_profile_temperature, new_profile_fan_speed, 'gx-', ms=5)
plt.title('RedLogo Linux Ubuntu GPU fan speed curves')
plt.legend(['current fan speed profile', 'fan speed profile to be deployed'])
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

#
# Source of https://www.pitunnel.com/uninstall
#
# Copyright 2020 PiTunnel
# All Rights Reserved.
#

import subprocess
import os

print("\nShutting down any running instances of pitunnel and its agents")
# First shutdown using systemctl, for newer installations
try:
    subprocess.check_output('sudo systemctl stop pitunnel', stderr=subprocess.STDOUT, shell=True)
    subprocess.check_output('sudo systemctl disable pitunnel', stderr=subprocess.STDOUT, shell=True)
except:
    # Previous version was an older version or new installation.
    pass
# Then directly terminate any remaining proccesses incase of an older installation
pids = []
for app_name in ['pitunnel', 'monitor_device', 'wetty', 'ttyd', 'pitunnel_terminal', 'persistent_tunnel_manager','terminal_monitor','status_reporter','fixed_length_log','tunnel_log']:
    try:
        pids.extend(subprocess.check_output(["pidof", app_name], universal_newlines=True).strip().split(' '))
    except:
        pass
for pid in pids:
    try:
        subprocess.check_output('sudo kill -9 %s 2> /dev/null' % pid, shell=True)
    except:
        pass

print("Removing installations")
subprocess.call("rm -rf /usr/local/lib/tunnel_client", shell=True)
# Remove symbolic links
subprocess.call("rm -rf /usr/local/bin/pitunnel", shell=True)
subprocess.call("rm -rf /usr/local/bin/pitunnel_terminal", shell=True)

# Remove log and setting dirs
subprocess.check_output('rm -rf /etc/pitunnel', shell=True)
subprocess.check_output('rm -rf /var/log/pitunnel', shell=True)

# Delete existing rc.local entry, if we are upgrading from an old version of PiTunnel
if os.path.exists('/etc/rc.local'):
    print("Removing startup command")
    lines = []
    with open('/etc/rc.local', 'r') as f:
        for line in f:
            lines.append(line)
    # Backup the old rc.local
    subprocess.call('mv /etc/rc.local /etc/rc.local.bak', shell=True)
    with open('/etc/rc.local', 'w') as f:
        for line in lines:
            if 'pitunnel_start.conf' not in line:
                f.write(line)
    # Set the correct permissions on rc.local
    subprocess.call('chmod 755 /etc/rc.local', shell=True)

# Remove systemd service file
if os.path.exists('/etc/systemd/system/pitunnel.service'):
    subprocess.check_output('rm /etc/systemd/system/pitunnel.service', stderr=subprocess.STDOUT, shell=True)

print ("\n## Uninstall complete ##")
print('Please delete the device from the pitunnel.com website to complete the uninstall.')

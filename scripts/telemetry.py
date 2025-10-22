#!/usr/bin/env python
from datetime import datetime, timedelta, timezone
import subprocess
import random
import time

detector_id = ""
sleep_time = random.randint(0,600)
time.sleep(sleep_time)

output_str = subprocess.run("ps aux | grep read_mcp",shell=True,capture_output=True,text=True).stdout
if "read_mcp.rb" in output_str:
    running = "Running"
else:
    running = "Stopped"

date = datetime.now(timezone(timedelta(hours=+9),"JST")).strftime("%Y-%m-%d %H:%M:%S")
output_string = "date: {} JST, DAQ status: {}".format(date,running)
subprocess.run("ssh raindrop -o 'ConnectTimeout 5' 'echo {} >> ~/telemetry/efmlogger_{}.csv'".format(output_string,detector_id),shell=True)

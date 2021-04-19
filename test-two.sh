#!/bin/bash
ps aux | egrep "apache2|PID" | awk '{print $2"  "$4}' > archivo3s.cvs
cat archivo.cvs
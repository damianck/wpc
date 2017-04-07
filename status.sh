#!/bin/bash
for serverName in $@
do
ssh 175402@$serverName "uptime"
done 

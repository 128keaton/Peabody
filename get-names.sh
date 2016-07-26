#!/bin/sh
alias gam='python ~/GAM/gam.py'
for group in `gam print cros | grep -EiEio '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'`; do
		echo "$group"
done

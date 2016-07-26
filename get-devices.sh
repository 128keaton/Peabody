#!/bin/sh
alias gam='python ~/GAM/gam.py'
gam print cros > cros.csv
mysql --user="$user" --password="$password" --local_infile=1 Peabody -e "LOAD DATA LOCAL INFILE './cros.csv' INTO TABLE ChromeOS FIELDS TERMINATED BY ','"

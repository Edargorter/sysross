#!/bin/bash
#Update repository ... upgrade existing software

sudo apt update && sudo apt upgrade -y

#Requirements lists 
require="requirements.txt"
sec_require="security_requirements.txt"

#Install work requirements.txt from repo

pkgs=$(cat $require)
echo ${pkgs[0]}

for p in $pkgs; do
	echo "Package: $p"
	sudo apt install -y $p
done

#Install security requirements from repos

sec_pkgs=$(cat $sec_require)
echo ${sec_pkgs[0]}

printf "Install security requirements? [Y]: "
read str
echo ""

if [[ $str == "n" && $str == "N" ]]; then
	echo "Packages will not be installed."
else
	echo "Installing security packages:"
	for p in ${sec_pkgs}; do
		echo "Package: $p"
		sudo apt install -y $p
	done
fi

#Make ips.txt file in ~
touch ~/ips.txt

#Remove unused dependencies etc.
sudo apt autoremove && sudo apt autoclean

#!/bin/bash

read -p "Jhetalal ne mud ke kise dekha: " bandi
read -p "Jhetalal ka pyaar %" pyaar

if [[ $bandi == "daya bhabhi"  ]];
then
	echo "Jhethalal is loyal"
elif [[ $pyaar -ge 100 ]];
then
	echo "Jhethalal is loyal"
else
	echo "Jhetalal is not loyal"
fi
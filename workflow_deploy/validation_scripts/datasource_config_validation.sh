#!/bin/bash 

#INS_DIR="${BASH_SOURCE%/*}"
#if [[ ! -d "$INS_DIR" ]]; then INS_DIR="$PWD"; fi
if [[ $1 == "install" ]]; then
usecase_name=$(awk ''/^usecase_name:' /{ if ($2 !~ /#.*/) {print $2}}' config.yml)
fi
if [[ $1 == "upgrade" ]]; then
usecase_name=$(awk ''/^usecase_name:' /{ if ($2 !~ /#.*/) {print $2}}' upgradation_config.yml)
fi

if [[ $usecase_name == "" ]]; then
   echo "Error - in usecase_name. Unable to get the value. Please check."; fail=1
else

case $usecase_name in
   
   education_usecase)
       . $INS_DIR/validation_scripts/${usecase_name}_datasource_config_validation.sh
       ;;
   test_usecase)
       . $INS_DIR/validation_scripts/${usecase_name}_datasource_config_validation.sh
       ;;
   *)
       echo "Error - Please enter the correct value in usecase_name."; fail=1
       ;;
esac

fi

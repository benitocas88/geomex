#!/usr/bin/env bash

set -e -o errexit

cyan='\033[0;36m'
cmd="pip-compile -q"

if [ -n "$*" ];then for arg in "$@";do args="${args} ${arg}";done;fi;
if [ -n "$args" ];then cmd="${cmd} ${args}";fi;

cd /opt/requirements

reqs="base"
for req in ${reqs};do
  bashy="${cmd} ${req}.in --output-file=${req}.txt"
  echo "${cyan}Running command: ${bashy}"
  bash -c "${bashy}"
done

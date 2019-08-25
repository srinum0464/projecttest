#!/bin/bash

file="/home/ansible/hosts"

if [ -f $file ] ; then
    rm $file
fi
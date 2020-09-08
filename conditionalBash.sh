#!/bin/bash

if egrep "127.0.0.1" "/c/My tutorials/python coursera/practice/testPy";then
    echo "Everything Ok, the IP was found"
else
    echo "Error! the IP was not found"
fi

#!/bin/csh


set lastfile = `ls -rt | tail -1`
echo "Most recent file is $lastfile"

set ispyfile = `echo $lastfile | grep py | wc -l`

if ( $ispyfile > 0 ) then
    echo Running on $lastfile
    python3 $lastfile
else
    echo "Most recent file is not a python script."
    set pyfile = `ls -rt *.py | tail -1`
    echo "Most recent python script is $pyfile"
    echo "Do you want to run $pyfile?"
    set input = $<
    set input = `echo $input | cut -c1`
    echo "input is $input"
    if ( $input == "y" | $input == "Y") then
       python3 $pyfile
    endif
   
endif


#!/usr/bin/awk -f

BEGIN {
   a = "GNU/Linux Darwin/maxOS Microsoft/Windows"
   split(a, array, " ")
   print array[2]
}

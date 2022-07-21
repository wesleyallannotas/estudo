#!/usr/bin/awk -f

BEGIN {
  num = 0
  while(num < 10) {
    print num
    num = num + 1
  }
  
  for(i = 0; i < 10; i++) {
    print i
  }
}

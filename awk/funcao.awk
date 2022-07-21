#!/usr/bin/awk -f

function soma(x,y){
  return x + y
}

BEGIN {
  if(ARGV[2] == "") {
    print "Informe 2 numeros"
  }else {
    print "A soma de " ARGV[1] " e " ARGV[2] " e igual a " soma(ARGV[1] + ARGV[2])
  }
}

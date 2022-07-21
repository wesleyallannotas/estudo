#!/usr/bin/awk -f

BEGIN {
	if(ARGV[1] == "") {
    print "Informe o Numero."
	}else{
		print "A raiz quadrada de " ARGV[1] " e: " sqrt(ARGV[1])
  }
}

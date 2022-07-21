#!/usr/bin/awk -f

BEGIN {
  FNR == 2
}
{
  print "Qtd: "$1" - Valor: "$2" - Especificacao: "$3" = Total: "$1+$2+$3
}

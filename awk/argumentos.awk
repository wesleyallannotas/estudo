#!/usr/bin/awk -f

BEGIN {
    conceito = "O Awk e muito " ARGV[1] " e também e muito " ARGV[2]
    print conceito
}
# Formatar
- toLowerCase() - Formata tudo para minusculo
- toUpperCase() - Formata tudo para maiúsculo
- trim() - Remover espaços desnecessários (Por exemplo no final da string)

# Recortar
- substring(inicio) - Informando o inicio do corte
- substring(inicio, fim) - Informando o inicio e o fim do corte

# Substituir
- Replace(char, char) - Carácter por carácter
- Replace(String, String) - Texto por Texto

# Buscar
- indexOf(inicio) - Exibi a primeira aparição do **inicio ao fim**
- lastIndexOf(inicio) - Exibi a primeira aparição do **fim ao inicio**

# Dividir
- str.Split(" ") - Recorta a String com base em um separador especifico
    - Gera um vetor com as partes do string, recortadas conforme o separador.

```java
String original = "abcde FGHIJ ABC abc DEFG ";
String s01 = original.toLowerCase();
String s02 = original.toUpperCase();
String s03 = original.trim();
String s04 = original.substring(2);
String s05 = original.substring(2, 9);
String s06 = original.replace('a', 'x');
String s07 = original.replace("abc", "xy");
int i = original.indexOf("bc");
int j = original.lastIndexOf("bc");

System.out.println("Original: -" + original + "-");
System.out.println("toLowerCase: -" + s01 + "-");
System.out.println("toUpperCase: -" + s02 + "-");
System.out.println("trim: -" + s03 + "-");
System.out.println("substring(2): -" + s04 + "-");
System.out.println("substring(2, 9): -" + s05 + "-");
System.out.println("replace('a', 'x'): -" + s06 + "-");
System.out.println("replace('abc', 'xy'): -" + s07 + "-");
System.out.println("Index of 'bc': " + i);
System.out.println("Last index of 'bc': " + j);
```

```java
String s = "potato apple lemon";

String[] vect = s.split(" ");
String word1 = vect[0];
String word2 = vect[1];
String word3 = vect[2];
```
# Date

- Representa um **INSTANTE**
- Pacote: `java.util`
- Doc: <https://docs.oracle.com/javase/10/docs/api/java/util/Date.html>
- Um objeto *Date* internamente armazena:
    - O numero de milissegundos desde a meia noite do dia 1 de janeiro de 1970 GMT (UTC)
        - GMT: *Greenwich Mean Time (time zone)
        - UTC: Coordinated Universal Time (time standard)

## SimpleDateFormat

- Doc: <https://docs.oracle.com/javase/10/docs/api/java/text/SimpleDateFormat.html>
- Define formatos para conversão entre ***Date*** e ***String***
    - Quando informamos uma data para um sistemas ou quando o sistema vai ler uma data de um banco de dados ou arquivo, sera lido um texto, e este texto tem que ser convertido para o ***Date***, para fazer essa conversão existe varias formas, uma delas e o ***SimpleDateFormat***

- dd/MM/yyyy -> 23/07/2018
- dd/MM/yyyy HH:mm:ss -> 23/07/2018 15:42:07

# Padrão ISO 8601 e classe Instant

- Formato: yyyy-MM-ddTHH:mm:ssZ
- Exemplo: "2018-06-25T15:42:07Z"

O java da Versao 8 em diante possui uma nova biblioteca para mexer com data, ela possui vários recursos sendo um deles a classe `Instant`, ela possui um método que chama `parse` onde se colocarmos entre parentes dentro de aspas uma data dentro do Padrão ISO 8601, ele converte automaticamente para o tipo ***Date*** se informamos `Date.from`
- Date y3 = Date.from(Instant.parse("2018-06-25T15:42:07z));

## Exemplo

```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class App {
    public static void main(String[] args) throws ParseException {

        SimpleDateFormat sdf1 = new SimpleDateFormat("dd/MM/yyyy");
        SimpleDateFormat sdf2 = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        
        Date x1 = new Date(); // Gera uma data no instante que roda
        Date x2 = new Date(System.currentTimeMillis()); // Pega o instante do sistema, converte para milissegundos.
        
        Date y1 = sdf1.parse("25/06/2018");
        Date y2 = sdf2.parse("25/06/2018 15:42:07");
        
        System.out.println(y1); // Saida: Mon Jun 00:00:00 BRT 2018 
        System.out.println(y2); // Saida: Mon Jun 15:42:07 BRT 2018

        System.out.println(sdf2.format(y1)); // Saida: 25/06/2018 00:00:00
        System.out.println(sdf2.format(y2)); // Saida: 25/06/2018 15:42:07
    }
}
```

## Instanciando uma data no formato ISO 8601

```java
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;

public class App {
    public static void main(String[] args) {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");

        Date y = Date.from(Instant.parse("2018-06-25T15:42:07Z"));
        
        System.out.println(sdf.format(y)); // Saida: 25/06/2018 12:42:07
    }
}
```
> Podemos perceber que informamos 15:42:07 e o programa imprimiu 12:42:07, isso acontece por que informamos no padrão UTC e o sistema ja converteu para o horário da região do nosso sistema, no caso Brasil. ou seja, UTC -3.

### Imprimindo data no horário UTC (padrão mundial)
```java
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;
import java.util.TimeZone;

public class App {
    public static void main(String[] args) {

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        sdf.setTimeZone(TimeZone.getTimeZone("GMT")); // Horário GMT, ou seja, UTC padrão

        Date y = Date.from(Instant.parse("2018-06-25T15:42:07Z"));
        
        System.out.println(sdf.format(y)); // Saida: 25/06/2018 12:42:07
    }
}
```

# Manipulando uma data com Calendar

Umas das varias formas de manipular data, sendo uma das mais clássicas e antiga, ou seja, muita coisa desenvolvida no mercado usa ***Calendar***

## Somando uma unidade de tempo

Exemplo temos uma data e queremos adicionar uma quantidade de Dias a data, ou uma determina quantidade de Horas, ou seja, acrescentar a data.
```java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;

public class Program {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyy HH:mm:ss");

        Date d = Date.from(Instant.parse("2018-06-25T15:42:07Z"));

        System.out.println(sdf.format(d));

        Calendar cal = Calendar.getInstance();
        cal.setTime(d);
        cal.add(Calendar.HOUR_OF_DAY, 4); // Adicionamos 4 Horas a data atual.
        d = cal.getTime();

        System.out.println(sdf.format(d));
    }
}
```

## Obtendo uma unidade de tempo

```java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Calendar;
import java.util.Date;

public class Program {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyy HH:mm:ss");

        Date d = Date.from(Instant.parse("2018-06-25T15:42:07Z"));

        System.out.println(sdf.format(d));

        Calendar cal = Calendar.getInstance();
        cal.setTime(d);
        int minutes = cal.get(Calendar.MINUTE);
        int month = 1 + cal.get(Calendar.MONTH);

        System.out.println("Minutes: " + minutes);
        System.out.println("Month: " + month);
    }
}
```
> Exibira o valor por padrão 5 pois para o calendar começa no valor 0, ou seja, janeiro e o mes 0, por isso adicionamos mais 1 ao valor para dar no mes certo `int month = 1 + cal.get(Calendar.MONTH)`
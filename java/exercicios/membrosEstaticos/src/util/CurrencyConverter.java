package util;

public class CurrencyConverter {
    public static final double IOF = 0.06;

    public static double calc(double cotacao, double dollars) {
        return dollars * cotacao * (1.0 + IOF); 
    }
}
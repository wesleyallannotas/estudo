package entities;

public class Aluno {
    public String name;
    public double nota1;
    public double nota2;
    public double nota3;

    public double notaFinal() {
        return this.nota1 + this.nota2 + this.nota3;
    }
    public String notaCorte() {
        return (notaFinal() >= 90.00) ? "PASS" : "MISSING " + (60.00 - notaFinal());
    }
}
package entities;

public class Account {
   private int idAccount;
   private String name;
   private double balance;
   
   public Account(int idAccount, String name){
       this.idAccount = idAccount;
       this.name = name;
   }
   
   public Account(int idAccount, String name, double initialDeposit) {
       this.idAccount = idAccount;
       this.name = name;
       deposit(initialDeposit);
   }
   
   public int getIdAccount() {
       return idAccount;
   }
   public String getName() {
       return name;
   }
   public void setName(String name) {
       this.name = name;
   }
   public double getBalance() {
       return balance;
   }
   public void deposit(double depositValue) {
       balance += depositValue;
   }
   public void withdraw(double withdrawValue) {
       balance -= withdrawValue + 5.00;
   }
   public String toString() {
    return "Account "
            + idAccount 
            + ", Holder: "
            + name 
            + ", Balance: $ "
            + String.format("%.2f", balance);
}
}
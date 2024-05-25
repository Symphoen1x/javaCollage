
class Employee {
    String nama;
    int salary;

    public Employee() {
    }

    public Employee(String nm) {
        this.nama = nm;
        System.out.println("Employee");

    }

    public int salary() {
        return 0;
    }

}

class Manager extends Employee {
    private static final int gaji = 40000;
    private static final int tunjangan = 40000;

    public int salary() {
        return gaji;
    }

    public int tunjangan() {
        return tunjangan;
    }
}

class Programmer extends Employee {
    private static final int gaji2 = 50000;
    private static final int bonuspr = 70000;

    public int salary() {
        return gaji2;
    }

    public int bonus() {
        return bonuspr;
    }
}

public class Payroll {
    public int calcpayrol(Employee emp) {
        int money = emp.salary();
        if (emp instanceof Manager)
            money += ((Manager) emp).tunjangan();
        if (emp instanceof Programmer)
            money += ((Programmer) emp).bonus();
        return money;
    }

    public static void main(String[] args) {
        Payroll pr = new Payroll();
        Programmer prg = new Programmer();
        Manager mg = new Manager();
        System.out.println("Payroll untuk programmer: " + pr.calcpayrol(prg));
        System.out.println("Payroll untuk manager: " + pr.calcpayrol(mg));

    }
}

// class Un {
// public String nama;
// public String gaji;

// void info() {

// System.out.println("Nama" + nama);
// System.out.println("Gaji" + gaji);

// }
// }

// public class Payroll extends Un {
// public String departemen;

// void info() {

// System.out.println("Nama" + nama);
// System.out.println("Gaji" + gaji);
// System.out.println("Departemen" + departemen);

// }

// }

// Virtual Method Inovaction
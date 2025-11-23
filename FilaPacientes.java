import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class FilaPacientes {

    // Classe simples para representar um paciente
    static class Paciente {
        String nome;
        String cpf;

        Paciente(String nome, String cpf) {
            this.nome = nome;
            this.cpf = cpf;
        }

        @Override
        public String toString() {
            return nome + " - CPF: " + cpf;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Paciente> fila = new LinkedList<>();

        System.out.println("=== Inserir 3 pacientes na fila ===");
        for (int i = 1; i <= 3; i++) {
            System.out.printf("Paciente %d - Nome: ", i);
            String nome = sc.nextLine().trim();
            System.out.printf("Paciente %d - CPF: ", i);
            String cpf = sc.nextLine().trim();

            fila.add(new Paciente(nome, cpf));
        }

        System.out.println("\n=== Atendendo o primeiro paciente ===");
        Paciente atendido = fila.poll(); // usa poll() para não lançar exceção se fila vazia
        if (atendido != null) {
            System.out.println("Paciente atendido: " + atendido);
        } else {
            System.out.println("Fila vazia. Nenhum paciente para atender.");
        }

        System.out.println("\n=== Pacientes restantes na fila ===");
        if (fila.isEmpty()) {
            System.out.println("Nenhum paciente na fila.");
        } else {
            for (Paciente p : fila) {
                System.out.println(p);
            }
        }

        sc.close();
    }
}

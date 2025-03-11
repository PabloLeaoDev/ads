package exc_aula_pratica2.exc1;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite a primeira nota: ");
		double nota1 = sc.nextDouble();
		System.out.println("Digite a segunda nota: ");
		double nota2 = sc.nextDouble();
		System.out.println("Digite a terceira nota: ");
		double nota3 = sc.nextDouble();
		
		Avaliacao aluno = new Avaliacao(nota1, nota2, nota3);
		
		System.out.println("A média aritmética é de " + aluno.mediaAritmetica());
		System.out.println("A média ponderada é de " + aluno.mediaPonderada());
	}

}

package cofrinho_trabalho;

import java.util.Scanner;

public class Principal {
	private static Scanner sc = new Scanner(System.in);
	private static Cofrinho c = new Cofrinho();
	private static Moeda m;

	public static void main(String[] args) {
		while (true) {
			try {
				System.out.println("-----------------------------------------\n" + "COFRINHO:\n"
						+ "1 - Adicionar Moeda\n" + "2 - Remover Moeda\n" + "3 - Listar Moedas\n"
						+ "4 - Calcular total convertido para Real\n" + "0 - Encerrar");
				int choice = sc.nextInt();
				double value;
				switch (choice) {
				case 0:
					System.out.println("Progama encerrado");
					return;
				case 1:
					value = escolherMoeda();
					c.adicionar(m, value);
					break;
				case 2:
					value = escolherMoeda();
					c.remover(m, value);
					break;
				case 3:
					c.listagemMoedas();
					break;
				case 4:
					System.out.println("Valor Total no Cofrinho (em Real): " + c.totalConvertido());
					break;
				default:
					if (choice < 0 || choice > 4)
						throw new IllegalArgumentException("Valor inválido: " + choice);
					else
						throw new Exception();
				}
			} catch (IllegalArgumentException e) {
				System.out.println("\nOcorreu um erro(" + e + ");");
			} catch (Exception e) {
				System.out.println("\nOcorreu um erro(" + e + ");");
				System.out.println("Progama encerrado");
				return;
			}
		}

	}

	// método criado para fazer o usúario escolher uma moeda específica e seu
	// respectivo valor.
	public static double escolherMoeda() {
		System.out.println("Escolha a Moeda:\n" + "1 - Real\n" + "2 - Dolar\n" + "3 - Euro");
		while (true) {
			int choice = sc.nextInt();
			if (choice == 1) {
				m = new Real();
			} else if (choice == 2) {
				m = new Dolar();
			} else if (choice == 3) {
				m = new Euro();
			} else {
				System.out.println("\nDigite uma opção válida.");
				continue;
			}
			break;
		}
		System.out.println("Digite um valor:");
		double valor = sc.nextDouble();
		return valor;
	}

}

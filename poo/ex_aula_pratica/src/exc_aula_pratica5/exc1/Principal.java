package exc_aula_pratica5.exc1;

import java.util.ArrayList;

public class Principal {

	public static void main(String[] args) {
		Desktop pcA = new Desktop(480, 1, 600);
		Notebook pcB = new Notebook(240, 1, 15);
		
		Computador comp;
		
		comp = pcA;
		System.out.println("Valor Desktop: R$" + comp.calculaValor());
		
		comp = pcB;
		System.out.println("Valor Notebook: R$ " + comp.calculaValor());
		
		ArrayList<Computador> listaComputadores = new ArrayList();
		
		listaComputadores.add(pcA);
		listaComputadores.add(pcB);
		
		double valorTotal = 0;
		for (Computador computer: listaComputadores) {
			valorTotal += computer.calculaValor();
		}

		System.out.println("Valor Total: R$ " + valorTotal);
	}

}

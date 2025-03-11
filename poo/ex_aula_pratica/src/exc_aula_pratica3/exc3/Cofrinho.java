package exc_aula_pratica3.exc3;

import java.util.ArrayList;

public class Cofrinho {
	private ArrayList<Moeda> moedas = new ArrayList();
	
	Cofrinho() {}
	
	public void add(Moeda moeda) {
		moedas.add(moeda);
	}
	
	public double calcularTotal() {
		double total = 0;
		for (Moeda moeda : moedas) {
			total += moeda.getValor();
		}
		return total;
	}
}

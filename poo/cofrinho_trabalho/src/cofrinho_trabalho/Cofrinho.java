package cofrinho_trabalho;

import java.util.ArrayList;

public class Cofrinho {
	private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();
	
	// método criado para adicionar moedas ao cofrinho
	public void adicionar(Moeda m, double valor) {
		for (Moeda moeda : listaMoedas) {
			// se o tipo de moeda acrescida já existir no cofrinho, o valor da moeda apenas aumentará
			if (moeda.getClass() == m.getClass()) {
				moeda.manipulateValor(valor);
				return;
			}
		}
		m.setValor(valor);
		listaMoedas.add(m);
	}
	
	// método criado para remover moedas, ou subtrair algum valor delas, do cofrinho
	public void remover(Moeda m, double valor) {
		for (Moeda moeda : listaMoedas) {
			if (moeda.getClass() == m.getClass()) {
				if (valor <= moeda.getValor() && valor > 0) {
					// se o valor passado for igual ao valor total da moeda em questão, essa moeda é removida por inteiro do cofrinho
					if (valor == moeda.getValor()) {
						listaMoedas.remove(moeda);				
						return;
					}
					// negativando o valor para subtrair com o método manipulateValor() 
					valor *= (-1);
					moeda.manipulateValor(valor);
				} else if (valor <= 0) {
					System.out.println("São aceitos somente valores > 0.");
				} else if (valor > moeda.getValor()) {
					System.out.println("São aceitos somente valores <= " + moeda.getValor());					
				}
				return;
			}
		}
		System.out.println("Não é possível remover uma moeda que não está no cofrinho.");
	}
	
	// método criado para listar todas as moedas contidas no cofrinho e seus respectivos valores
	public void listagemMoedas() {
		if (listaMoedas.size() == 0) {
			System.out.println("Não há moedas no cofrinho.");
		} else {
			for (Moeda m : listaMoedas) {
				m.info();
			}			
		}
	}
	
	// método criado para retornar o valor total acumulado no cofrinho, em reais
	public double totalConvertido() {
		double valorTotal = 0; 
		
		for (Moeda m : listaMoedas) {
			if (m instanceof Dolar || m instanceof Euro) {
				valorTotal += m.converter(m.getValor());
			} else if (m instanceof Real) {
				valorTotal += m.getValor();
			}
		}
		
		return valorTotal;
	}
}

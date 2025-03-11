package exc_aula_pratica3.exc3;

public class Principal {

	public static void main(String[] args) {
		Cofrinho cofre = new Cofrinho();
		
		cofre.add(new Moeda("Dolar", 1));
		cofre.add(new Moeda("Dolar", 2));
		cofre.add(new Moeda("Dolar", 3));
		System.out.println("Total: $ " + cofre.calcularTotal());
	}

}

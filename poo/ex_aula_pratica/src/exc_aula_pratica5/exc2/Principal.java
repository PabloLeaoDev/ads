package exc_aula_pratica5.exc2;

public class Principal {
	public static void main(String[] args) {
		Funcionario f = new Funcionario("Fulano", 20, "Desenvolvedor Júnior");
		Carro c = new Carro("Skyline", "Nissan", 2000);
		
		f.imprimir();
		c.imprimir();
	}
}

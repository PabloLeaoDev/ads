package exc_aula_pratica6.exc1;

public class Principal {

	public static void main(String[] args) {
		Conta c = new Conta("Fulano", 3000);
		
		try {
			c.info();
			c.sacar(5000);
//			c.depositar(-1);
//			c.depositar(3000);
//			c.sacar(3000);
			c.sacar(1000);
			c.info();
		} catch (Exception e) {
			System.out.println("Erro detectado(" + e.getMessage() + ")");
			return;
		} finally {
			System.out.println("Programa encerrado.");
		}
	
	}

}

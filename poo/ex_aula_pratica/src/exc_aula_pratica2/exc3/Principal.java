package exc_aula_pratica2.exc3;

public class Principal {

	public static void main(String[] args) {
		Conta c1 = new Conta(1, "Fulano", 9600, 3000);
		Conta c2 = new Conta(2, "Sicrano", 1400, 500);
		
		c1.info();
		c1.sacar(1500);
		c1.info();
		c1.depositar(0);
		c1.depositar(2500);
		c1.limite = 6000;
		c1.info();
		c2.info();
		c1.transferir(1600, c2);
		c2.info();
	}

}

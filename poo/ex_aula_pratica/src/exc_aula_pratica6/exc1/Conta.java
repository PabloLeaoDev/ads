package exc_aula_pratica6.exc1;

public class Conta {
	private String nome;
	private double saldo;
	
	Conta() {}
	
	Conta(String nome, double saldo) {
		this.nome = nome;
		this.saldo = saldo;
	}
	
	public void depositar(double valor) throws Exception {
		if (valor < 0) {
			throw new Exception("Valores negativos não são válidos");
		} else if (valor > 2000) {
			throw new Exception("Não é possível depositar valores acima de R$ 2000");
		} else {
			System.out.println("Depósito realizado.");
			saldo += valor;				
		}
	}
	
	public void sacar(double valor) throws Exception {
		if (valor < 0) {
			throw new Exception("Valores negativos não são válidos");
		} else if (valor > saldo) {
			throw new Exception("Saldo insuficiente");
		} else if (valor > 2000) {
			throw new Exception("Não é possível sacar valores acima de R$ 2000"); 
		} else {
			System.out.println("Saque realizado.");
			saldo -= valor;				
		}
	}

	public void transferir(double valor) throws Exception {
		if (valor < 0) {
			throw new Exception("Valores negativos não são válidos");
		} else if (valor > saldo) {
			throw new Exception("Saldo insuficiente");
		} else {
			System.out.println("Transferência realizada.");
			saldo -= valor;				
		}
	}
	
	public void info() {
		System.out.println("------------------");
		System.out.println("Nome: " + nome);
		System.out.println("Saldo: R$ " + saldo);
	}
}

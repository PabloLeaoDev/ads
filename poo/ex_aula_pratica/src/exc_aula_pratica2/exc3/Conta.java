package exc_aula_pratica2.exc3;

public class Conta {
	int numero;
	String titular;
	double saldo;
	double limite;

	Conta(int numero, String titular, double saldo, double limite) {
		this.numero = numero;
		this.titular = titular;
		this.saldo = saldo;
		this.limite = limite;
	}
	
	boolean sacar(double valor) {
		if (this.saldo < valor) {
			System.out.println("\nERRO: Saldo insuficiente para saque.");
		} else if (this.limite < valor) {
			System.out.println("\nERRO: O saque não pode exceder o limite da conta.");
		} else if (valor <= 0) {
			System.out.println("\nERRO: Saques iguais ou menores que zero não são válidos.");
		} else {
			this.saldo -= valor;
			System.out.println("\nSaque realizado com sucesso!");
			return true;			
		}
		return false;
	}
	
	boolean depositar(double valor) {
		if (valor <= 0) {
			System.out.println("\nERRO: Depósitos iguais ou menores que zero não são válidos.");
			return false;
		}
		this.saldo += valor;
		System.out.println("\nDepósito realizado com sucesso!");
		return true;
	}
	
	boolean transferir(double valor, Conta destino) {
		if (this.saldo < valor) {
			System.out.println("\nERRO: Saldo insuficiente para transferência.");
		} else if (this.limite < valor) {
			System.out.println("\nERRO: A transferência não pode exceder o limite da conta.");
		} else if (valor <= 0) {
			System.out.println("\nERRO: Transferências iguais ou menores que zero não são válidas.");
			return false;
		}
		this.saldo -= valor;
		destino.saldo += valor;
		System.out.println("\nTransferência realizada com sucesso!");
		return true;
	}
	
	void info() {
		System.out.println("\nInformações da Conta:");
		System.out.println("-----------------------");
		System.out.println("Número: " + this.numero);
		System.out.println("Titular: " + this.titular);
		System.out.println("Saldo: R$ " + this.saldo);
		System.out.println("Limite: R$ " + this.limite);
		System.out.println("-----------------------");
	}

}

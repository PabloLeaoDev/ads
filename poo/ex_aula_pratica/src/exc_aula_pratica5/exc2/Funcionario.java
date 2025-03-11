package exc_aula_pratica5.exc2;

public class Funcionario implements Imprimivel {
	String nome;
	int idade;
	String cargo;
	
	Funcionario() {}
	
	Funcionario(String nome, int idade, String cargo) {
		this.nome = nome;
		this.idade = idade;
		this.cargo = cargo;
	}
	
	@Override
	public void imprimir() {
		System.out.println("Nome: " + nome + " - Idade: " + idade + " - Cargo: " + cargo);
	}
}

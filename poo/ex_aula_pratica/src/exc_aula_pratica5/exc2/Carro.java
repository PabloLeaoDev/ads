package exc_aula_pratica5.exc2;

public class Carro implements Imprimivel {
	String nome;
	String marca;
	int ano;
	
	public Carro() {}
	
	public Carro(String nome, String marca, int ano) {
		this.nome = nome;
		this.marca = marca;
		this.ano = ano;
	}
	
	@Override
	public void imprimir() {
		System.out.println("Nome: " + nome + " - Marca: " + marca + " - Ano: " + ano);
	}
}

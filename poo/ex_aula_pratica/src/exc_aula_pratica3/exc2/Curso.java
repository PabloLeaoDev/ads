package exc_aula_pratica3.exc2;

public class Curso {
	String nome;
	double mensalidade;
	
	Curso() {}
	
	Curso(String nome, double mensalidade) {
		setNome(nome);
		setMensalidade(mensalidade);
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getMensalidade() {
		return mensalidade;
	}

	public void setMensalidade(double mensalidade) {
		if (mensalidade < 0) {
			System.out.println("Mensalidade inválida!");
			return;
		}
		this.mensalidade = mensalidade;
	}

	public void descrever() {
		System.out.println("Nome do Curso: " + nome);
		System.out.println("Mensalidade: R$ " + mensalidade);
	}
}

package exc_aula_pratica3.exc2;

public class Aluno {
	private String nome;
	private int matricula;
	private double desconto;
	private Curso curso;
	
	Aluno(String nome, int matricula, double desconto, String curso, double mensalidade) {
		setNome(nome);
		setMatricula(matricula);
		setDesconto(desconto);
		setCurso(curso, mensalidade);
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public int getMatricula() {
		return matricula;
	}
	
	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}
	
	public double getDesconto() {
		return desconto;
	}
	
	public void setDesconto(double desconto) {
		this.desconto = desconto;
	}
	
	public Curso getCurso() {
		return curso;
	}
	
	public void setCurso(String curso, double mensalidade) {
		this.curso = new Curso(curso, mensalidade);
	}
	
	public void descrever() {
		System.out.println("Nome do Aluno: " + nome);
		System.out.println("Matrícula: " + matricula);
		System.out.println("Desconto: " + desconto + "%");
		curso.descrever();
	}
	
	public double pagamento() {
		final double desconto = (curso.mensalidade * this.desconto) / 100;
		final double pagar = curso.mensalidade - desconto;
		return pagar;
	}
	
}

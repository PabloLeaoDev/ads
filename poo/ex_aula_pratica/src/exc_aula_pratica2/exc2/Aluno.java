package exc_aula_pratica2.exc2;

public class Aluno {
	String nome;
	String curso;
	Avaliacao desempenho;
	
	Aluno() {}
	
	Aluno(String nome, String curso, double n1, double n2, double n3) {
		this.nome = nome;
		this.curso = curso;
		this.desempenho = new Avaliacao(n1, n2, n3);
		
		System.out.println("Aluno: " + this.nome);
		System.out.println("Curso: " + this.curso);
		System.out.println("Média Aritmética: " + desempenho.mediaAritmetica());
		System.out.println("Média Ponderada: " + desempenho.mediaPonderada());
	}
}

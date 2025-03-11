package exc_aula_pratica3.exc1;

public class Principal {

	public static void main(String[] args) {
		Nota aluno = new Nota();
		
		aluno.setNota1(7);
		aluno.setNota2(9);
		aluno.setFaltas(10);
		System.out.println("1° Nota: " + aluno.getNota1());
		System.out.println("2° Nota: " + aluno.getNota2());
		System.out.println("Faltas: " + aluno.getFaltas());
		aluno.result();
	}

}

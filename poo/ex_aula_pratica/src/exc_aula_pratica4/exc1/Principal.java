package exc_aula_pratica4.exc1;

public class Principal {

	public static void main(String[] args) {
		Livro livro = new Livro("O Príncipe",
				new Autor("Nicolau Maquiável", "", "Italiano"),
				"Filosofia",
				1);
		livro.info();
	}

}

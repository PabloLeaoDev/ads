package exc_aula_pratica3.exc2;

public class Principal {

	public static void main(String[] args) {
		Aluno aluno = new Aluno("Pablo", 1, 90, "ADS", 760);
		aluno.descrever();
		System.out.println("Valor a pagar: R$ " + aluno.pagamento());
	}

}

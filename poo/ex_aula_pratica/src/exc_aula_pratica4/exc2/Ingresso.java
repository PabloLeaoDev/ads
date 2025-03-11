package exc_aula_pratica4.exc2;

public class Ingresso {
	private String nomeEvento;
	protected double valor;
	
	public Ingresso() {}
	
	public Ingresso(String nomeEvento, double valor) {
		this.nomeEvento = nomeEvento;
		this.valor = valor;
	}
	
	public String getNomeEvento() {
		return nomeEvento;
	}

	public void setNomeEvento(String nomeEvento) {
		this.nomeEvento = nomeEvento;
	}

	public double getValor() {
		return valor;
	}

	public void setValor(double valor) {
		this.valor = valor;
	}

	public void info() {
		System.out.println("Evento: " + nomeEvento);
		System.out.println("Valor do Ingresso: R$ " + valor);
	}
	
}

package exc_aula_pratica4.exc2;

public class IngressoVip extends Ingresso {
	private double adicional;
	
	public IngressoVip() {}
	
	public IngressoVip(String nomeEvento, double valor, double adicional) {
		super(nomeEvento, valor);
		this.adicional = adicional;
	}
	
	@Override
	public void info() {
		super.info();
		System.out.println("Valor Adicional: R$ " + adicional);
		System.out.println("Valor Total: R$ " + (valor + adicional));
	}
}

package exc_aula_pratica5.exc1;

public class Desktop extends Computador {
	private double acessorios;
	
	public Desktop(int gbMemoria, int numProcessadores, double acessorios) {
		super(gbMemoria, numProcessadores);
		this.acessorios = acessorios;
	}
	
	@Override
	public double calculaValor() {
		return (double) (this.gbMemoria * 200) + (double) (this.numProcessadores * 400) + this.acessorios;
	}
}

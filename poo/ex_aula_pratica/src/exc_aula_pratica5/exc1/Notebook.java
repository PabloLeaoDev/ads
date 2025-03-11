package exc_aula_pratica5.exc1;

public class Notebook extends Computador {
	private int polegadasTela;
	
	public Notebook(int gbMemoria, int numProcessadores, int polegadasTela) {
		super(gbMemoria, numProcessadores);
		this.polegadasTela = polegadasTela;
	}
	
	@Override
	public double calculaValor() {
		return (double) (gbMemoria * 250) + (double) (numProcessadores * 500) + polegadasTela * 100;
	}
}

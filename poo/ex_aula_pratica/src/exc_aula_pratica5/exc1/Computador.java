package exc_aula_pratica5.exc1;

public abstract class Computador {
	int gbMemoria;
	int numProcessadores;
	
	Computador(int gbMemoria, int numProcessadores) {
		this.gbMemoria = gbMemoria;
		this.numProcessadores = numProcessadores;
	}
	
	abstract double calculaValor();
}

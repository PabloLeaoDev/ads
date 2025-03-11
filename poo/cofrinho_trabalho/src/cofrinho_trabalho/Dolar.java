package cofrinho_trabalho;

public class Dolar extends Moeda {
	Dolar() {}
	
	Dolar(double valor) {
		super(valor);
	}
	
	@Override
	public void info() {
		System.out.println("Dolar: " + this.getValor());
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		return true;
	}

	@Override
	public double converter(double valor) {
		return valor * 5.53;
	}
}

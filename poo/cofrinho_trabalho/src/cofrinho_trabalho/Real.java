package cofrinho_trabalho;

public class Real extends Moeda {
	Real() {}
	
	Real(double valor) {
		super(valor);
	}
	
	@Override
	public void info() {
		System.out.println("Real: " + this.getValor());
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
}

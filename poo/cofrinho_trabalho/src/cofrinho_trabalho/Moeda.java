package cofrinho_trabalho;

import java.util.Objects;

public abstract class Moeda {
	private double valor;
	
	Moeda() {}
	
	Moeda(double valor) {
		this.valor = valor;
	}
	
	public abstract void info();
	
	public double converter(double valor) {
		return valor;
	}
	
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Moeda other = (Moeda) obj;
		return Double.doubleToLongBits(valor) == Double.doubleToLongBits(other.valor);
	}
	
	public void manipulateValor(double valor) {
		this.valor += valor;
	}

	public double getValor() {
		return valor;
	}

	public void setValor(double valor) {
		this.valor = valor;
	}
}

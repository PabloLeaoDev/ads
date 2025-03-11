package exc_aula_pratica3.exc1;

public class Nota {
	private double nota1;
	private double nota2;
	private int faltas; 
	
	Nota() {}
	
	Nota(double nota1, double nota2, int faltas) {
		setNota1(nota1);
		setNota2(nota2);
		setFaltas(faltas);
	}
	
	public void setNota1(double nota) {
		if (nota >= 0 && nota <= 10) {
			this.nota1 = nota;	
			return;
		}
		System.out.println("O valor da nota não é válido!");
	}
	
	public void setNota2(double nota) {
		if (nota >= 0 && nota <= 10) {
			this.nota2 = nota;			
		} else {
			System.out.println("O valor da nota não é válido!");
		}
	}
	
	public void setFaltas(int faltas) {
		if (faltas < 0 || faltas > 30) {
			System.out.println("Valor de faltas inválido!");
			return;
		}
		this.faltas = faltas;
	}
	
	public double getNota1() {
		return this.nota1;
	}
	
	public double getNota2() {
		return this.nota2;
	}
	
	public double getFaltas() {
		return this.faltas;
	}
	
	public void result() {
		final double media = (this.nota1 + this.nota2) / 2;
		
		System.out.println("Média: " + media);
		
		if (this.faltas > 7) {
			System.out.println("Reprovado por faltas!");
			return;
		}
		
		if (media < 4) {
			System.out.println("Reprovado!");
		} else if (media < 7) {
			System.out.println("Exame Final!");
		} else {
			System.out.println("Aprovado!");
		}
	}
}

package exc_aula_pratica6.exc2;

public class Principal {

	public static int[] instanciaArray(int n) {
		return new int[n];			
	}
	
	public static void main(String[] args) {
		try {
			int[] arr = instanciaArray(-10);	
			for(int num: arr) {
				System.out.println(num);
			}
		} catch (NegativeArraySizeException e) {
			System.out.println("Ocorreu um erro: (" + e + ")");
			System.out.println("Valor inválido: (" + e.getMessage() + ")");
		} catch (Exception e) {
			System.out.println("Ocorreu um erro: (" + e + ")");
		} finally {
			System.out.println("Fim do programa.");
		}

	}

}

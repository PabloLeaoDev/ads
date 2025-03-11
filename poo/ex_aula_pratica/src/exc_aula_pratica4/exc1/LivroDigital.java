package exc_aula_pratica4.exc1;

public class LivroDigital extends Livro {
	private int download;
	private double tamanho;
	
	public LivroDigital() {}
	
	public LivroDigital(String titulo, Autor autor, String genero, int edicao, int download, int tamanho) {
		super(titulo, autor, genero, edicao);
		this.download = download;
		this.tamanho = tamanho;
	}
	
	public int getDownload() {
		return download;
	}
	
	public void setDownload(int download) {
		this.download = download;
	}
	
	public double getTamanho() {
		return tamanho;
	}
	
	public void setTamanho(double tamanho) {
		this.tamanho = tamanho;
	}
	
	@Override
	public void info() {
		super.info();
		System.out.println("Download: " + download);
		System.out.println("Tamanho: " + tamanho);
	}
}

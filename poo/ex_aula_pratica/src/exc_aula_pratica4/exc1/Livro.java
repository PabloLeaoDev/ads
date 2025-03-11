package exc_aula_pratica4.exc1;

public class Livro {
	private String titulo;
	private Autor autor;
	private String genero;
	private int edicao;
	
	public Livro() {}
	
	public Livro(String titulo, Autor autor, String genero, int edicao) {
		this.titulo = titulo;
		this.autor = autor;
		this.genero = genero;
		this.edicao = edicao;
	}
	
	public String getTitulo() {
		return titulo;
	}
	
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	
	public Autor getAutor() {
		return autor;
	}
	
	public void setAutor(Autor autor) {
		this.autor = autor;
	}
	
	public String getGenero() {
		return genero;
	}
	
	public void setGenero(String genero) {
		this.genero = genero;
	}
	
	public int getEdicao() {
		return edicao;
	}
	
	public void setEdicao(int edicao) {
		this.edicao = edicao;
	}
	
	public void info() {
		System.out.println("Título: " + this.titulo);
		System.out.println("Nome Autor: " + this.autor.getNome());
		if (!(this.autor.getEmail().equals(""))) {
			System.out.println("Email do Autor: " + this.autor.getEmail());			
		}
		System.out.println("Nacionalidade do Autor: " + this.autor.getNacionalidade());
		System.out.println("Genêro: " + this.genero);
		System.out.println("Edição: " + this.edicao);
	}
}

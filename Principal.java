import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
// anime
class Anime {
    // Atributo
    public String nombre;
    public String genero;
    private int nroEpisodios;
    private List<String> episodios;

    // Constructorr
    public Anime(String nombre, String genero, int nroEpisodios) {
        this.nombre = nombre;
        this.genero = genero;
        this.nroEpisodios = nroEpisodios;
        this.episodios = new ArrayList<>();
    }

    // Getters y Setters priv
    public int getNroEpisodios() {
        return nroEpisodios;
    }

    public void setNroEpisodios(int nroEpisodios) {
        this.nroEpisodios = nroEpisodios;
    }

    public List<String> getEpisodios() {
        return episodios;
    }

    public void setEpisodios(List<String> episodios) {
        this.episodios = episodios;
    }

    // metodo tostring
    @Override
    public String toString() {
        return "Anime{" +
                "nombre='" + nombre + '\'' +
                ", genero='" + genero + '\'' +
                ", nroEpisodios=" + nroEpisodios +
                ", episodios=" + episodios +
                '}';
    }
}

// Clase televisor
class Televisor {
    // Atributos priv
    private String marca;
    private int resolucion;
    private String tipo; // oled, ips, etc

    // Constructor con parametros
    public Televisor(String marca, int resolucion, String tipo) {
        this.marca = marca;
        this.resolucion = resolucion;
        this.tipo = tipo;
    }

    // Constructor vacío por default
    public Televisor() {
        this.marca = "";
        this.resolucion = 0;
        this.tipo = "";
    }

    // Getters y setters
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getResolucion() {
        return resolucion;
    }

    public void setResolucion(int resolucion) {
        this.resolucion = resolucion;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    // Método tostring
    @Override
    public String toString() {
        return "Televisor{" +
                "marca='" + marca + '\'' +
                ", resolucion=" + resolucion +
                ", tipo='" + tipo + '\'' +
                '}';
    }
}

// Clase instrumento
class Instrumento {
    // atributos
    public String nombre;
    private String material;
    private String tipo; 

    // constructor
    public Instrumento(String nombre, String material, String tipo) {
        this.nombre = nombre;
        this.material = material;
        this.tipo = tipo;
    }
    
    // Getters y setters
    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    // Metodo tostring
    @Override
    public String toString() {
        return "Instrumento{" +
                "nombre='" + nombre + '\'' +
                ", material='" + material + '\'' +
                ", tipo='" + tipo + '\'' +
                '}';
    }
}

// Clase principal
public class Principal {
    public static void main(String[] args) {
        // Crear dos objetos de anime
        Anime anime1 = new Anime("One Piece", "Shonen", 1000);
        anime1.setEpisodios(Arrays.asList("Episodio 1", "Episodio 2", "Episodio 3", "..."));

        Anime anime2 = new Anime("Your Name", "Romance", 1);
        anime2.setEpisodios(Arrays.asList("Película completa"));

        // Crear dos objetos de televisor
        Televisor tv1 = new Televisor("Samsung", 3840, "OLED");
        Televisor tv2 = new Televisor();
        tv2.setMarca("LG");
        tv2.setResolucion(1920);
        tv2.setTipo("IPS");

        // Crear dos objetos de instrunmneto
        Instrumento inst1 = new Instrumento("Guitarra", "Madera", "cuerda");
        Instrumento inst2 = new Instrumento("Flauta", "Metal", "aire");

        // Mostrar los objetos creados
        System.out.println("Objetos anime");
        System.out.println(anime1);
        System.out.println("Episodios de " + anime1.nombre + ": " + anime1.getEpisodios());
        System.out.println(anime2);
        System.out.println("Episodios de " + anime2.nombre + ": " + anime2.getEpisodios());

        System.out.println("\nObjetos televisor");
        System.out.println(tv1);
        System.out.println(tv2);

        System.out.println("\nObjetos instrumentos");
        System.out.println(inst1);
        System.out.println(inst2);
        
        // Demostracion de setters
        System.out.println("\nModificando objetos");
        inst1.setMaterial("Caoba");
        inst1.setTipo("cuerda (acústica)");
        System.out.println("Instrumento modificado: " + inst1);
    }
}
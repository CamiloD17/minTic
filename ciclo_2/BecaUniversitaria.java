// import java.util.*;
// import java.util.Collections;

public class BecaUniversitaria {

    // Atributs
    int pTiempo = 0;
    double pMonto = 0;
    double pInteres = 0;

    // Contructor methods
    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        this.pTiempo = pTiempo;
        this.pInteres = pInteres;
        this.pMonto = pMonto;
    }

    public BecaUniversitaria() {
        pInteres = 0;
        pTiempo = 0;
        pInteres = 0;
    }

    public double calcularInteresSimple() {
        double interesSimple = 0;
        interesSimple = pMonto * (pInteres / 100) * pTiempo;
        return Math.round(interesSimple);

    }

    public double calcularInteresCompuesto() {
        double interesCompuesto = 0;
        interesCompuesto = (pMonto * (Math.pow(((1 + (pInteres / 100))), pTiempo) - 1));
        return Math.round(interesCompuesto);
    }

    public String compararInversion(int pTiempo, double pMonto, double pInteres) {
        this.pTiempo = pTiempo;
        this.pInteres = pInteres;
        this.pMonto = pMonto;
        if (pInteres != 0 && pMonto != 0 && pInteres != 0) {
            double diferencia = 0;
            diferencia = calcularInteresCompuesto() - calcularInteresSimple();
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyeccciones, revisar los parámetros de entrada.";
        }
    }

    public String compararInversion() {
        if (pInteres != 0 && pMonto != 0 && pInteres != 0) {
            double diferencia = 0;
            diferencia = calcularInteresCompuesto() - calcularInteresSimple();
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }
}

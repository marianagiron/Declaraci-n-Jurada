
def crear_grafico(
    tabla,
    columna_nombre,
    columna_valor,
    titulo,
    horizontal=False,
    tipo="bar"
):
    import io
    import base64
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 3.5))

    if tabla.empty:
        ax.text(
            0.5, 0.5,
            "No hay datos disponibles",
            ha="center",
            va="center"
        )
        ax.axis("off")
    else:
        nombres = tabla[columna_nombre].astype(str)
        valores = tabla[columna_valor]

        if tipo == "line":
            ax.plot(nombres, valores, marker="o")
        elif horizontal:
            ax.barh(nombres, valores)
            ax.invert_yaxis()
        else:
            ax.bar(nombres, valores)
            ax.tick_params(axis="x", rotation=25)

        ax.set_title(titulo)
        ax.grid(axis="y", alpha=0.2)
        fig.tight_layout()

    imagen = io.BytesIO()
    fig.savefig(imagen, format="png", dpi=120, bbox_inches="tight")
    plt.close(fig)

    imagen.seek(0)
    return base64.b64encode(imagen.read()).decode("utf-8")

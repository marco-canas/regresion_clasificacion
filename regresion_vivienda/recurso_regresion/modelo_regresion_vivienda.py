

def save_fig(nombre_archivo_imagen):
    import os 
    import matplotlib.pyplot as plt
    ubicacion_para_imagenes = r"C:/Users/marco/Descargas"
    imagen_path = os.path.join(ubicacion_para_imagenes, nombre_archivo_imagen)
    plt.savefig(imagen_path, bbox_inches='tight')
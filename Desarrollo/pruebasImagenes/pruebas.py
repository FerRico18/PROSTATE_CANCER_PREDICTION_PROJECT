import pydicom
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from skimage import exposure

# Ruta al folder donde descomprimiste el dataset
DATA_PATH = "tu_ruta/PROSTATEx/"


# Cargar un estudio (DICOM)
def load_dicom_series(series_path):
    slices = [
        pydicom.dcmread(os.path.join(series_path, f))
        for f in sorted(os.listdir(series_path))
    ]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    volume = np.stack([s.pixel_array for s in slices])
    return volume


# Visualización de una imagen de ejemplo
def show_slice(volume, slice_idx):
    plt.imshow(volume[slice_idx], cmap="gray")
    plt.title(f"Slice {slice_idx}")
    plt.axis("off")
    plt.show()


# Normalización de Intensidades
def normalize(volume):
    volume = volume.astype(np.float32)
    volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume))
    return volume


# Filtro de Ruido (Gaussiano)
def denoise(volume, sigma=1):
    return gaussian_filter(volume, sigma=sigma)


# Prueba rápida
volume = load_dicom_series(DATA_PATH + "ProstateX-0000/T2W")  # Ajusta nombre
show_slice(volume, 15)

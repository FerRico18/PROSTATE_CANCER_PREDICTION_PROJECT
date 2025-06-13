# Predicción Temprana de Cáncer de Próstata usando Inteligencia Artificial

Este proyecto forma parte de la investigación de titulación de la Licenciatura en Ingeniería en Computación en la UAEMex. Su objetivo es desarrollar un sistema de predicción temprana del cáncer de próstata a partir de imágenes médicas DICOM y datos clínicos, utilizando técnicas de aprendizaje automático y procesamiento de imágenes.

## Objetivo
Proponer un modelo híbrido que combine técnicas de extracción de características, procesamiento de regiones de interés (ROIs) en imágenes DICOM y aprendizaje automático para mejorar el diagnóstico temprano del cáncer de próstata.

## Metodología
1. **Recolección de datos**: Dataset con imágenes DICOM de próstata y datos clínicos asociados.
2. **Procesamiento de imágenes**: Identificación y extracción de regiones de interés (ROIs).
3. **Extracción de características (FE)**: Textura, densidad, intensidad y patrones geométricos.
4. **Modelado predictivo**: Entrenamiento de clasificadores (Random Forest, SVM, XGBoost, CNN híbridas).
5. **Evaluación del modelo**: Usando métricas como Accuracy, AUC, Recall, y F1-Score.

## Estructura del proyecto
📂 ProstatePredictionAI
├──

## Tecnologías
- Python 3.10
- NumPy, Pandas, Scikit-learn
- Pydicom, OpenCV
- Matplotlib, Seaborn

## Resultados esperados
- Mejorar la sensibilidad del diagnóstico temprano.
- Reducción de falsos negativos en pacientes con posible desarrollo tumoral.
- Visualización de regiones críticas que influyen en la predicción.

## Artículos base
- Cuadro comparativo y análisis incluidos en el apartado de antecedentes (`antecedentes.md`).

## Autor
María Fernanda Rico Elizarrarás  
Estudiante de Ingeniería en Computación, UAEMex  
Contacto: [mricoe001@alumno.uaemex.mx]  

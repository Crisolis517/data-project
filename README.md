# data-project

Proyecto de práctica de **limpieza y transformación de datos** para la asignatura
M1721 · Bases de Datos para Datos Estructurados, No Estructurados e Introducción
a Big Data para Ciencia de Datos.

- **Institución:** Escuela Superior Politécnica de Chimborazo (ESPOCH)
- **Programa:** Maestría en Estadística con mención en Ciencia de Datos e Inteligencia Artificial
- **Estudiante:** Cristian Solis Aguirre
- **Docente:** Miguel Alfonso Flores Sánchez
- **Cohorte 2 · Paralelo 1 · 2026**

## Objetivo

Practicar el flujo de trabajo completo con Git, GitHub y Visual Studio Code:

`Editar → Revisar → Stage → Commit → Push`

## Estructura

```
data-project/
├── .gitignore
├── README.md
└── suma.py
```

## Uso

```bash
python3 suma.py
```

## Notas

El archivo `.gitignore` evita versionar credenciales (`.env`), entornos
virtuales (`.venv/`), caché de Python (`__pycache__/`), registros (`*.log`)
y archivos del sistema (`.DS_Store`).

> Regla: nunca guardes contraseñas, API keys o tokens directamente en Git.

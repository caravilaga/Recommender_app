FROM continuumio/miniconda3

WORKDIR /app

# Copia la carpeta completa "Datos" al contenedor
COPY Datos /app/Datos

# Copia la carpeta completa "Datos" al contenedor
COPY Resultados /app/Resultados

# Copia también el resto de los archivos del proyecto
COPY . /app/

# Copy the environment.yml file
COPY environment.yml .

# Create conda environment from file
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "venv_", "/bin/bash", "-c"]

# Set entrypoint to use the new environment
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "venv_", "python"]

# Copy your application code
COPY . .

EXPOSE 5000

# Default command (can be overridden)
CMD ["App.py"]
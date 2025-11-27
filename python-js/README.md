# Julieth Sarmiento folder

Instrucciones básicas.

## Virtual Environment

Usando actualmente venv para crear entornos virtuales.

Para crear un entorno virtual:

```bash
python -m venv .venv (nombre de carpeta)
```

Para activar el entorno virtual:

```bash
source .venv/bin/activate (en mac)
```

Para desactivar el entorno virtual:

```bash
deactivate
```

Hay que instalar paquetes con requirements.txt

```bash
pip3 install -r requirements.txt
```

## AWS

AWS requiere .env file para las variables:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION

README - Sitio Web CBC E.I.R.L.

Proyecto desarrollado en Django 5 para la empresa CBC E.I.R.L., dedicada a servicios de construcción, obras civiles, mantenciones y servicios integrales.
El sistema permite mostrar servicios, recibir solicitudes, gestionar cotizaciones y administrarlas desde un panel interno.
Preparado para entorno local y producción en Render.

----------------------------------------
1. Características principales
----------------------------------------
• Sitio web público:
  - Listado de servicios
  - Detalles
  - Formulario de contacto
  - Formulario de cotización
• Panel de administración:
  - Crear/editar servicios
  - Revisar solicitudes
  - Adjuntar presupuestos PDF
  - Marcar estados
• Cloudinary para imágenes
• Render.com para deploy
• Seguridad: HSTS, SSL, CSP, WhiteNoise

----------------------------------------
2. Usuario administrador por defecto
----------------------------------------
Ruta: /create-admin/

Credenciales:
Usuario: admin
Contraseña: Admin1234!

----------------------------------------
3. Requisitos previos
----------------------------------------
• Python 3.10+
• pip
• Git
• Virtualenv (opcional)
• Cuenta Cloudinary

----------------------------------------
4. Instalación en local
----------------------------------------
git clone https://github.com/gustavobugeno/Desarrollo-cbc-eirl.git
cd Desarrollo-cbc-eirl

python -m venv env
env\Scripts\activate       (Windows)
source env/bin/activate      (Linux/Mac)

pip install -r requirements.txt

----------------------------------------
5. Archivo .env requerido
----------------------------------------
ENVIRONMENT=development
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_correo
EMAIL_HOST_PASSWORD=clave_app
DEFAULT_FROM_EMAIL=tu_correo
CLOUDINARY_CLOUD_NAME=xxxxx
CLOUDINARY_API_KEY=xxxxx
CLOUDINARY_API_SECRET=xxxxx
DATABASE_URL=sqlite:///db.sqlite3

----------------------------------------
6. Migraciones
----------------------------------------
python manage.py migrate

----------------------------------------
7. Crear superusuario manual
----------------------------------------
python manage.py createsuperuser

----------------------------------------
8. Ejecutar servidor
----------------------------------------
python manage.py runserver

----------------------------------------
9. Crear admin en producción
----------------------------------------
https://desarrollo-cbc-eirl.onrender.com/create-admin/

----------------------------------------
10. Estructura del proyecto
----------------------------------------
Desarrollo-cbc-eirl/
  cbc/
  core/
  templates/
  media/
  staticfiles/
  build.sh
  render.yaml
  requirements.txt
  manage.py

----------------------------------------
11. Dependencias principales
----------------------------------------
asgiref, Django 5.2.2, django-csp, pillow, numpy, pandas,
cloudinary, whitenoise, psycopg2-binary, dj-database-url.

----------------------------------------
12. Autores
----------------------------------------
Gustavo Bugueño
Cristóbal Ruz
INACAP 2025


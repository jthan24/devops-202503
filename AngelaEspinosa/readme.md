Antes de iniciar

1. Crea un archivo en formato txt que contenga las variables que nos permitirán conectarnos hacia aws desde la consola:
export AWS_ACCESS_KEY_ID=XXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXX
export AWS_REGION=us-east-1

Recuerda que esa información la puedes obtener en tu portal de AWS en la sección de users de IAM, buscas tu usuario y en la pestaña de SECURITY CREDENTIALS en la sección de ACCESS KEYS podrás crear esta llave para que quede asociado a tu usuario y te dé los valores.

2. Una vez ya tengamos nuestro archivo txt, vamos a la consola, nos ubicamos en el directorio donde guardaste tu archivo txt y con el comando CAT NOMBRE_ARHIVO.txt podrás ver su contenido. Una vez logras verlo, solo lo pegas en la consola y le das enter, para que te queden en tu terminal guardadas como variables de entorno.

3. Luego puedes ejecutar el comando "env |grep -i aws" para que te ignore las mayusculas. Listo, ahora puedes usar el siguiente comando para confirmar que si tengas conexión hacia AWS "aws s3 ls".

De esta manera ya tienes tu terminal lista para empezar a usar el archivo "listinstances.py".
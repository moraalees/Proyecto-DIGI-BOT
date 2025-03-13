## *Ciclo de vida del dato (5b):*

### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
- Los datos en mi proyecto son generados cuando un usuario interactúa con el bot y crea o contribuye a una historia. Estos datos se almacenan en una variable llamada 'historia_completa', mientras la historia está activa. Cuando la historia se finaliza o el usuario decide guardarla, la información se guarda en un archivo JSON mediante la función /guardar. Este archivo JSON contiene la historia completa, para que se pueda ver de forma correcta, ya que si es muy larga, en el servidor de Discord no se alcanza a ver entera. Los datos permanecen guardados de forma persistente hasta que el archivo JSON es eliminado manualmente o se sobrescribe por una nueva historia.

### Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
- Cada vez que se activa un comando, se comprueba si la historia está activa o no, demostrando que la consistencia del código es fiable. Al igual pasa para poder guardar o finalizar la historia, se comprueba si existe o no.
- Los datos son respaldados en un archivo JSON que contiene toda la conversación entre el bot y el usuario.

## *Almacenamiento en la nube (5f):*

### Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
- Me propondría emplear un sistema de guardado en la nube óptimo como podrían ser Google Cloud Storage. Este servicio permitiría almacenar diferentes tipos de datos, como todas y cada una de las historias hechas con el usuario además de algunos chistes o sistemas de registros mediante el comando /hola. Así, se podría acceder a estos de forma escalable.

## *Seguridad y regulación (5i):*

### ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

- Utilizo un archivo .env para almacenar de forma segura las claves de acceso (como el token de Discord y la API KEY de OpenRouter). El archivo .env no se sube al repositorio de GitHub gracias al uso de un archivo .gitignore, lo que garantiza que las claves no sean visibles ni accesibles públicamente. Además, las claves solo están disponibles en el entorno de ejecución del bot, lo que reduce el riesgo de exposición.

### ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

- El uso del bot podría verse afectado por normativas como el Reglamento General de Protección de Datos, si se recopilan o procesan datos personales de los usuarios. Afortunadamente, el bot no almacena información personal hasta el momento, salvo la conversación dentro de la historia, que no son datos personales, si no ficticios. Sin embargo, si se decides almacenar información personal o realizar análisis más avanzados, sería necesario asegurarse de que el programa cumpla con el GDPR.

## *Implicación de las THD en negocio y planta (2e):*

### Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

- Este bot podría beneficiar a entornos educativos o de entretenimiento, proporcionando historias con las que pasar el tiempo.. Los usuarios pueden interactuar de forma lúdica con la IA, para mejorar la creatividad gracias a las ingeniosas respuestas del bot al generar historias y experimentar con la automatización de la narrativa.

## *Mejoras en IT y OT (2f):*

### Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

- Para integrar la solución en un entorno IT, en el futuro se podría utilizar el bot en un entorno corporativo que atienda a diferentes dudas, funcionando como un asistente virtual para tareas de atención al cliente, responder preguntas frecuentes o asistir en la generación de contenido automatizado. También, podse podría integrar con herramientas de productividad como calendarios o plataformas de gestión de proyectos para una mejor aplicación de IT/OT.

## *Tecnologías Habilitadoras Digitales (2g):*

### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

- En este proyecto he utilizado la IA a través de OpenRouter, que permite generar respuestas inteligentes basadas en el procesamiento de lenguaje natural del humano. Esta, se utiliza para generar inicios de historias, continuar relatos y ofrecer respuestas interactivas a los usuarios, como sea un buen chiste. Esta tecnología habilitadora digital permite automatizar y enriquecer la experiencia de los usuarios mediante interacciones dinámicas e inteligentes. Además, la IA contribuye a mejorar la personalización y creatividad del bot, haciendo que las interacciones sean más atractivas y útiles que una normal.

### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

- La IA me permite generar contenido dinámico como historias o chistes que se verán influenciadas según lo que el usuario prefiera y decida escribir. También, el uso inteligente de la IA permite ofrecer respuestas a ciertas preguntas o pensamientos del humano, además de enriquecer su experiencia con formas interactivas que parecen naturales.

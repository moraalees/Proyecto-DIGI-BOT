# FASE 1

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

---

# FASE 2

## *Criterio 6a) Objetivos estratégicos:*

### ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?

- En resumidas cuentas, este proyecto fomenta la creatividad y la interacción en entornos digitales, ya que permite a los usuarios colaborar en la creación de historias narrativas de forma dinámica, utilizando la IA como apoyo creativo. También se explora el uso de IA generativa para la realización de contenidos lúdicos, como escribir o narrar historias, lo cual puede alinearse con objetivos estratégicos relacionados con la innovación, la mejora de la experiencia del usuario y la transformación digital de productos interactivos.

### ¿Cómo se alinea el software con la estrategia general de digitalización?

- Este software promueve el uso de tecnologías que últimamente son emergentes, como la IA y su integración en código mediante APIs. Al ser totalmente digital y colaborativo, facilita su implementación en plataformas como Discord sin necesidad de cualquier infraestructura adicional. Por último, refuerza competencias digitales en el desarrollo, documentación y despliegue de software en plataformas como GitHub, GitHub Pages y formas de documentación automática (PDoc).

---

## *Criterio 6b) Áreas de negocio y comunicaciones:*

### ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?

- Las áreas más beneficiadas serían indiscutiblemente las de comunicaciones y producción creativa. El software puede integrarse como una herramienta innovadora para generar contenido narrativo automatizado en cierta manera, ideal para campañas de marketing, storytelling interactivo o experiencias entre el usuario y la IA. Asimismo, puede ser útil para la creación de prototipos rápidos de guiones o contenido en empresas del ámbito audiovisual, educativo o del entretenimiento, al crear historias fascinantes e interesantes.

### ¿Qué impacto operativo esperas en las operaciones diarias?

- Espero una reducción significativa en el tiempo y esfuerzo dedicados a la creación de contenido narrativo, además de una mejora en la interacción con el usuario gracias a respuestas personalizadas y dinámicas, que varían cada vez que la IA es cuestionada. También, se facilita la incorporación de herramientas de IA en flujos de trabajo tradicionales, lo cual impulsa la digitalización y la innovación dentro de la propia empresa.

---

## Criterio 6c) Áreas susceptibles de digitalización:

### ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?

- Las áreas más susceptibles de digitalización relacionadas con este programa son aquellas relacionadas con creación de contenido, atención al cliente y dinámicas de comunicación tanto interna como externa. En sectores creativos puede llegar a reemplazar procesos manuales de escritura o diseño de narrativas, ya que son automatizados en cierta parte. En el ámbito corporativo, podría adaptarse para generar respuestas automáticas, mensajes personalizados, etc.

### ¿Cómo mejorará la digitalización las operaciones en esas áreas?

- La digitalización permitirá automatizar tareas repetitivas, reducir tiempos de producción, y mejorar la experiencia del usuario final al ofrecer respuestas atractivas e interesantess. Además, fomenta una cultura innovadora dentro de la empresa al integrar IA como herramienta de trabajo habitual, potenciando la eficiencia y creatividad en los procesos.

---

## Criterio 6d) Encaje de áreas digitalizadas (AD):

### ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?

- En el estado actual del proyecto, la principal área digitalizada es la generación automática de contenido narrativo mediante IA, que opera en un entorno digital, Discord. Esta funcionalidad no interactúa directamente con áreas no digitalizadas de una empresa, ya que el uso se limita al entorno virtual y no está integrado con flujos u operativos tradicionales.

### ¿Qué soluciones o mejoras propondrías para integrar estas áreas?

- Como no existe actualmente una conexión con áreas no digitalizadas, una posible mejora sería facilitar la exportación del contenido generado para su uso en medios físicos, ya sean libros impresos o materiales educativos. También se podría contemplar formar a usuarios no técnicos para que puedan aprovechar el bot sin necesidad de conocimientos en programación, facilitando así un puente entre lo digital y lo manual.

---

## Criterio 6e) Necesidades presentes y futuras:

### ¿Qué necesidades actuales de la empresa resuelve tu software?

- Como ya se ha comentado previamente, el proyecto cubre principalmente necesidades relacionadas con la creatividad, el entretenimiento digital y la experimentación con IA. Permite generar historias de forma colaborativa entre humanos y una IA, lo cual puede ser útil en ciertos contextos:
  - Fomento de la creatividad en equipos de trabajo o entornos educativos, ofreciendo una herramienta interactiva.
  - Demostración práctica del uso de IA generativa, algo relevante en el contexto actual de digitalización y transformación tecnológica.
  - Mejora del engagement en plataformas sociales como Discord, al introducir una dinámica innovadora.
- Aunque no está enfocado directamente a procesos de negocio clásicos, considero que responde a la necesidad actual de explorar herramientas digitales creativas e integrarlas en dinámicas comunicativas o de formación.

---

## Criterio 6f) Relación con tecnologías:

### ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?

- La IA generativa sería un buen ejemplo, ya que a través de modelos como los proporcionados por OpenRouter, el bot genera contenido narrativo en tiempo real. La Discord API, que se utiliza para la interacción directa con los usuarios mediante comandos personalizados en un servidor, funciona correctamente como una tecnología habilitadora. Además, Python, el lenguaje principal para el desarrollo del bot, es ideal para integrar dicha API y procesar texto. Por último, PDoc y GitHub Pages ayudan a la hora de generar documentación automatizada del código y su publicación web.
- Las diferentes tecnologías impactan de dos maneras diferentes:
  - Área de comunicación y creatividad: Mejora la capacidad de generar contenido dinámico, interactivo y atractivo al humano, en el que este mismo puede participar.
  - Área de formación o entretenimiento digital: Facilita experiencias prácticas en IA y programación, útiles en empresas que exploren la innovación tecnológica.

### ¿Qué beneficios específicos aporta la implantación de estas tecnologías?

Puedo señalar un beneficio por cada tecnología:
- Automatización de procesos creativos mediante la IA generativa.
- Mejora de la interacción digital con usuarios.
- Promueve el aprendizaje técnico sobre APIs, gestión de proyectos y documentación profesional.
- Visibilidad del proyecto mediante la integración con GitHub Pages, además de los archivos HTML que detallan el código generados por PDoc.

---

## Criterio 6g) Brechas de seguridad:

### ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?

He recogido 3 diferentes peligros:
- Claves API: Si las claves de acceso a servicios como OpenRouter no se protegen adecuadamente, podrían ser explotadas de mala manera.
- Mal uso del bot por usuarios: Al ser un bot público en Discord, podría recibir entradas maliciosas o abusivas.
- Fugas de información en entornos compartidos: Si la historia generada contiene datos sensibles o no filtrados adecuadamente, podría suponer algún peligro en la protección de datos.

### ¿Qué medidas concretas propondrías para mitigarlas?

- Aunque ya lo aplique, el uso de archivos .env y la librería dotenv sirven para cargar claves de forma segura, evitando que se expongan en el código fuente. Se podría aplicar una validación de entradas del usuario antes de procesarlas, para evitar que comandos o mensajes sospechosos afecten la IA o el bot y de ahí su comportamiento. El control de permisos del bot en Discord me parece una buena opción, ya que limitaría su uso solo a canales o roles específicos. Para finalizar, aplicar almacenamiento local cifrado para no filtrar esas historias que el usuario genera con la IA de forma privada.

---

## Criterio 6h) Tratamiento de datos y análisis:

### ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?

- En mi proyecto los datos principales que se manejan son los textos generados por usuarios y por la IA. Estos se almacenan de forma temporal en una variable global y, al finalizar una historia, pueden guardarse en un archivo JSON local, a elección del usuario. No se emplean bases de datos externas ni servicios en la nube.

- Se utiliza una estructura modular en el código para garantizar que los datos, en este caso, la historia, se traten de forma ordenada, separando la aportación del usuario, la respuesta de la IA y el cierre de la historia cuando toque.

### ¿Qué haces para garantizar la calidad y consistencia de los datos?

- El sistema verifica que haya una historia activa antes de permitir una aportación o un final, lo cual previene errores lógicos de que si no existe el inicio de la historia, no se puede continuar, como es lógico. Las historias se construyen siguiendo una estructura coherente siguiendo un ciclo de: inicio, aportaciones, respuestas de IA y cuando se decida el final. Esto facilita su lectura drásticamente. Por último, al ser un archivo estructurado, se guarda en formato JSON con indentación, asegurando que los datos sean fácilmente legibles y reutilizables.

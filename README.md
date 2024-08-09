## Sobre este proyecto
![](https://github.com/LeoR22/Proyecto_ia/blob/main/projec_ia.jpg)

# Roop

> Graba un vídeo y reemplaza la cara que aparece con una cara de tu elección. Sólo necesitas una imagen del rostro deseado. Sin conjunto de datos, sin entrenamiento.


[![Build Status](https://img.shields.io/github/actions/workflow/status/s0md3v/roop/ci.yml.svg?branch=main)](https://github.com/s0md3v/roop/actions?query=workflow:ci)

## Manual

Este proyecto incluye un manual detallado que proporciona instrucciones paso a paso sobre cómo utilizar el software de manera efectiva. 
El manual abarca desde la instalación hasta la implementación de las funciones principales del software. 
Puede encontrar el manual Aqui: 

[Descargar Manual del Proyecto](https://github.com/LeoR22/Proyecto_ia/blob/main/Manual.docx)

## Instalación

Tenga en cuenta que la instalación requiere conocimientos técnicos y no es para principiantes. No abra problemas relacionados con la plataforma y la instalación en GitHub.
Por favor, siga las instrucciones detalladas en el manual para garantizar una instalación adecuada. Si encuentra problemas relacionados con la plataforma o la instalación, consulte el manual.


[Descargar Proyecto Colab Pynb](https://github.com/LeoR22/Proyecto_ia/blob/main/Proyecto_IA_Universidad_V_Final.ipynb)


## Uso

Inicie el programa con argumentos:

```
python run.py [options]

-h, --help                                                                 show this help message and exit
-s SOURCE_PATH, --source SOURCE_PATH                                       select an source image
-t TARGET_PATH, --target TARGET_PATH                                       select an target image or video
-o OUTPUT_PATH, --output OUTPUT_PATH                                       select output file or directory
--frame-processor FRAME_PROCESSOR [FRAME_PROCESSOR ...]                    frame processors (choices: face_swapper, face_enhancer, ...)
--keep-fps                                                                 keep target fps
--keep-frames                                                              keep temporary frames
--skip-audio                                                               skip target audio
--many-faces                                                               process every face
--reference-face-position REFERENCE_FACE_POSITION                          position of the reference face
--reference-frame-number REFERENCE_FRAME_NUMBER                            number of the reference frame
--similar-face-distance SIMILAR_FACE_DISTANCE                              face distance used for recognition
--temp-frame-format {jpg,png}                                              image format used for frame extraction
--temp-frame-quality [0-100]                                               image quality used for frame extraction
--output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc}  encoder used for the output video
--output-video-quality [0-100]                                             quality used for the output video
--max-memory MAX_MEMORY                                                    maximum amount of RAM in GB
--execution-provider {cpu} [{cpu} ...]                                     available execution provider (choices: cpu, ...)
--execution-threads EXECUTION_THREADS                                      number of execution threads
-v, --version                                                              show program's version number and exit
```


### Headless

El uso del `-s/--source`, `-t/--target` y el  `-o/--output` argumento ejecutará el programa en modo sin headless.


## Proyecto de Generación de Medios con Inteligencia Artificial

Este proyecto es parte de un trabajo académico tiene como objetivo principal contribuir positivamente a la industria de los medios generados por inteligencia artificial (IA), ofreciendo herramientas educativas para artistas y diseñadores. 
Nuestro software está diseñado específicamente para ayudar en tareas como la animación de personajes y modelos de ropa, brindando a los usuarios la oportunidad de explorar y aprender sobre las capacidades creativas de la IA.

## Ética y Responsabilidad

Estamos comprometidos con la ética en el uso de la IA y hemos implementado medidas para garantizar que nuestro software no se utilice para crear contenido inapropiado, como desnudos. 
Es fundamental que los usuarios sigan las leyes locales y utilicen el software de manera responsable. En caso de utilizar imágenes reales, se requiere obtener el consentimiento y etiquetar claramente cualquier resultado generado por el software.

## Nota Legal

Este proyecto es parte de un trabajo académico y tiene un enfoque educativo. Los desarrolladores no son responsables del uso indebido del software ni de las acciones de los usuarios. 
Se espera que todos los usuarios respeten las normas éticas y legales al utilizar este software.
¡Gracias por ser parte de nuestro proyecto educativo en IA!


## Licencias

Nuestro software utiliza muchas bibliotecas de terceros, así como modelos previamente entrenados. Los usuarios deben tener en cuenta que estos componentes de terceros tienen su propia licencia y términos, por lo que no se aplica nuestra licencia.


## Creditos

- [deepinsight](https://github.com/deepinsight)  y  [insightface](https://github.com/deepinsight/insightface) por su proyecto insightface , que proporcionó una biblioteca y modelos bien hechos.
todos los desarrolladores detrás de las bibliotecas utilizadas en este proyecto


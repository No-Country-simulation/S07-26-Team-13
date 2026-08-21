# Dashboard de Métricas de Campaña: Monetización y Priorización de Leads (Stranded Capacity)

## Resumen Ejecutivo
Este proyecto es una solución analítica integral diseñada para conectar el rendimiento de campañas de marketing B2B con el impacto financiero directo. A través de la simulación de parámetros de infraestructura (Capacidad Varada / MW), la herramienta transforma interacciones de marketing en un "Costo de la Inacción" monetizado, permitiendo al equipo comercial priorizar leads de alto valor.

![Diagrama de la campaña](https://github.com/No-Country-simulation/S07-26-Team-13/blob/main/Proyecto/Data%20Analyst/img/img-readme.png?raw=true)


## Estrategia de Marketing y Generación de Leads
Este proyecto no es solo un tablero de visualización, sino el núcleo de una campaña de marketing B2B (Lead Magnet). La estrategia consistió en:
*	El Gancho (Lead Magnet): Utilizar la "Calculadora de Capacidad Varada" como una herramienta de valor gratuito. A cambio de simular sus parámetros, el usuario recibe un reporte exclusivo.
*	Diseño de Entregables: Creación de los activos visuales y reportes de la campaña utilizando Canva e Illustrator, garantizando una identidad de marca sólida y atractiva para el segmento corporativo.
*	Calificación Automática: La interacción con la campaña (desde la impresión del anuncio hasta el uso de la calculadora) alimenta directamente el embudo de conversión, transformando visitantes anónimos en Marketing Qualified Leads (MQLs) listos para ser priorizados por el equipo comercial en el dashboard.

[🎯Audiencia](https://canva.link/60cdtbjlgu5mjl2)  
[🧩​ Benchmark competitivo](https://canva.link/0jgqttzq9mrylih)  
[♟️​ Plan de contenidos y assets de campaña](https://canva.link/9klm093ua29z2ml)  
[💌​​ Embudo y correos](https://canva.link/wqdc1d252ztwlt0)      
 
## Arquitectura de Datos y Stack Tecnológico

El flujo de datos fue diseñado para ser automatizado y escalable, enfocando los esfuerzos en el análisis y la toma de decisiones:

*	Captura de Datos: Interfaz interactiva construida con Streamlit para la simulación de parámetros por parte del usuario.
*	Automatización (Pipeline): Orquestación con Make para procesar los inputs, registrar los datos históricos en Google Sheets y disparar correos transaccionales vía Gmail.
*	Motor Analítico: Procesamiento y modelado de datos utilizando Python y BigQuery.
*	Visualización Estratégica: Tableau Public para el desarrollo de un producto de datos interactivo, con técnicas avanzadas de UI/UX (filtros aislados por panel, control de tooltips interactivos).
*	Diseño de Entregables: Canva e Illustrator para la identidad visual de los reportes.

![flujo](https://github.com/No-Country-simulation/S07-26-Team-13/blob/main/Proyecto/Data%20Analyst/img/flujo-readme.JPG?raw=true)

[🤖​ Flujo de automatización](https://drive.google.com/drive/folders/1XBMf_iE_nETyeX0kYMnFVgFQUPl8jfNj?usp=sharing) 
 
## La Solución Analítica (Paneles del Dashboard)

El producto final se divide en tres enfoques estratégicos de negocio:

1.	Embudo de Conversión (Rendimiento de Marketing):
*	Análisis end-to-end de impresiones a conversión final.
*	Filtros interactivos por Nombre Pieza para aislar el rendimiento de campañas específicas (Benchmark, Calculadora, Reportes).
2.	Costo de la Inacción (Modelado Financiero):
*	Proyección a 5 años de la pérdida de capital por capacidad varada.
*	Segmentación dinámica por Tipo de Empresa (Colocation, Hyperscaler, etc.) comparando escenarios conservadores vs. tarifarios proyectados.
3.	Calificación de Leads (Priorización Comercial):
*	Matriz de calor que cruza Tamaño de Empresa y Capacidad Varada.
*	Listado de Hot Leads interactivo filtrable por Cargo Usuario, diseñado específicamente para que los fundadores o el equipo de ventas sepan a quién contactar primero.

![Tablero](https://github.com/No-Country-simulation/S07-26-Team-13/blob/main/Proyecto/Data%20Analyst/img/tablero-readme.JPG?raw=true)

 
[​📊 Dashboard](https://public.tableau.com/views/Campana-B2B-DataCenters-F/Panel1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


# S07-26-Team-13
Campaña de Lanzamiento — Marketing &amp; Growth

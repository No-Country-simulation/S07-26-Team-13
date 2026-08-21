# Dashboard de Métricas de Campaña: Monetización y Priorización de Leads (Stranded Capacity)

## Resumen Ejecutivo
Este proyecto es una solución analítica integral diseñada para conectar el rendimiento de campañas de marketing B2B con el impacto financiero directo. A través de la simulación de parámetros de infraestructura (Capacidad Varada / MW), la herramienta transforma interacciones de marketing en un "Costo de la Inacción" monetizado, permitiendo al equipo comercial priorizar leads de alto valor.
 
## Estrategia de Marketing y Generación de Leads
Este proyecto no es solo un tablero de visualización, sino el núcleo de una campaña de marketing B2B (Lead Magnet). La estrategia consistió en:
*	El Gancho (Lead Magnet): Utilizar la "Calculadora de Capacidad Varada" como una herramienta de valor gratuito. A cambio de simular sus parámetros, el usuario recibe un reporte exclusivo.
*	Diseño de Entregables: Creación de los activos visuales y reportes de la campaña utilizando Canva e Illustrator, garantizando una identidad de marca sólida y atractiva para el segmento corporativo.
*	Calificación Automática: La interacción con la campaña (desde la impresión del anuncio hasta el uso de la calculadora) alimenta directamente el embudo de conversión, transformando visitantes anónimos en Marketing Qualified Leads (MQLs) listos para ser priorizados por el equipo comercial en el dashboard.
 
## Arquitectura de Datos y Stack Tecnológico

El flujo de datos fue diseñado para ser automatizado y escalable, enfocando los esfuerzos en el análisis y la toma de decisiones:

*	Captura de Datos: Interfaz interactiva construida con Streamlit para la simulación de parámetros por parte del usuario.
*	Automatización (Pipeline): Orquestación con Make para procesar los inputs, registrar los datos históricos en Google Sheets y disparar correos transaccionales vía Gmail.
*	Motor Analítico: Procesamiento y modelado de datos utilizando Python y BigQuery.
*	Visualización Estratégica: Tableau Public para el desarrollo de un producto de datos interactivo, con técnicas avanzadas de UI/UX (filtros aislados por panel, control de tooltips interactivos).
*	Diseño de Entregables: Canva e Illustrator para la identidad visual de los reportes.
 
## La Solución Analítica (Paneles del Dashboard)

El producto final se divide en tres enfoques estratégicos de negocio:

1.	Embudo de Conversión (Rendimiento de Marketing):
o	Análisis end-to-end de impresiones a conversión final.
o	Filtros interactivos por Nombre Pieza para aislar el rendimiento de campañas específicas (Benchmark, Calculadora, Reportes).
2.	Costo de la Inacción (Modelado Financiero):
o	Proyección a 5 años de la pérdida de capital por capacidad varada.
o	Segmentación dinámica por Tipo de Empresa (Colocation, Hyperscaler, etc.) comparando escenarios conservadores vs. tarifarios proyectados.
3.	Calificación de Leads (Priorización Comercial):
o	Matriz de calor que cruza Tamaño de Empresa y Capacidad Varada.
o	Listado de Hot Leads interactivo filtrable por Cargo Usuario, diseñado específicamente para que los fundadores o el equipo de ventas sepan a quién contactar primero.
 
 
 



# S07-26-Team-13
Campaña de Lanzamiento — Marketing &amp; Growth

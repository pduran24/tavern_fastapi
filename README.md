
# Taberna Inteligente
## 🍺 FASE 1: Cimientos de la Taberna (Backend Core)
**Milestone: Fase 1**: Backend Core & CRUD Objetivo: Tener una API funcional que persista datos. Que existan "cosas" (productos) y "gente" (clientes).

- Issue #1: Configuración inicial y Modelo de Productos
  - Desc: Configurar database.py, models.py (clase Product) y verificar creación de tabla en Docker/Postgres.

- Issue #2: Esquemas Pydantic (Validación)
  - Desc: Crear schemas.py. Definir DTOs para entrada/salida de datos (ProductCreate, ClientCreate, etc.).

- Issue #3: Capa de Acceso a Datos (CRUD)
  - Desc: Crear crud.py. Funciones para leer/escribir en BD sin exponer lógica HTTP.

- Issue #4: Endpoints de Inventario
  - Desc: Crear rutas GET /products y POST /products. Conectar con Swagger UI.

- Issue #5: Gestión de Parroquianos (Clientes)
  - Desc: Crear modelo, esquemas y endpoints para Client. Incluir campo cash (dinero).

## 💰 FASE 2: La Economía (Lógica de Negocio)
**Milestone: Fase 2**: Lógica Transaccional Objetivo: Que las acciones tengan consecuencias. Implementar reglas de negocio para impedir compras ilegales (sin dinero o sin stock).

- Issue #6: Endpoint de Compra (Transacción simple)
  - Desc: Crear ruta POST /transactions/buy. Recibe {client_id, product_id}.
  - Criterios: Debe restar 1 al stock y restar el precio al dinero del cliente.

- Issue #7: Validaciones de Negocio (Exceptions)
  - Desc: Implementar lógica defensiva.
  - Si stock == 0 → Error 400 "¡Se ha acabado la cerveza!".
  - Si client_cash < price → Error 400 "No tienes suficientes monedas".

- Issue #8: Historial de Transacciones (Opcional/Extra)
  - Desc: Crear tabla orders para guardar registro de quién compró qué y cuándo.

- Issue #9: Endpoint de Recarga (Admin)
  - Desc: Una ruta para añadir stock o dar dinero (útil para pruebas). PUT /clients/{id}/add_cash.

## 🤖 FASE 3: El Tavernero IA (Integración LLM)
**Milestone: Fase 3**: Inteligencia Artificial (Backend) Objetivo: Integrar un LLM (OpenAI o local) que interprete el contexto de la base de datos para responder como un personaje.

- Issue #10: Servicio de Integración IA
  - Desc: Configurar API Key (OpenAI/Mistral/Ollama). Crear función generate_tavern_response(prompt).

- Issue #11: Ingeniería del Prompt (Persona)
  - Desc: Diseñar el System Prompt de "Gareth".
  - Ejemplo: "Eres un tavernero medieval rudo. No sabes qué es internet."

- Issue #12: Inyección de Contexto (RAG Básico)
  - Desc: Modificar el endpoint para que lea la BD antes de hablar.
  - Flujo: Usuario habla -> Backend busca: "¿Cuánto dinero tiene el usuario?" -> Backend inyecta info en el prompt -> LLM responde sabiendo si eres rico o pobre.

- Issue #13: Endpoint de Chat
  - Desc: POST /chat. Input: {client_id, message}. Output: {response_text, mood}.

## 🖥️ FASE 4: La Taberna Visible (Frontend Flet)
**Milestone: Fase 4**: Interfaz de Usuario (Full Python) Objetivo: Crear una aplicación de escritorio/web visual usando Flet (Python) que consuma nuestra API.

- Issue #14: Setup de Flet y Cliente HTTP
  - Desc: Estructura del proyecto frontend. Configurar httpx para llamar a localhost:8000.

- Issue #15: Pantalla de "Login" (Selección de Personaje)
  - Desc: Dropdown para elegir usuario existente. Botón "Entrar".

- Issue #16: Pantalla Principal (La Barra)
  - Desc: Grid mostrando productos con su precio y stock. Al hacer click, llama al endpoint de compra y actualiza tu dinero visualmente.

- Issue #17: Interfaz de Chat
  - Desc: Panel lateral o pestaña nueva. Input de texto y área de scroll con los mensajes del Tavernero IA.

- Issue #18: Pulido Visual (Estilo Medieval)
  - Desc: Aplicar fuentes, colores oscuros/madera e iconos acordes a la temática.

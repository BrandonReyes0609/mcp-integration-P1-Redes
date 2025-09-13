# MCP Schedulizer 🧠⏰

Servidor MCP local con protocolo JSON-RPC 2.0 que permite agendar tareas, listarlas, generar horarios y eliminarlas. Se comunica con un chatbot anfitrión para facilitar la interacción.

---

## 📦 Requisitos

- Python 3.8 o superior
- Flask

Instalar dependencias:

```bash
pip install flask
```

---

## ▶️ Ejecución

### 1. Ejecutar el servidor

```bash
python mcp_schedulizer.py
```

Corre en `http://localhost:8000`.

### 2. Ejecutar el cliente (chatbot anfitrión)

```bash
python cliente_chatbot.py
```

---

## 🧪 Pruebas paso a paso

### ✅ Opción 1: Agregar tareas

Ejecutar opción `1` y luego ingresar:

#### Tarea 1

```
Nombre: Revisión informe
Duración: 45
Fecha límite: 2025-09-06T18:00
Prioridad: alta
Categoría: universidad
```

#### Tarea 2

```
Nombre: Lavar ropa
Duración: 30
Fecha límite: 2025-09-08T20:00
Prioridad: media
Categoría: personal
```

#### Tarea 3

```
Nombre: Estudiar Redes
Duración: 120
Fecha límite: 2025-09-10T23:59
Prioridad: alta
Categoría: universidad
```

---

### ✅ Opción 2: Listar tareas

```
Selecciona una opción (1-5): 2
```

### ✅ Opción 3: Generar horario

```
Selecciona una opción (1-5): 3

Fecha de inicio: 2025-09-05
Minutos por día: 240
```

Resultado esperado:

```
Agenda generada:
2025-09-05 08:00 - 08:45 -> Revisión informe
2025-09-06 08:00 - 08:30 -> Lavar ropa
2025-09-07 08:00 - 10:00 -> Estudiar Redes
```

---

### ✅ Opción 4: Eliminar tarea

```
Selecciona una opción (1-5): 4
Nombre de la tarea a eliminar: Lavar ropa
```

Resultado esperado:

```
Respuesta:
{'status': 'tarea eliminada correctamente', 'tareas_restantes': 2}
```

---

### ✅ Opción 5: Salir

```
Selecciona una opción (1-5): 5
```

---

## 📁 Archivos importantes

- `mcp_schedulizer.py` → Servidor Flask JSON-RPC
- `cliente_chatbot.py` → Chatbot anfitrión que interactúa con el servidor
- `tasks_db.json` → Base de datos de tareas

---

Proyecto para el curso **CC3067 - Redes de Computadoras** - Universidad del Valle de Guatemala

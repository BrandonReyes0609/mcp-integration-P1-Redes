
Paso 2: Instalar las dependencias necesarias


```
pip install flask
```

Paso 3: Ejecuta ambos servidores

* Terminal A:

  ```
  cd mcp_official_servers/src/filesystem
  python filesystem_server.py
  ```

Dereia de mostrar algo como:

```
* Running on http://127.0.0.1:5100
```


Teminal B -  Git MCP

```
cd mcp_official_servers/src/git
python git_server.py
```

Deberia de ejecutar en:

```
* Running on http://127.0.0.1:5200
```

Paso 4: Agregar definición en el cliente cliente_chatbot.py

import requests
import time
import psutil
from requests.auth import HTTPBasicAuth

# Configuración de OrientDB
db_name = "Estudiantes_Profecionales"
url = f"http://localhost:2480/command/{db_name}/sql"
headers = {"Content-Type": "application/json"}
auth = HTTPBasicAuth("root", "1234")

# Definir consultas para medir el rendimiento
queries = [
    "SELECT * FROM estudiantes WHERE Edad_cumplida = 23",
    "SELECT COUNT(*) FROM estudiantes"
]

# Inicializar métricas
metrics = {
    "latency": [],
    "cpu_usage": [],
    "memory_usage": []
}

# Ejecutar consultas y medir métricas
for query in queries:
    # Medir uso de CPU y memoria antes de la consulta
    cpu_before = psutil.cpu_percent(interval=1)
    memory_before = psutil.virtual_memory().used

    # Medir tiempo de ejecución de la consulta
    start_time = time.time()
    response = requests.post(url, headers=headers, data=query, auth=auth)
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Medir uso de CPU y memoria después de la consulta
    cpu_after = psutil.cpu_percent(interval=1)
    memory_after = psutil.virtual_memory().used

    # Almacenar métricas
    metrics["latency"].append(elapsed_time)
    metrics["cpu_usage"].append(cpu_after - cpu_before)
    metrics["memory_usage"].append(memory_after - memory_before)

    # Imprimir resultado de la consulta
    if response.status_code == 200:
        print("Consulta exitosa:", query)
    else:
        print("Error en la consulta:", response.status_code, response.text)

# Imprimir métricas recopiladas
print("\nMétricas de rendimiento:")
for i, query in enumerate(queries):
    print(f"Consulta: {query}")
    print(f"  Latencia: {metrics['latency'][i]:.4f} segundos")
    print(f"  Uso de CPU: {metrics['cpu_usage'][i]}%")
    print(f"  Uso de memoria: {metrics['memory_usage'][i] / (1024 * 1024):.2f} MB")
    print("-")

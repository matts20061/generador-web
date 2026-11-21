from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

descripcion = input("Describe la página web que quieres: ")

respuesta = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=descripcion,
    config={
        "system_instruction": (
            "Eres un desarrollador web. Responde solo con un archivo HTML completo, "
            "con el CSS dentro de una etiqueta <style>, sin explicaciones "
            "ni bloques de código markdown."
        )
    },
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(respuesta.text)

print("Listo: abre index.html en el navegador")
"""
PLANES DE MATERIA V2_OK ELABORADOR
"""

#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
from openai import OpenAI
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from docx import Document
import pdfplumber

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener clave API de OpenAI desde variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("No se encontró la clave de API en el archivo .env")

client = OpenAI(api_key=api_key)

# Frase adicional para los prompts
additional_instruction = "Debes entregar una sola respuesta. La respuesta debe seguir el patrón de redacción de los siguientes tres ejemplos: ejemplo1, ejemplo2, ejemplo3."

from docx import Document
import pdfplumber

def extract_examples(directory, keyword):
    examples = []
    try:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            if os.path.isfile(file_path):
                # Leer archivos Word
                if file_name.endswith('.docx'):
                    try:
                        doc = Document(file_path)
                        for paragraph in doc.paragraphs:
                            if keyword.lower() in paragraph.text.lower():
                                examples.append(paragraph.text.strip())
                                if len(examples) == 3:
                                    break
                    except Exception as e:
                        print(f"Error al leer archivo Word: {file_name}, {e}")

                # Leer archivos PDF
                elif file_name.endswith('.pdf'):
                    try:
                        with pdfplumber.open(file_path) as pdf:
                            for page in pdf.pages:
                                text = page.extract_text()
                                if text:
                                    for line in text.splitlines():
                                        if keyword.lower() in line.lower():
                                            examples.append(line.strip())
                                            if len(examples) == 3:
                                                break
                                if len(examples) == 3:
                                    break
                    except Exception as e:
                        print(f"Error al leer archivo PDF: {file_name}, {e}")

            if len(examples) == 3:
                break
    except Exception as e:
        print(f"Error al extraer ejemplos: {e}")

    # Rellenar con valores predeterminados si no se encontraron suficientes ejemplos
    while len(examples) < 3:
        examples.append("Ejemplo por defecto")

    return examples


# Función para generar contenido específico

def generate_content(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto pedagogo en planes de materia"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al generar contenido: {e}")
        return "Contenido no disponible"

# Funciones específicas para cada variable del template

def generate_justification(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "justificación")
    prompt = f"Redacta la justificación de la asignatura '{subject_name}' en un plan de materia. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_competence(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "competencia de la asignatura")
    prompt = f"Describe la competencia principal que debe desarrollar un estudiante en la asignatura '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_competence_area(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "competencia área")
    prompt = f"Especifica la competencia genérica o transversal de la asignatura '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_competence_cycle(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "competencia ciclo")
    prompt = f"Define la competencia específica asociada al ciclo al que pertenece la asignatura '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_profile(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "perfil")
    prompt = f"Describe el perfil profesional esperado al finalizar la asignatura '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_compete(subject_name,Unidad):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "elemento de comptencia")
    prompt = f"Enuncia la principal competencia que habrá adquirido el estudiante al finalizar la asignatura '{Unidad}' del modulo '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)   

def generate_procedurals(subject_name, Unidad):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "procedimental")
    prompt = f"Lista tres saberes procedimentales que se deben desarrollar en la asignatura '{Unidad}' del modulo '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_conceptuals(subject_name, Unidad):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "conceptual")
    prompt = f"Lista tres  saberes conceptuales que se deben desarrollar en la asignatura '{Unidad}' del modulo '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_attitudinals(subject_name, Unidad):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "actitudinal")
    prompt = f"Lista tres saberes actitudinales que se deben desarrollar en la asignatura '{Unidad}' del modulo '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_eval(subject_name, Unidad):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "evaluación de la competencia")
    prompt = f"Proporciona tres formas de evaluar la competencia adquirida de la asignatura '{Unidad}' del modulo '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

def generate_bibliography(subject_name):
    directory = "C:\\Users\\HP\\Desktop\\Planificación Curricular\\Administración\\"
    examples = extract_examples(directory, "bibliografía")
    prompt = f"Proporciona una lista de referencias bibliográficas recomendadas para la asignatura '{subject_name}'. {additional_instruction} Ejemplo1: {examples[0]} Ejemplo2: {examples[1]} Ejemplo3: {examples[2]}"
    return generate_content(prompt)

# Función para llenar el template con el contexto generado
def fill_template_with_response(template_path, output_path, context):
    try:
        doc = DocxTemplate(template_path)
        doc.render(context)
        doc.save(output_path)
        print(f"Template completado guardado en {output_path}")
    except Exception as e:
        print(f"Error al llenar el template: {e}")

# Función principal
def main():
    subject_name = "Técnicas de Gestión de Ventas y Marketing mediante el análisis de datos"
    template_path = r"C:\Users\HP\Desktop\PROPUESTAS DE DIPLOMADO\DIPLOMADO EXCEL Y POWER BI APLICADO A LA GESTION DE VENTAS\PLAN DE MATERIA TEMPLATE\Template plan de materia .docx"
    output_path = f"C:\\Users\\HP\\Desktop\\PROPUESTAS DE DIPLOMADO\\DIPLOMADO EXCEL Y POWER BI APLICADO A LA GESTION DE VENTAS\\PLANES DE MATERIA\\Plan de materia - {subject_name}.docx"


    Unidad_1= "Analisis RFM"
    Unidad_2= "Análisis CLV (customer lifetime value)"
    Unidad_3= "Análisis de churn"
    Unidad_4= "Análisis predictivo"
    Unidad_5= "Análisis de ROI de marketing"

    context = {

        "JUSTIFICACIÓN": generate_justification(subject_name),
        "COMPETENCIA": generate_competence(subject_name),
        "COMPETENCIA_AREA": generate_competence_area(subject_name),
        "COMPETENCIA_CICLO": generate_competence_cycle(subject_name),
        "PERFIL": generate_profile(subject_name),
        "ELEMENTO_COMPETENCIA_1":generate_compete(subject_name,Unidad_1),
        "ELEMENTO_COMPETENCIA_2":generate_compete(subject_name,Unidad_2),
        "ELEMENTO_COMPETENCIA_3":generate_compete(subject_name,Unidad_3),
        "ELEMENTO_COMPETENCIA_4":generate_compete(subject_name,Unidad_4),
        "ELEMENTO_COMPETENCIA_5":generate_compete(subject_name,Unidad_5),
        "PROCEDIMENTALES_1":generate_procedurals(subject_name,Unidad_1),
        "PROCEDIMENTALES_2":generate_procedurals(subject_name,Unidad_2),
        "PROCEDIMENTALES_3":generate_procedurals(subject_name,Unidad_3),
        "PROCEDIMENTALES_4":generate_procedurals(subject_name,Unidad_4),
        "PROCEDIMENTALES_5":generate_procedurals(subject_name,Unidad_5),
        "CONCEPTUALES_1":generate_conceptuals(subject_name,Unidad_1),
        "CONCEPTUALES_2":generate_conceptuals(subject_name,Unidad_2),
        "CONCEPTUALES_3":generate_conceptuals(subject_name,Unidad_3),
        "CONCEPTUALES_4":generate_conceptuals(subject_name,Unidad_4),
        "CONCEPTUALES_5":generate_conceptuals(subject_name,Unidad_5),
        "ACTITUDINALES_1":generate_attitudinals(subject_name,Unidad_1),
        "ACTITUDINALES_2":generate_attitudinals(subject_name,Unidad_2),
        "ACTITUDINALES_3":generate_attitudinals(subject_name,Unidad_3),
        "ACTITUDINALES_4":generate_attitudinals(subject_name,Unidad_4),
        "ACTITUDINALES_5":generate_attitudinals(subject_name,Unidad_5),
        "UNIDAD_1": Unidad_1,
        "UNIDAD_2": Unidad_2,
        "UNIDAD_3": Unidad_3,
        "UNIDAD_4": Unidad_4,
        "UNIDAD_5": Unidad_5,
        "EVAL_COMPET_1":generate_eval(subject_name,Unidad_1),
        "EVAL_COMPET_2":generate_eval(subject_name,Unidad_2),
        "EVAL_COMPET_3":generate_eval(subject_name,Unidad_3),
        "EVAL_COMPET_4":generate_eval(subject_name,Unidad_4),
        "EVAL_COMPET_5":generate_eval(subject_name,Unidad_5),
        "UNIDADES": "\n".join([Unidad_1, Unidad_2, Unidad_3, Unidad_4, Unidad_5]),
        "BIBLIOGRAFÍA": generate_bibliography(subject_name)
    }

    fill_template_with_response(template_path, output_path, context)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





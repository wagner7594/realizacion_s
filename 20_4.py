import requests
import json
import time
import random
import logging
import uuid

# ==================== CONFIGURACIÓN ====================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('constants.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# === TUS DATOS (desde constants.json) ===
AUTH = data["authorization"]
SESSION_TOKEN = data["sessionToken"]
SCHOOL_NAME = data["schoolName"]
USER_ID = data["userId"]
UNITS_TO_COMPLETE = data["unitsToComplete"]

# Headers actualizados
HEADERS_XML = {
    "User-Agent": "Mozilla/5.0",
    "content-type": "text/xml; charset=utf-8",
    "x-rosettastone-app-version": "ZoomCourse/11.11.3",
    "x-rosettastone-protocol-version": "8",
    "x-rosettastone-session-token": SESSION_TOKEN,
}

# ==================== CONFIGURACIÓN MANUAL ====================
UNIDAD_ACTUAL = 20                    # Unidad que ves en pantalla
UNIT_INDEX = "3"                     # Índice real (unidad_visual - 1)
COURSE = "SK-ENG-L5-NA-PE-NA-NA-Y-3"

# ==================== ESTRUCTURA DE LECCIONES ====================

LECCIONES_CONFIG = {
   
    0: {
        "nombre": "leccion principal",
        "path_type": "general",        
        "version": "171121",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_165683599", "challenges": 6},  ### Actividad 1
            {"id": "PATHSTEP_165684054", "challenges": 5},  ### Actividad 2
            {"id": "PATHSTEP_165684059", "challenges": 6},  ### Actividad 3
            {"id": "PATHSTEP_170092407", "challenges": 3},  ### Actividad 4
            {"id": "PATHSTEP_165685309", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_165685285", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_165685311", "challenges": 3},  ### Actividad 7
            {"id": "PATHSTEP_166083987", "challenges": 6},  ### Actividad 8
            {"id": "PATHSTEP_166084266", "challenges": 3},  ### Actividad 9
            {"id": "PATHSTEP_166084263", "challenges": 1},  ### Actividad 10
            {"id": "PATHSTEP_165985080", "challenges": 4},  ### Actividad 11
            {"id": "PATHSTEP_165692325", "challenges": 2},  ### Actividad 12
            {"id": "PATHSTEP_165830128", "challenges": 4},  ### Actividad 13
            {"id": "PATHSTEP_165951686", "challenges": 4},  ### Actividad 14
            {"id": "PATHSTEP_165965183", "challenges": 3},  ### Actividad 15
            {"id": "PATHSTEP_165951789", "challenges": 4},  ### Actividad 16
            {"id": "PATHSTEP_165951820", "challenges": 4},  ### Actividad 17
            {"id": "PATHSTEP_165731516", "challenges": 4},  ### Actividad 18
            {"id": "PATHSTEP_166169845", "challenges": 3},  ### Actividad 19
            {"id": "PATHSTEP_165736910", "challenges": 2},  ### Actividad 20
            {"id": "PATHSTEP_165951839", "challenges": 2},  ### Actividad 21
            {"id": "PATHSTEP_166058776", "challenges": 3},  ### Actividad 22
            {"id": "PATHSTEP_165980455", "challenges": 3},  ### Actividad 23
            {"id": "PATHSTEP_165980472", "challenges": 4},  ### Actividad 24
            {"id": "PATHSTEP_165980487", "challenges": 4},  ### Actividad 25
            {"id": "PATHSTEP_166058814", "challenges": 6},
        ]
    },
    

    1: {
        "nombre": "pronunciacion",
        "path_type": "pronunciation",     
        "version": "159279",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_186476496", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_186476515", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_186476528", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_186476536", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_186476506", "challenges": 6},  ### Actividad 5
            {"id": "PATHSTEP_186476535", "challenges": 2},  ### Actividad 6
            {"id": "PATHSTEP_186476489", "challenges": 2},  ### Actividad 7
            {"id": "PATHSTEP_186476532", "challenges": 3},  ### Actividad 8

        ]
    },


    2: {
        "nombre": "hablar",
        "path_type": "speaking",        
        "version": "177261",
        "lesson_index": "1",
        "actividades": [
            {"id": "PATHSTEP_186593297", "challenges": 2},  ### Actividad 1
            {"id": "PATHSTEP_184968455", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_184968438", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_186593579", "challenges": 3},  ### Actividad 4
            {"id": "PATHSTEP_184968451", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_184968415", "challenges": 2},  ### Actividad 6
            {"id": "PATHSTEP_184968412", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_184968425", "challenges": 6},  ### Actividad 8
            
        ]
    },
   
    3: {
        "nombre": "revision",
        "path_type": "review",        
        "version": "127385",
        "lesson_index": "1",
        "actividades": [
            {"id": "PATHSTEP_186594897", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_185444217", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_185444214", "challenges": 3},  ### Actividad 3
            {"id": "PATHSTEP_185444210", "challenges": 2},  ### Actividad 4
            {"id": "PATHSTEP_185444200", "challenges": 2},  ### Actividad 5
            {"id": "PATHSTEP_185444195", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_185444177", "challenges": 6},  ### Actividad 7
            {"id": "PATHSTEP_185444168", "challenges": 4},
        ]
    },
  

    4: {
        "nombre": "leer",
        "path_type": "reading",        
        "version": "159279",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_186602815", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_186606064", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_186606062", "challenges": 3},  ### Actividad 3
            {"id": "PATHSTEP_186606080", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_186606082", "challenges": 6},  ### Actividad 5
            {"id": "PATHSTEP_186606014", "challenges": 5},  ### Actividad 6
            {"id": "PATHSTEP_186606028", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_186606057", "challenges": 2},  ### Actividad 8
            {"id": "PATHSTEP_186606016", "challenges": 2},  ### Actividad 9
            {"id": "PATHSTEP_186606008", "challenges": 3},  ### Actividad 10
        ]

    },

    5: {
        "nombre": "escuchar",
        "path_type": "listening",        
        "version": "133764",
        "lesson_index": "2",
        "actividades": [
            {"id": "PATHSTEP_186601953", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_186601961", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_186601895", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_186601846", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_186601941", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_186601951", "challenges": 6},  ### Actividad 6
            {"id": "PATHSTEP_186601901", "challenges": 3},  ### Actividad 7
            {"id": "PATHSTEP_186601918", "challenges": 4},  ### Actividad 8

        ]

    },

    6: {
        "nombre": "gramatica",
        "path_type": "grammar",        
        "version": "127695",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_181246088", "challenges": 4},  ### Actividad 1
            {"id": "PATHSTEP_181246090", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_181246144", "challenges": 5},  ### Actividad 3
            {"id": "PATHSTEP_181246122", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_181246165", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_181246104", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_181246150", "challenges": 5},  ### Actividad 7
            {"id": "PATHSTEP_181246139", "challenges": 6},  ### Actividad 8
        ]

    },

    7: {
        "nombre": "escribir",
        "path_type": "writing",        
        "version": "133764",
        "lesson_index": "2",
        "actividades": [
            {"id": "PATHSTEP_185900819", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_185900834", "challenges": 2},  ### Actividad 2
            {"id": "PATHSTEP_185900838", "challenges": 3},  ### Actividad 3
            {"id": "PATHSTEP_185900822", "challenges": 1},  ### Actividad 4
            {"id": "PATHSTEP_185900821", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_185900847", "challenges": 1},  ### Actividad 6
            {"id": "PATHSTEP_185900829", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_185900836", "challenges": 1},  ### Actividad 8
        ]

    },

    8: {
        "nombre": "hablar",
        "path_type": "speaking",        
        "version": "133448",
        "lesson_index": "2",
        "actividades": [
            {"id": "PATHSTEP_184973494", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_186601658", "challenges": 3},  ### Actividad 2
            {"id": "PATHSTEP_184973525", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_184974008", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_184974092", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_184974173", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_184974177", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_186601636", "challenges": 4},  ### Actividad 8
        ]

    },


    9: {
        "nombre": "escuchar",
        "path_type": "listening",        
        "version": "114438",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_186606004", "challenges": 5},  ### Actividad 1
            {"id": "PATHSTEP_186606083", "challenges": 3},  ### Actividad 2
            {"id": "PATHSTEP_186606072", "challenges": 6},  ### Actividad 3
            {"id": "PATHSTEP_186606005", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_186606015", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_186606063", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_186606024", "challenges": 3},  ### Actividad 7
            {"id": "PATHSTEP_186606079", "challenges": 4},  ### Actividad 8

        ]

    },


    10: {
        "nombre": "revision",
        "path_type": "review",        
        "version": "127385",
        "lesson_index": "2",
        "actividades": [
            {"id": "PATHSTEP_185479502", "challenges": 4},  ### Actividad 1
            {"id": "PATHSTEP_185479519", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_185479522", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_185479524", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_185479527", "challenges": 2},  ### Actividad 5
            {"id": "PATHSTEP_185479504", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_185479499", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_185479495", "challenges": 4},  ### Actividad 8
            {"id": "PATHSTEP_186601791", "challenges": 4},  ### Actividad 9
        ]

    },


    11: {
        "nombre": "vocabulario",
        "path_type": "vocabulary",        
        "version": "127385",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_184914138", "challenges": 6},  ### Actividad 1
            {"id": "PATHSTEP_184914146", "challenges": 4},  ### Actividad 2
            {"id": "PATHSTEP_184914143", "challenges": 3},  ### Actividad 3
            {"id": "PATHSTEP_184914127", "challenges": 5},  ### Actividad 4
            {"id": "PATHSTEP_184914141", "challenges": 3},  ### Actividad 5
            {"id": "PATHSTEP_186602820", "challenges": 4},  ### Actividad 6
            {"id": "PATHSTEP_184916508", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_184916446", "challenges": 4},  ### Actividad 8
            {"id": "PATHSTEP_184916452", "challenges": 4},  ### Actividad 9
            {"id": "PATHSTEP_184916477", "challenges": 4},  ### Actividad 10
            {"id": "PATHSTEP_184916470", "challenges": 4},  ### Actividad 11
            {"id": "PATHSTEP_184916478", "challenges": 4},  ### Actividad 12
        ]

    },


    12: {
        "nombre": "hablar",
        "path_type": "speaking",        
        "version": "159279",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_184978079", "challenges": 2},  ### Actividad 1
            {"id": "PATHSTEP_184978065", "challenges": 2},  ### Actividad 2
            {"id": "PATHSTEP_186604727", "challenges": 4},  ### Actividad 3
            {"id": "PATHSTEP_184978085", "challenges": 5},  ### Actividad 4
            {"id": "PATHSTEP_184978094", "challenges": 3},  ### Actividad 5
            {"id": "PATHSTEP_184978068", "challenges": 2},  ### Actividad 6
            {"id": "PATHSTEP_184978055", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_184978097", "challenges": 3},  ### Actividad 8
            {"id": "PATHSTEP_184978087", "challenges": 2},  ### Actividad 9
        ]

    },


    13: {
        "nombre": "revision",
        "path_type": "review",        
        "version": "171121",
        "lesson_index": "3",
        "actividades": [
            {"id": "PATHSTEP_185484148", "challenges": 3},  ### Actividad 1
            {"id": "PATHSTEP_185484165", "challenges": 3},  ### Actividad 2
            {"id": "PATHSTEP_185484134", "challenges": 2},  ### Actividad 3
            {"id": "PATHSTEP_185484169", "challenges": 4},  ### Actividad 4
            {"id": "PATHSTEP_185484139", "challenges": 4},  ### Actividad 5
            {"id": "PATHSTEP_185484128", "challenges": 2},  ### Actividad 6
            {"id": "PATHSTEP_185484114", "challenges": 4},  ### Actividad 7
            {"id": "PATHSTEP_185484122", "challenges": 3},  ### Actividad 8
           
        ]

    },

    14: {
        "nombre": "hito",
        "path_type": "production_milestone",        
        "version": "176985",
        "lesson_index": "4",
        "actividades": [
            {"id": "PATHSTEP_181084731", "challenges": 19},
        ]

    },


    
}

# ==================== IDs A SALTAR ====================
ACTIVIDADES_SALTAR = [
    # Pon aquí IDs que ya están hechas
    # "PATHSTEP_186451037",
]

# ==================== FUNCIÓN PARA CALCULAR TIEMPO ====================
def calcular_tiempo_actividad(challenges, tipo_leccion):
    """Calcula tiempo realista según número de desafíos y tipo de lección"""
    if tipo_leccion == 0:  # Core Lesson
        seg_por_desafio = random.uniform(20, 35)
    elif tipo_leccion == 1:  # Pronunciation
        seg_por_desafio = random.uniform(10, 15)
    elif tipo_leccion == 2:  # Grammar
        seg_por_desafio = random.uniform(25, 45)
    elif tipo_leccion == 3:  # Listening
        seg_por_desafio = random.uniform(20, 30)
    else:  # Review
        seg_por_desafio = random.uniform(20, 30)
    
    tiempo_base = random.uniform(5, 10)
    tiempo_total_seg = tiempo_base + (challenges * seg_por_desafio)
    tiempo_total_seg += random.uniform(1, 3) * challenges
    
    return int(tiempo_total_seg * 1000)

# ==================== FUNCIÓN PARA ENVIAR PATH_STEP_SCORE ====================
def send_path_step_score(step_id, challenges, updated_at, index, version, lesson_index, path_type):
    url = f"https://tracking.rosettastone.com/ee/ce/{SCHOOL_NAME}/users/{USER_ID}/path_step_scores"
    
    params = {
        "course": COURSE,
        "unit_index": UNIT_INDEX,
        "lesson_index": lesson_index,
        "path_type": path_type,
        "occurrence": "1",
        "path_step_media_id": step_id,
        "_method": "put"
    }
    
    xml_body = f"""<path_step_score>
    <course>{COURSE}</course>
    <unit_index>{UNIT_INDEX}</unit_index>
    <lesson_index>{lesson_index}</lesson_index>
    <path_type>{path_type}</path_type>
    <occurrence>1</occurrence>
    <path_step_media_id>{step_id}</path_step_media_id>
    <complete>true</complete>
    <score_correct>{challenges}</score_correct>
    <score_incorrect>0</score_incorrect>
    <score_skipped type="fmcp">0</score_skipped>
    <number_of_challenges>{challenges}</number_of_challenges>
    <speech_was_enabled>true</speech_was_enabled>
    <version>{version}</version>
    <updated_at>{updated_at}</updated_at>
</path_step_score>"""

    headers = HEADERS_XML.copy()
    headers["x-request-id"] = str(uuid.uuid4())
    
    try:
        r = requests.post(url, headers=headers, params=params, data=xml_body.encode('utf-8'))
        if r.status_code == 200:
            logging.info(f"      ✅ {step_id} ({challenges} desafíos)")
            return True
        else:
            logging.warning(f"      ⚠️ Error {r.status_code}: {r.text[:100]}")
            return False
    except Exception as e:
        logging.error(f"      ❌ Excepción: {e}")
        return False

# ==================== FUNCIÓN PARA ENVIAR PATH_SCORE ====================
def send_path_score(total_challenges, updated_at, delta_time, version, lesson_index, path_type):
    url = f"https://tracking.rosettastone.com/ee/ce/{SCHOOL_NAME}/users/{USER_ID}/path_scores"
    
    params = {
        "course": COURSE,
        "unit_index": UNIT_INDEX,
        "lesson_index": lesson_index,
        "path_type": path_type,
        "occurrence": "1",
        "_method": "put"
    }
    
    xml_body = f"""<path_score>
    <course>{COURSE}</course>
    <unit_index>{UNIT_INDEX}</unit_index>
    <lesson_index>{lesson_index}</lesson_index>
    <path_type>{path_type}</path_type>
    <occurrence>1</occurrence>
    <complete>true</complete>
    <score_correct>{total_challenges}</score_correct>
    <score_incorrect>0</score_incorrect>
    <score_skipped type="fmcp">0</score_skipped>
    <number_of_challenges>{total_challenges}</number_of_challenges>
    <delta_time>{delta_time}</delta_time>
    <version>{version}</version>
    <updated_at>{updated_at}</updated_at>
    <is_lagged_review_path>false</is_lagged_review_path>
</path_score>"""

    headers = HEADERS_XML.copy()
    headers["x-request-id"] = str(uuid.uuid4())
    
    try:
        r = requests.post(url, headers=headers, params=params, data=xml_body.encode('utf-8'))
        if r.status_code == 200:
            logging.info(f"  📊 Path score enviado - Total: {total_challenges} desafíos")
            return True
        else:
            logging.warning(f"  ⚠️ Error {r.status_code}: {r.text[:100]}")
            return False
    except Exception as e:
        logging.error(f"  ❌ Error: {e}")
        return False

# ==================== FUNCIÓN PARA PROCESAR UNA LECCIÓN ====================
def procesar_leccion(leccion_id, config):
    """Procesa una lección específica y devuelve estadísticas"""
    version = config["version"]
    lesson_index = config["lesson_index"]
    path_type = config["path_type"]
    actividades = config["actividades"]
    
    # Filtrar actividades a saltar
    saltar_set = set(ACTIVIDADES_SALTAR)
    pendientes = [a for a in actividades if a["id"] not in saltar_set]
    saltadas = [a for a in actividades if a["id"] in saltar_set]
    
    total_saltados = sum(a["challenges"] for a in saltadas)
    
    print(f"\n📖 {config['nombre']}")
    print(f"   Versión: {version}")
    print(f"   Lesson Index: {lesson_index}")
    print(f"   Path Type: {path_type}")
    print(f"   Total: {len(actividades)} actividades")
    print(f"   A saltar: {len(saltadas)} (desafíos: {total_saltados})")
    print(f"   A procesar: {len(pendientes)}")
    
    if not pendientes:
        print("   🎉 ¡Todas las actividades ya están hechas!")
        return {"exitos": 0, "total": 0, "desafios": 0, "tiempo": 0}
    
    # Generar timestamps
    ahora = int(time.time() * 1000)
    timestamps = []
    tiempos = []
    
    for i in range(len(pendientes)):
        ts = ahora + (i * random.randint(45000, 90000))
        timestamps.append(ts)
        tiempos.append(calcular_tiempo_actividad(pendientes[i]["challenges"], leccion_id))
    
    # Enviar actividades
    print(f"\n📤 Procesando {len(pendientes)} actividades...")
    exitos = 0
    tiempo_total_seg = 0
    total_desafios = 0
    
    for i, (act, ts, tiempo_act) in enumerate(zip(pendientes, timestamps, tiempos)):
        total_desafios += act["challenges"]
        tiempo_min = tiempo_act / 1000
        
        logging.info(f"  📌 {i+1}/{len(pendientes)}: {act['id']} ({act['challenges']} desafíos) - {tiempo_min:.0f} seg")
        
        if send_path_step_score(act["id"], act["challenges"], ts, i, version, lesson_index, path_type):
            exitos += 1
            tiempo_total_seg += tiempo_act / 1000
        
        if i < len(pendientes) - 1:
            espera = random.uniform(8, 15)
            logging.info(f"     ⏱️  Esperando {espera:.1f} seg...")
            time.sleep(espera)
            tiempo_total_seg += espera
    
    # Enviar path_score
    if exitos == len(pendientes):
        tiempo_total_ms = int(tiempo_total_seg * 1000)
        
        print("\n📊 ENVIANDO PATH_SCORE...")
        send_path_score(total_desafios, timestamps[-1], tiempo_total_ms, version, lesson_index, path_type)
        
        return {
            "exitos": exitos,
            "total": len(pendientes),
            "desafios": total_desafios,
            "tiempo": tiempo_total_seg,
            "saltados": len(saltadas),
            "desafios_saltados": total_saltados
        }
    else:
        logging.warning(f"⚠️ Fallaron {len(pendientes) - exitos} actividades")
        return {
            "exitos": exitos,
            "total": len(pendientes),
            "desafios": total_desafios,
            "tiempo": tiempo_total_seg,
            "saltados": len(saltadas),
            "desafios_saltados": total_saltados
        }

# ==================== FUNCIÓN PRINCIPAL ====================
def main():
    print("="*70)
    print("🚀 ROSETTA STONE - PROCESAR LECCIÓN")
    print("="*70)
    print(f"Usuario: {USER_ID}")
    print(f"Unidades desde constants.json: {UNITS_TO_COMPLETE}")
    print(f"Unidad actual: {UNIDAD_ACTUAL} (unit_index = {UNIT_INDEX})")
    print("="*70)
    
    # Mostrar lecciones disponibles
    print("\n📚 LECCIONES DISPONIBLES:")
    for idx, config in LECCIONES_CONFIG.items():
        print(f"   {idx}: {config['nombre']}")
        print(f"      - lesson_index: {config['lesson_index']}")
        print(f"      - path_type: {config['path_type']}")
        print(f"      - version: {config['version']}")
        print(f"      - actividades: {len(config['actividades'])}")
        print()
    
    # Opción de selección
    print("\n🔢 OPCIONES DE SELECCIÓN:")
    print("   1. Procesar una lección específica")
    print("   2. Procesar múltiples lecciones (ej: 0,1,2,3)")
    print("   3. Procesar todas las lecciones")
    
    try:
        opcion = input("\n👉 Elige una opción (1, 2 o 3): ").strip()
        
        if opcion == "1":
            # Procesar una lección
            leccion_elegida = int(input(f"\n🔢 ¿Qué lección quieres procesar? (0-{len(LECCIONES_CONFIG)-1}): "))
            if leccion_elegida not in LECCIONES_CONFIG:
                print(f"❌ Lección {leccion_elegida} no existe")
                return
            
            config = LECCIONES_CONFIG[leccion_elegida]
            resultado = procesar_leccion(leccion_elegida, config)
            
            print("\n" + "="*70)
            print("📊 RESUMEN TOTAL:")
            print(f"   Lección: {config['nombre']}")
            print(f"   Actividades: {resultado['exitos']}/{resultado['total']}")
            print(f"   Desafíos procesados: {resultado['desafios']}")
            print(f"   Desafíos saltados: {resultado['desafios_saltados']}")
            print(f"   Tiempo: {resultado['tiempo']:.0f} seg ({resultado['tiempo']/60:.1f} min)")
            print("="*70)
        
        elif opcion == "2":
            # Procesar múltiples lecciones
            lecciones_input = input(f"\n🔢 ¿Qué lecciones quieres procesar? (ej: 0,1,2,3): ")
            lecciones_elegidas = [int(x.strip()) for x in lecciones_input.split(",")]
            
            # Validar
            lecciones_validas = [l for l in lecciones_elegidas if l in LECCIONES_CONFIG]
            if not lecciones_validas:
                print("❌ Ninguna lección válida")
                return
            
            print(f"\n📋 Procesando {len(lecciones_validas)} lecciones: {lecciones_validas}")
            confirm = input("\n¿Continuar? (s/n): ")
            if confirm.lower() != 's':
                print("Cancelado")
                return
            
            resultados = []
            tiempo_total_general = 0
            desafios_total = 0
            actividades_total = 0
            
            for i, leccion_id in enumerate(lecciones_validas):
                print(f"\n{'='*70}")
                print(f"📌 PROCESANDO LECCIÓN {leccion_id} ({i+1}/{len(lecciones_validas)})")
                print(f"{'='*70}")
                
                config = LECCIONES_CONFIG[leccion_id]
                resultado = procesar_leccion(leccion_id, config)
                resultados.append({
                    "id": leccion_id,
                    "nombre": config['nombre'],
                    "resultado": resultado
                })
                
                tiempo_total_general += resultado['tiempo']
                desafios_total += resultado['desafios']
                actividades_total += resultado['exitos']
                
                # Esperar entre lecciones
                if i < len(lecciones_validas) - 1:
                    espera_entre = random.randint(15, 30)
                    print(f"\n⏱️  Esperando {espera_entre} segundos antes de la siguiente lección...")
                    time.sleep(espera_entre)
            
            # Resumen general
            print("\n" + "="*70)
            print("📊 RESUMEN GENERAL - TODAS LAS LECCIONES")
            print("="*70)
            for r in resultados:
                print(f"\n   📖 Lección {r['id']}: {r['nombre']}")
                print(f"      Actividades: {r['resultado']['exitos']}/{r['resultado']['total']}")
                print(f"      Desafíos: {r['resultado']['desafios']}")
                print(f"      Tiempo: {r['resultado']['tiempo']:.0f} seg ({r['resultado']['tiempo']/60:.1f} min)")
            
            print("\n" + "-"*70)
            print(f"📊 TOTALES:")
            print(f"   Actividades completadas: {actividades_total}")
            print(f"   Desafíos completados: {desafios_total}")
            print(f"   Tiempo total: {tiempo_total_general:.0f} seg ({tiempo_total_general/60:.1f} min)")
            print("="*70)
        
        elif opcion == "3":
            # Procesar todas las lecciones
            print(f"\n📋 Procesando TODAS las lecciones ({len(LECCIONES_CONFIG)} lecciones)")
            confirm = input("\n¿Continuar? (s/n): ")
            if confirm.lower() != 's':
                print("Cancelado")
                return
            
            resultados = []
            tiempo_total_general = 0
            desafios_total = 0
            actividades_total = 0
            
            lecciones_ordenadas = sorted(LECCIONES_CONFIG.keys())
            
            for i, leccion_id in enumerate(lecciones_ordenadas):
                print(f"\n{'='*70}")
                print(f"📌 PROCESANDO LECCIÓN {leccion_id} ({i+1}/{len(lecciones_ordenadas)})")
                print(f"{'='*70}")
                
                config = LECCIONES_CONFIG[leccion_id]
                resultado = procesar_leccion(leccion_id, config)
                resultados.append({
                    "id": leccion_id,
                    "nombre": config['nombre'],
                    "resultado": resultado
                })
                
                tiempo_total_general += resultado['tiempo']
                desafios_total += resultado['desafios']
                actividades_total += resultado['exitos']
                
                # Esperar entre lecciones
                if i < len(lecciones_ordenadas) - 1:
                    espera_entre = random.randint(15, 30)
                    print(f"\n⏱️  Esperando {espera_entre} segundos antes de la siguiente lección...")
                    time.sleep(espera_entre)
            
            # Resumen general
            print("\n" + "="*70)
            print("📊 RESUMEN GENERAL - TODAS LAS LECCIONES")
            print("="*70)
            for r in resultados:
                print(f"\n   📖 Lección {r['id']}: {r['nombre']}")
                print(f"      Actividades: {r['resultado']['exitos']}/{r['resultado']['total']}")
                print(f"      Desafíos: {r['resultado']['desafios']}")
                print(f"      Tiempo: {r['resultado']['tiempo']:.0f} seg ({r['resultado']['tiempo']/60:.1f} min)")
            
            print("\n" + "-"*70)
            print(f"📊 TOTALES:")
            print(f"   Actividades completadas: {actividades_total}")
            print(f"   Desafíos completados: {desafios_total}")
            print(f"   Tiempo total: {tiempo_total_general:.0f} seg ({tiempo_total_general/60:.1f} min)")
            print("="*70)
        
        else:
            print("❌ Opción no válida")
            
    except KeyboardInterrupt:
        print("\n⚠️ Interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
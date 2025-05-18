import logging

def main(documents: list):
    if documents:
        for doc in documents:
            km = doc.get("km")
            huella = doc.get("huella")
            user = doc.get("user_id")
            logging.info(f"NUEVO cálculo - Usuario: {user}, {km} km -> {huella} kg CO2")
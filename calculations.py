# Berechnungen

def calculate_costs_and_recycling(material_data):
    costs = {}
    recycling_rates = {}

    # Ist das Material leer?
    if not material_data:
        return costs, recycling_rates  # Leere Dictionaries

    for material, data in material_data.items():
        try:
            # Berechnung der Kosten und Recyclingraten pro Material
            cost_per_unit = data["cost"]
            recycling_percentage = data["recycling"]

            # Hier können weitere Berechnungen hinzugefügt werden, z. B. wenn du Preise für Materialmengen benötigst
            costs[material] = cost_per_unit
            recycling_rates[material] = recycling_percentage
        except Exception as e:
            # Fehlerbehandlung für jeden Materialdatensatz
            print(f"Fehler bei der Berechnung für {material}: {e}")
            costs[material] = 0
            recycling_rates[material] = 0
    
    # Gib immer gültige Werte zurück, auch wenn Fehler aufgetreten sind
    return costs, recycling_rates

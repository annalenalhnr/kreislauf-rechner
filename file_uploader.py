import streamlit as st
import ifcopenshell
import pandas as pd

def upload_and_process_ifc():
    """Lädt die IFC-Datei hoch und extrahiert Materialnamen."""
    uploaded_file = st.file_uploader("Laden Sie Ihre IFC-Datei hoch", type=["ifc"])
    
    if uploaded_file is not None:
        try:
            # Temporäre Datei speichern
            with open("temp.ifc", "wb") as f:
                f.write(uploaded_file.getbuffer())

            # IFC-Modell laden
            ifc_model = ifcopenshell.open("temp.ifc")
            
            # Extrahiere Materialnamen
            material_names = extract_material_names(ifc_model)

            if material_names:
                # Speichern der Materialnamen in Session State
                st.session_state.material_names = material_names
                
                # Materialnamen anzeigen
                material_df = pd.DataFrame({"Material": material_names})
                st.write("Gefundene Materialien:", material_df)

            #    # Weiter-Button, nur wenn Materialien gefunden wurden
            #     if st.button("Weiter zur Eingabe der Materialdaten", key="upload_to_input_button_1"):
            #         st.session_state.page = "input"  # Wechsel zur Eingabeseite

            else:
                st.warning("Keine Materialien in der IFC-Datei gefunden.")
        except Exception as e:
            st.error(f"Fehler beim Verarbeiten der IFC-Datei: {e}")

def extract_material_names(ifc_model):
    """
    Extrahiert Materialnamen aus der IFC-Datei.
    Gibt eine Liste mit Materialnamen zurück.
    """
    material_names = []

    # Gehe alle Relationen von Materialien durch
    for rel in ifc_model.by_type("IfcRelAssociatesMaterial"):
        material = rel.RelatingMaterial
        
        if material and hasattr(material, 'Name') and material.Name:
            material_names.append(material.Name)

    return material_names
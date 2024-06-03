import flet as ft
import random

def main(page: ft.Page):
    # Kérdések és válaszok definiálása
    kerdesek = [
        {
            "kerdes": "Mi Magyarország fővárosa?",
            "valaszok": ["Budapest", "Debrecen", "Szeged", "Pécs"],
            "helyes_valasz": ["Budapest"]
        },
        {
            "kerdes": "Melyik két város található Németországban?",
            "valaszok": ["Berlin", "München", "Barcelona", "Párizs"],
            "helyes_valasz": ["Berlin", "München"]
        },
        {
            "kerdes": "Melyik évben csatlakozott Magyarország az EU-hoz?",
            "valaszok": ["2004", "2007", "2013", "1999"],
            "helyes_valasz": ["2004"]
        },
        {
            "kerdes": "Melyik a legnagyobb kontinens?",
            "valaszok": ["Ázsia", "Afrika", "Európa", "Amerika"],
            "helyes_valasz": ["Ázsia"]
        },
        {
            "kerdes": "Mi a magyar forint rövidítése?",
            "valaszok": ["HUF", "EUR", "USD", "GBP"],
            "helyes_valasz": ["HUF"]
        },
        {
            "kerdes": "Ki írta az 'Egri csillagok' című regényt?",
            "valaszok": ["Gárdonyi Géza", "Jókai Mór", "Móricz Zsigmond", "Mikszáth Kálmán"],
            "helyes_valasz": ["Gárdonyi Géza"]
        },
        {
            "kerdes": "Melyik két elem a víz összetevője?",
            "valaszok": ["Hidrogén", "Oxigén", "Nitrogén", "Szén"],
            "helyes_valasz": ["Hidrogén", "Oxigén"]
        },
        {
            "kerdes": "Melyik bolygó a Naprendszer legnagyobb bolygója?",
            "valaszok": ["Jupiter", "Mars", "Föld", "Szaturnusz"],
            "helyes_valasz": ["Jupiter"]
        },
        {
            "kerdes": "Melyik ország zászlaja piros-fehér-zöld?",
            "valaszok": ["Olaszország", "Magyarország", "Mexikó", "Írország"],
            "helyes_valasz": ["Olaszország", "Magyarország", "Mexikó"]
        },
        {
            "kerdes": "Melyik híres tudós fejezte be az általános relativitáselméletet?",
            "valaszok": ["Albert Einstein", "Isaac Newton", "Nikola Tesla", "Galileo Galilei"],
            "helyes_valasz": ["Albert Einstein"]
        }
    ]

    random.shuffle(kerdesek)
    felhasznalo_valaszok = {}

    def urlap_bekuldese(e):
        eredmeny = 0
        osszes_kerdes = len(kerdesek)

        for idx, kerdes in enumerate(kerdesek):
            helyes_valasz = set(kerdes["helyes_valasz"])
            adott_valasz = felhasznalo_valaszok.get(idx, set())
            if helyes_valasz == adott_valasz:
                eredmeny += 1
        
        eredmeny_szoveg.value = f"Az eredményed: {eredmeny} / {osszes_kerdes}"
        page.update()

    page.title = "Kérdőív"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    kerdesek_widgetek = []

    for idx, kerdes in enumerate(kerdesek):
        kerdes_widget = ft.Column([
            ft.Text(kerdes["kerdes"]),
            ft.Column([
                ft.Checkbox(label=valasz, on_change=lambda e, idx=idx, valasz=valasz: felhasznalo_valaszok.setdefault(idx, set()).add(valasz) if e.control.value else felhasznalo_valaszok[idx].remove(valasz))
                for valasz in random.sample(kerdes["valaszok"], len(kerdes["valaszok"]))
            ])
        ])
        kerdesek_widgetek.append(kerdes_widget)

    bekuldes_gomb = ft.ElevatedButton(text="Beküldés", on_click=urlap_bekuldese)
    eredmeny_szoveg = ft.Text()

    #scroll_view = ft.Container(
        #content=ft.Column(controls=kerdesek_widgetek),
        #scroll=ft.ScrollMode.AUTO,
        #height=400,
    #)

    page.add(
        #scroll_view,
        bekuldes_gomb,
        eredmeny_szoveg
    )

ft.app(target=main)
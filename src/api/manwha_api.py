import requests

def get_manwhas():
    try:
        response = requests.get("https://olympusbiblioteca.com/api/homepage")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching manwhas:", e)
        return []

def get_manwha_details(slug):
    try:
        response = requests.get(f"https://olympusbiblioteca.com/api/series/{slug}?type=comic")
        response.raise_for_status()
        manwha_details = response.json().get("data", {})
        return manwha_details

    except requests.RequestException as e:
        print(f"Error fetching details for {slug}:", e)
        return {}


def get_manwha_chapters_quantity(slug):
    try:
        response = requests.get(f"https://dashboard.olympusbiblioteca.com/api/series/{slug}/chapters?page=1&direction=desc&type=comic")
        response.raise_for_status()
        manwha_chapters = response.json().get("meta", [])
        return manwha_chapters

    except requests.RequestException as e:
        print(f"Error fetching manwha_chapters for {slug}:", e)
        return {}


def get_manwha_chapters(slug, manwha_count_chapters):
    try:
        manwha_chapters = []
        for i in range(1, manwha_count_chapters + 1):
            response = requests.get(f"https://dashboard.olympusbiblioteca.com/api/series/{slug}/chapters?page={i}&direction=asc&type=comic")
            response.raise_for_status()
            manwha_chapters += response.json().get("data", [])
        print(f"total chapters: {len(manwha_chapters)}")
        return manwha_chapters

    except requests.RequestException as e:
        print(f"Error fetching manwha_chapters for {slug}:", e)
        return {}


def get_chapter_images(slug, chapter_id):
    try:
        response = requests.get(f"https://olympusbiblioteca.com/api/capitulo/{slug}/{chapter_id}?type=comic")
        response.raise_for_status()
        data = response.json()
        return data
        
    except requests.RequestException as e:
        print(f"Error al obtener las imágenes del capítulo {slug}/{chapter_id}:", e)
        return {
            "chapter": {"pages": []},
            "prev_chapter": None,
            "next_chapter": None,
            "comic": {"name": "Error"}
        }
        
        
def search_manwhas_query(query):
    try:
        response = requests.get(f"https://dashboard.olympusbiblioteca.com/api/search?name={query}")
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        print("Error fetching manwhas:", e)
        return []
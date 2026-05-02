import PIL.Image
import PIL.ImageStat
import urllib.request
import io

def get_dominant_color(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
        
        img = PIL.Image.open(io.BytesIO(image_data)).convert('RGB')
        
        # Redimensiona para acelerar e suavizar ruídos
        img = img.resize((50, 50))
        
        # Pega a cor média
        stat = PIL.ImageStat.Stat(img)
        avg_color = stat.mean
        rgb = (int(avg_color[0]), int(avg_color[1]), int(avg_color[2]))
        
        # Converte para HEX
        hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        
        return rgb, hex_color
    except Exception as e:
        return str(e)

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSemi3GdNVjswQLPTNSr_eWBoUVlXuQ6M6YxA&s"
print(get_dominant_color(url))

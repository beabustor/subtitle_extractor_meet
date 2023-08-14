import subprocess as sp
import json

# Ruta al archivo de video
videofile = 'Documents/how_ar_int.mp4'

# Obtener metadatos del video usando FFprobe
metadata_cmd = ['ffprobe', '-of', 'json', '-show_entries', 'format:stream', videofile]
metadata_out = sp.run(metadata_cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
metadata = json.loads(metadata_out.stdout)

# Obtener subtítulos en formato WebVTT usando FFmpeg
subtitle_cmd = ['ffmpeg', '-i', videofile, '-map', 's:0', '-f', 'webvtt', '-']
subtitle_out = sp.run(subtitle_cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
subtitle = subtitle_out.stdout

# Guardar subtítulos en un archivo de texto
subtitle_file = 'subtitulos.txt'
with open(subtitle_file, 'w', encoding='utf-8') as f:
    f.write(subtitle)

print(f"Subtítulos guardados en '{subtitle_file}'")

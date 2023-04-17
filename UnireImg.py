from PIL import Image
import PySimpleGUI as sg

# Carica le due immagini PNG che vuoi unire
image1 = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FOTO1 del paziente")
image2 = sg.popup_get_file(sg.FileBrowse(), title="RECUPERA FOTO2 del paziente")


image11 = Image.open(image1)
image22 = Image.open(image2)

# Ottieni le dimensioni dell'immagine risultato
width, height = image11.size

merged_image = Image.new('RGB', (image11.width + image22.width, image11.height))
merged_image.paste(image11, (0, 0))
merged_image.paste(image22, (image11.width, 0))


# Salva l'immagine risultato
merged_image.save("grafic/Immagine_risultato.png")
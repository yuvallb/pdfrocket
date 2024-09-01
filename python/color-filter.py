import fitz  # PyMuPDF
from PIL import Image
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def remap_color(image):
    # Convert image to numpy array
    img_array = np.array(image)

    # Define color mapping (example: invert colors)
    img_array =  (img_array > 100) * 255
    img_array=Image.fromarray(np.uint8(img_array))
    # Convert back to PIL Image
    return img_array
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, dpi=300):
    images = convert_from_path(pdf_path, dpi=dpi)
    return images


    return images

def images_to_pdf(images, output_path):
    c = canvas.Canvas(output_path, pagesize=(2480 ,3508))
    width, height = (2480 ,3508)
    i=0
    for img in images:
        img = img.convert("RGB")
        img.save("temp_image"+str(i)+".jpg")  # Save the image temporarily

        c.drawImage("temp_image"+str(i)+".jpg", 0, 0, width, height)
        i+=1
        c.showPage()

    c.save()

def process_pdf(input_pdf_path, output_pdf_path):
    images = pdf_to_images(input_pdf_path)

    remapped_images = [remap_color(img) for img in images]

    images_to_pdf(remapped_images, output_pdf_path)

# Usage example
input_pdf_path = "input.pdf"
output_pdf_path = "output_filtered.pdf"

process_pdf(input_pdf_path, output_pdf_path)

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi


def pdftotext(filename):
	pdf = wi(filename = filename, resolution = 300)
	pdfImage = pdf.convert('jpeg')

	imageBlobs = []

	for img in pdfImage.sequence:
		imgPage = wi(image = img)
		imageBlobs.append(imgPage.make_blob('jpeg'))

	recognized_text = []

	for imgBlob in imageBlobs:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'ben')
		recognized_text.append(text)

	print(recognized_text)
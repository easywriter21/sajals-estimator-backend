import fitz

def extract_data_from_pdf(file):
    doc = fitz.open(stream=file, filetype="pdf")
    text = ""

    for page in doc:
        text += page.get_text()

    text = text.lower()

    area = None
    floors = None

    for line in text.split("\n"):
        if "area" in line:
            nums = [int(s) for s in line.split() if s.isdigit()]
            if nums:
                area = nums[0]

        if "floor" in line:
            nums = [int(s) for s in line.split() if s.isdigit()]
            if nums:
                floors = nums[0]

    return area, floors

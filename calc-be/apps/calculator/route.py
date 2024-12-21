from fastapi import APIRouter
from fastapi.responses import JSONResponse
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    
    # Analyze the image and get responses
    responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
    
    # Prepare a list to hold the responses
    data_list = []
    
    for response in responses:
        data_list.append(response)
        print('response in route: ', response)  # Print each response inside the loop
    
    return JSONResponse({"message": "Image processed", "data": data_list, "status": "success"})
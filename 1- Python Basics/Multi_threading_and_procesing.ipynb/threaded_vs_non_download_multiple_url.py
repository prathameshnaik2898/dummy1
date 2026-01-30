import requests
import time
import threading


urls = [
    "https://raw.githubusercontent.com/mahavird/Person-Detector-Dataset/refs/heads/master/images/FudanPed00006.png",
    "https://raw.githubusercontent.com/Monalsingh/VideoBroadcaster/refs/heads/main/static/default-office-animated.png",
    "https://raw.githubusercontent.com/A2Amir/Counting-Trees-using-Satellite-Images/refs/heads/main/imgs/5.png"
]

def download_file(process_name, url, file_path ):      # file_path → where to save the file on your system
    try:
        print(f"Download process name Started :{process_name}")
        response = requests.get(url)        # Sends a GET request to the URL, Downloads the content into response,response.content → raw bytes of file
        
        with open(file_path, "wb") as file:         # w is write mode(over writes if file exists) and b is binary mode
            for chunk in response.iter_content(chunk_size = 8192): # Reads the download file piece by piece,Each chunk is 8192 bytes(8KB)
                if chunk:
                    file.write(chunk)
        print("File downloaded Successfully")
    except Exception as e:
        print(f"Error downloading file: {e}")
    print(f"Process name completed: {process_name}")

print("Downloading without threading ")

t1 = time.time()
download_file("Download without thread 1",urls[0],"a.png")
download_file("Download without thread 2",urls[1],"b.png")
download_file("Download without thread 3",urls[2],"c.png")
t2 = time.time()
print(f"Time taken(seconds) : {t2-t1}")

print("Downloading without threading completed ")

#================================================================================================================#
#================================================================================================================#
#================================================================================================================#

print("Downloading with threading......")

t1= threading.Thread(target = download_file, args =("Download with thread 1", urls[0],"a1.png"))   # t1,t2 and t3 are objects
t2= threading.Thread(target = download_file, args =("Download with thread 2", urls[1],"b1.png"))
t3= threading.Thread(target = download_file, args =("Download with thread 3", urls[2],"c1.png")) 


t1_t = time.time()
t1.start()
t2.start()
t3.start()

t1.join()                                        
t2.join()   # join() blocks the main thread until the child thread completes, ensuring correct execution order and accurate timing.
t3.join()

print("Main Program done!!")
t2_t = time.time()
print(f"Time taken(seconds): {t2_t - t1_t}")

print("Downloading with threading completed")
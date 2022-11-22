Install req.txt file
--> pip3 -m install req.txt
To Run the file run python3 flask_app.py
http://127.0.0.1:8080 is the landing page
![Screenshot from 2022-11-22 10-51-32](https://user-images.githubusercontent.com/63957082/203272892-8a7f9a19-b250-4f1d-9622-1d92ca815b52.png)

First you need to run video with either aadhar or pan card by directing to http://127.0.0.1:8080/video_feed/


![Screenshot from 2022-11-22 10-47-00](https://user-images.githubusercontent.com/63957082/203273395-3879b3cb-aec3-4ace-b24a-54781dab5e7c.png)

After this process you have to go to http://127.0.0.1:8080/extract_data/ to extract the data which is being manages automatically by the ocr.


![Screenshot from 2022-11-22 10-48-08](https://user-images.githubusercontent.com/63957082/203273986-055a4cfe-96cd-478c-93ab-a05247c476ac.png)

Now data is being divided into two urls one is aadhar and another is pan url
In order to see aadhar data go to  http://127.0.0.1:8080/index/aadhar/<id>
![Screenshot from 2022-11-22 10-43-38](https://user-images.githubusercontent.com/63957082/203274328-a9df799b-d387-4701-b098-3ebb004bb472.png)

In order to see pan data go to  http://127.0.0.1:8080/index/pan/<id>![Screenshot from 2022-11-22 10-42-49](https://user-images.githubusercontent.com/63957082/203274291-009a68b9-2210-43db-872f-ee1a1e3e78cd.png)

Process -->
You need to go to video_stream page in order to stream the video and segregate aadhar and pan card. Segregated aadhar and pan can be seen using above mentioned urls.Images have been segregated and classified accordingly. After this data extraction is being done by the ocr. From OCR our model extracts the keywords and these keywords are then shown in the UI, along with the type of document.

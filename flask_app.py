from only_detection import detection
import cv2
import threading
from time import time
import multiprocessing
import os
import datetime
# import boto3
from flask import Flask, render_template, Response
from aadhar_pan import extract_data

app = Flask(__name__)

@app.route('/index/aadhar/<id>')
def show_index(id):
    # pan_c = os.listdir('static/data/pan')
    #
    # pan_c = ['data/pan/' + file for file in pan_c]
    # print("pan_c",pan_c)

    aadhar_c = os.listdir('static/data/aadhar')
    aadhar_c = ['data/aadhar/' + file for file in aadhar_c]
    print('aadhar_c value is ',aadhar_c)

    face_f = os.listdir('static/data/face')
    face_f = ['data/face/' + file for file in face_f]
    print('face value is ',face_f)


    name = value()
    jsonData = name["ID Type"]

    if jsonData=="Adhaar":
        return render_template('index.html',aadhar_c=aadhar_c,face_f=face_f,name=name)
    # return

@app.route('/index/pan/<id>')
def show_pan(id):
    pan_c = os.listdir('static/data/pan')

    pan_c = ['data/pan/' + file for file in pan_c]
    print("pan_c",pan_c)

    face_f = os.listdir('static/data/face')
    face_f = ['data/face/' + file for file in face_f]
    print('face value is ',face_f)
    name = value()
    jsonData = name["ID Type"]

    if jsonData=="PAN":

        return render_template('pan.html', pan_c = pan_c,face_f=face_f,name=name)

def yolo_v4():

    cap =  cv2.VideoCapture(0)

    # success,image = self.gen_frames("ucCPm3MMSbPmzxWcvd1zb5").read()

    previous = time()
    yolo_v4.delta = 0
    while True:
        (success,image) = cap.read()
        current = time()

        yolo_v4.delta += current - previous
        previous = current
        frame = image
        # frame = camera.do_something()
        # detection(frame, 0.5)
        create_alert(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def create_alert(frame):

    try:

        info = detection(frame)

        # print(run_video.count)
        x,y,w,h,label,conf = info[0]
        ct = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        if label == "aadhar":
            crop_img = frame[y:y+h,x:x+w]
            # run_video.count+=1
            cv2.imwrite("static/data/aadhar/img_aadhar_"+str(ct)+".jpg",crop_img)
            # time_screenshot()

            # take_screenshot(frame,run_video.count)


            # print( .count)
            print("Alert!!! Condition not met")

            # cv2.imwrite("img_"+str(count)+".jpg",f)
        if label == "pan":
            crop_img = frame[y:y+h,x:x+w]
            # run_video.count+=1
            cv2.imwrite("static/data/pan/img_pan_"+str(ct)+".jpg",crop_img)

        if label == "face":
            crop_img = frame[y:y+h,x:x+w]
            # run_video.count+=1
            cv2.imwrite("static/data/face/img_face_"+str(ct)+".jpg",crop_img)

    except Exception as e:
        print("_______-",e)

# def take_screenshot(frame,count):
#     if not os.path.exists('screen_shot'):
#        os.makedirs('screen_shot')
#     if run_video.delta > 3:
#         cv2.imwrite("screen_shot/img_"+str(count)+".jpg",frame)
#         # print("Ready to capture")
#         run_video.delta = 0


# def write_video(frame):
#
@app.route('/video_feed/')
def enter_stream_name():

    return Response(yolo_v4(),mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/value')
def value():
    import json
    input_file = open('info.json','r')
    json_decode = json.load(input_file)

    # print(json_decode)
    # jsonData = json_decode["Adhaar Number"]
    # ID Type
    return json_decode



@app.route('/extract_data/')
def extracting_data():
    extract_data()
    return "Data Extracted. Go to index"





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080,threaded=True)


# thread2.join()
# thread1.join()

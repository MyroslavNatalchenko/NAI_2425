#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>
using namespace std;
using namespace cv;

//void detectAndDisplay( Mat frame );

std::vector<cv::Rect> detectFaces(const Mat &frame_gray);
Mat drawFaces(Mat frame, const std::vector<cv::Rect> &faces);

CascadeClassifier face_cascade;
CascadeClassifier eyes_cascade;
int main( int argc, const char** argv )
{
    CommandLineParser parser(argc, argv,
                             "{help h||}"
                             "{face_cascade|data/haarcascades/haarcascade_frontalface_alt.xml|Path to face cascade.}"
                             "{eyes_cascade|data/haarcascades/haarcascade_eye_tree_eyeglasses.xml|Path to eyes cascade.}"
                             "{camera|0|Camera device number.}");
    parser.about( "\nThis program demonstrates using the cv::CascadeClassifier class to detect objects (Face + eyes) in a video stream.\n"
                  "You can use Haar or LBP features.\n\n" );
    parser.printMessage();
    String face_cascade_name = samples::findFile( parser.get<String>("face_cascade") );
    String eyes_cascade_name = samples::findFile( parser.get<String>("eyes_cascade") );
    //-- 1. Load the cascades
    if( !face_cascade.load( face_cascade_name ) )
    {
        cout << "--(!)Error loading face cascade\n";
        return -1;
    };
    if( !eyes_cascade.load( eyes_cascade_name ) )
    {
        cout << "--(!)Error loading eyes cascade\n";
        return -1;
    };
    int camera_device = parser.get<int>("camera");
    VideoCapture capture;
    //-- 2. Read the video stream
    capture.open( camera_device );
    if ( ! capture.isOpened() )
    {
        cout << "--(!)Error opening video capture\n";
        return -1;
    }
    Mat frame;
    while (capture.read(frame))
    {
        if(frame.empty())
        {
            cout << "--(!) No captured frame -- Break!\n";
            break;
        }
        // Szkala szarości - z zeszłej funkcji drawAndDisplay
        Mat frame_gray;
        cvtColor(frame, frame_gray, COLOR_BGR2GRAY);
        equalizeHist(frame_gray, frame_gray);

        int max=-1;
        // 2. Funkcja która zwraca wszystkie twarzy które mają 2 oczy
        std::vector<cv::Rect> faces = detectFaces(frame_gray);
        cout << "Ilość twarz na ekranie: " << faces.size() << endl;
        if (faces.size() > max){
            max = faces.size();
        }

        // 3. Rysowanie twarzy
        frame = drawFaces(frame, faces);
        cv::flip(frame, frame, 1); //odbicie w lustrze
        imshow("Capture - Face detection", frame);

        if( waitKey(10) == 27 )
        {
            cout << "Maksymalna ilość wykrytych twarz: " << max << endl;
            break; // escape
        }
    }
    return 0;
}

std::vector<cv::Rect> detectFaces(const Mat &frame_gray) // & - wskaźnik (adres). Unika kopijowania dannych
{
    std::vector<cv::Rect> faces;
    face_cascade.detectMultiScale(frame_gray, faces);

    // Filtrowanie twarzy, które mają oczy
    std::vector<cv::Rect> valid_faces;
    for (size_t i = 0; i < faces.size(); i++)
    {
        Mat faceROI = frame_gray(faces[i]);
        std::vector<cv::Rect> eyes;
        eyes_cascade.detectMultiScale(faceROI, eyes);

        if (eyes.size() > 1) // 2+ oczy
        {
            valid_faces.push_back(faces[i]);
        }
    }

    // Filtrowanie nakładających się twarzy
    std::vector<cv::Rect> filtered_list_of_faces;
    for (size_t i = 0; i < valid_faces.size(); i++) {
        bool check_if_not_copy = true;
        for (size_t j = 0; j < valid_faces.size(); j++) {
            if (i!=j) {
                if ((valid_faces[i] & valid_faces[j]) == valid_faces[i]) { //przez nakładanie możemy sprawdzić czy są jednakowe
                    check_if_not_copy = false;
                    break;
                }
            }
        }
        if (check_if_not_copy) {
            filtered_list_of_faces.push_back(valid_faces[i]);
        }
    }

    return filtered_list_of_faces;
}

Mat drawFaces(Mat frame, const std::vector<cv::Rect> &faces)
{
    for (size_t i = 0; i < faces.size(); i++)
    {
        Point center(faces[i].x + faces[i].width / 2, faces[i].y + faces[i].height / 2);
        ellipse(frame, center, Size(faces[i].width / 2, faces[i].height / 2), 0, 0, 360, Scalar(255, 0, 255), 4);
    }

    return frame;
}

//void detectAndDisplay( Mat frame )
//{
//    Mat frame_gray;
//    cvtColor( frame, frame_gray, COLOR_BGR2GRAY );
//    equalizeHist( frame_gray, frame_gray );
//    //-- Detect faces
//    std::vector<Rect> faces;
//    face_cascade.detectMultiScale( frame_gray, faces );
//    for ( size_t i = 0; i < faces.size(); i++ )
//    {
//        Mat faceROI = frame_gray( faces[i] );
//        //-- In each face, detect eyes
//        std::vector<Rect> eyes;
//        eyes_cascade.detectMultiScale( faceROI, eyes );
//
//        if (eyes.size()>1){ //przynajmniej 2 oka dla jednej twarzy
//            Point center( faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2 );
//            ellipse( frame, center, Size( faces[i].width/2, faces[i].height/2 ), 0, 0, 360, Scalar( 255, 0, 255 ), 4 );
//            for ( size_t j = 0; j < eyes.size(); j++ )
//            {
//                Point eye_center( faces[i].x + eyes[j].x + eyes[j].width/2, faces[i].y + eyes[j].y + eyes[j].height/2 );
//                int radius = cvRound( (eyes[j].width + eyes[j].height)*0.25 );
//                circle( frame, eye_center, radius, Scalar( 255, 0, 0 ), 4 );
//            }
//        }
//    }
//    //-- Show what you got
//    imshow( "Capture - Face detection", frame );
//}

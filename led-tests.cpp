// g++ led-tests.cpp -oleds -L$HOME/Raspi/display32x32/rpi-rgb-led-matrix/lib -lrgbmatrix -lrt -lm -lpthread -std=c++0x


#include </home/pi/Raspi/display32x32/rpi-rgb-led-matrix/include/led-matrix.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <iostream>

using namespace rgb_matrix;
using namespace std; 


static void DrawOnCanvas(Canvas *canvas) {
  /*
   * Let's create a simple animation. We use the canvas to draw
   * pixels. We wait between each step to have a slower animation.
   */
  canvas->Fill(0, 0, 255);

  int center_x = canvas->width() / 2;
  int center_y = canvas->height() / 2;
  float radius_max = canvas->width() / 2;
  float angle_step = 1.0 / 360;
  for (float a = 0, r = 0; r < radius_max; a += angle_step, r += angle_step) {
    float dot_x = cos(a * 2 * M_PI) * r;
    float dot_y = sin(a * 2 * M_PI) * r;
    canvas->SetPixel(center_x + dot_x, center_y + dot_y,
                     255, 0, 0);
    usleep(1 * 1000);  // wait a little to slow down things.
  }
}

static void drawStraightLine(Canvas *canvas, int x1, int y1, int x2, int y2, int R, int G, int B) {
	//correct coordinates
	y1 = 31 - y1;
	y2 = 31 - y2;
	//int temp = 0;	
	int yDiff = abs(y2 - y1); 
	int xDiff = abs(x2 - x1); 
	
	//draw the line
	if (x1 == x2) {
		for (int i = 0; i <= yDiff; i++) {
			canvas->SetPixel(x1, y1 - i, R, G, B);
			//usleep(100);
		}
	}
	else if (y1 == y2) {
		for (int i = 0; i <= xDiff; i++) {
			canvas->SetPixel(x1 + i, y1, R, G, B);
			//usleep(100);
		}
	}
	else {
		std::cout << "straight lines only please." << std::endl;
	}
}

static void lightLines(Canvas *canvas, bool up, vector<int> nums, int R, int G, int B) {
	int size = nums.size();
	
	if (up) {
		for (int i = 0; i < size; i++) {
			drawStraightLine(canvas,i,0,i,nums[i],R,G,B);
			usleep(30000);
		}
	}
	else {
		for (int i = 0; i < size; i++) {
			drawStraightLine(canvas,i,31-nums[i],i,31,R,G,B);
			usleep(30000);
		}
	}
}

static void setBepis(Canvas *canvas) {
	//B
	drawStraightLine(canvas,3,13,3,23,255,0,0);
	drawStraightLine(canvas,3,19,3,23,255,0,0);
	drawStraightLine(canvas,3,13,3,17,255,0,0);
	drawStraightLine(canvas,3,18,7,18,255,0,0);
	drawStraightLine(canvas,3,13,8,13,255,0,0);
	drawStraightLine(canvas,8,13,8,17,255,0,0);
	drawStraightLine(canvas,8,19,8,23,255,0,0);
	drawStraightLine(canvas,3,23,8,23,255,0,0);
	//E
	drawStraightLine(canvas,10,13,10,23,0,255,0);
	drawStraightLine(canvas,10,13,15,13,0,255,0);
	drawStraightLine(canvas,10,18,15,18,0,255,0);
	drawStraightLine(canvas,10,23,15,23,0,255,0);
	//P
	drawStraightLine(canvas,17,13,17,23,0,0,255);
	drawStraightLine(canvas,21,18,21,23,0,0,255);
	drawStraightLine(canvas,17,23,21,23,0,0,255);
	drawStraightLine(canvas,17,18,21,18,0,0,255);
	//I
	drawStraightLine(canvas,23,13,23,23,0,255,0);
	//S
	drawStraightLine(canvas,25,13,29,13,255,0,0);
	drawStraightLine(canvas,25,18,29,18,255,0,0);
	drawStraightLine(canvas,25,23,29,23,255,0,0);
	drawStraightLine(canvas,25,18,25,23,255,0,0);
	drawStraightLine(canvas,29,13,29,18,255,0,0);
}

int main(int argc, char *argv[]) {
  /*
   * Set up GPIO pins. This fails when not running as root.
   */
  GPIO io;
  if (!io.Init())
    return 1;
    
  /*
   * Set up the RGBMatrix. It implements a 'Canvas' interface.
   */
  int rows = 32;    // A 32x32 display. Use 16 when this is a 16x32 display.
  int chain = 1;    // Number of boards chained together.
  int parallel = 1; // Number of chains in parallel (1..3). > 1 for plus or Pi2
  Canvas *canvas = new RGBMatrix(&io, rows, chain, parallel);
  
  vector<int> nums1 {0 ,2 ,4 ,6 ,8 ,10,12,10,8 ,10,12,10,8 ,6 ,4 ,2 ,2 ,4 ,6 ,8 ,10,12,10,8 ,10,12,10,8 ,6 ,4 ,2 ,0 };
  vector<int> nums2 {31,29,27,25,23,21,19,21,23,21,19,21,23,25,27,29,29,27,25,23,21,19,21,23,21,19,21,23,25,27,29,31};
  vector<int> nums3 {0 ,0 ,2 ,4 ,6 ,8 ,10,8 ,6 ,8 ,10,8 ,6 ,4 ,2 ,0 ,0 ,2 ,4 ,6 ,8 ,10,8 ,6 ,8 ,10,8 ,6 ,4 ,2 ,0 ,0 };
  vector<int> nums4 {31,31,29,27,25,23,21,23,25,23,21,23,25,27,29,31,31,29,27,25,23,21,23,25,23,21,23,25,27,29,31,31};
  
  
  lightLines(canvas,1,nums1,10,10,255);    // Using the canvas.
  lightLines(canvas,0,nums2,20,255,10);
  lightLines(canvas,1,nums3,20,10,240);
  lightLines(canvas,0,nums4,60,10,25);
  sleep(1);
  setBepis(canvas);
  sleep(5);  
  // Animation finished. Shut down the RGB matrix.
  canvas->Clear();
  delete canvas;

  return 0;
}

//#define _CRT_SECURE_NO_WARNINGS
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
void error_cmd() {
	FILE* fp;
	fp = fopen("translate.txt", "w+");
	fprintf(fp, "Error");
	fclose(fp);
}
int main(int argc, char *argv[]) {
	char* bt;
	char urlmain[2048];
	char merge_text[2048] = "";
	char main_text[2048] = "";
	char _url1[] = "https://script.google.com/macros/s/AKfycbwirkwEL1WaWKegnXgaUqq9LRHECuDj8XIjGDND67xzOQfBqxU/exec?text=";
	bt = strtok(argv[2], " ");
	for (;;) {
		if (bt == NULL)
			break;
		strcat(merge_text, bt);
		strcat(merge_text, "%20");
		bt = strtok(NULL, " ");
	}

	merge_text[strlen(merge_text) - 3] = '\0';
	if (merge_text == '\0') {
		error_cmd();
		return 0;
	}
	sprintf(urlmain, "chcp 65001 & curl -L \"%s%s%s%s\"%s", "", _url1, merge_text, argv[1], " > translate.txt");
	system(urlmain);
	return 0;
}

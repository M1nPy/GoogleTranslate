function doGet(e) {
    var a = e.parameter;
    var translatedText = LanguageApp.translate(a.text, a.source, a.target);
    var body;
    if (translatedText) {
        body = translatedText
        ;
    } else {
        body = {
          code: 400,
          text: "Bad Request"
        };
    }
    // レスポンス
    var response = ContentService.createTextOutput(body);
    response.setMimeType(ContentService.MimeType.TEXT);
    return response;
}
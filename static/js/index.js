
var markers = [{ "position": "128.3657142857143", "markerPosition": "7" },
{ "position": "235.1944023323615", "markerPosition": "19" },
{ "position": "42.5978231292517", "markerPosition": "-3" }];



function postReqest(){
    text = "hello"
    tttt = "world"
    $.ajax({
        type: 'POST',
        url: '/data',
        data: JSON.stringify({ Markers: markers }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",

        success: function(){console.log('Got Device Information');},
        mimeType: 'text'
      });
}
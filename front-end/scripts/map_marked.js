/**
 * Created by rlawk on 2017-08-19.
 */
var myArray;
init();
function init(){

    myArray = new Array()
}

function myMap() {
  var myCenter = new google.maps.LatLng(51.508742,-0.120850);
  var myCenter1 = new google.maps.LatLng(a,-0.120850);
  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 5};
  var map = new google.maps.Map(mapCanvas, mapOptions);

  for(var i = 0; i < 1;i++) {
      var marker = new google.maps.Marker({position: markArray});

      marker.setMap(map);
  }
  // Zoom to 9 when clicking on marker
  google.maps.event.addListener(marker,'load',function() {
    map.setZoom(9);
    map.setCenter(marker.getPosition());
  });
}
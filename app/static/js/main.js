var map;
var location_marker;
var list;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    });
}

function update_map(lat, lng) {
    var location = new google.maps.LatLng(lat, lng);
    map.setCenter(location);
    location_marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

function get_jobs() {

}


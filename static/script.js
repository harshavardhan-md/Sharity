// Get current location and fill address input
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("locationButton").addEventListener("click", function() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var userLatitude = position.coords.latitude;
                var userLongitude = position.coords.longitude;
                
                // Search for nearby locations using OpenStreetMap Nominatim API
                var url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${userLatitude}&lon=${userLongitude}&addressdetails=1`;
                fetch(url)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        var address = data.address;
                        var completeAddress = `${address.road || ''}, ${address.suburb || ''}, ${address.city || ''}, ${address.state || ''}, ${address.country || ''}`;
                        document.getElementById("location").value = completeAddress;
                    })
                    .catch(error => {
                        console.error("Error getting location details:", error);
                        document.getElementById("locationDisplay").innerHTML = "Error getting location details";
                    });
            });
        } else {
            document.getElementById("locationDisplay").innerHTML = "Geolocation is not supported by this browser.";
        }
    });

    // Get directions to Shri Swami Sant Dass Udaasin Aashram
    document.getElementById("getDirectionsButton").addEventListener("click", function() {
        // Destination coordinates for Shri Swami Sant Dass Udaasin Aashram in Jalandhar
        var destinationLatitude = 31.3260; // Replace with actual latitude
        var destinationLongitude = 75.5762; // Replace with actual longitude

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var userLatitude = position.coords.latitude;
                var userLongitude = position.coords.longitude;
                
                // Open Google Maps with directions from current location to destination
                var googleMapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${userLatitude},${userLongitude}&destination=${destinationLatitude},${destinationLongitude}`;
                window.open(googleMapsUrl, "_blank");
            });
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    });
});

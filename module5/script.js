require([
  "esri/config",
  "esri/Map",
  "esri/views/MapView",
  "esri/widgets/Search",
  "esri/Graphic",
  "esri/rest/locator",
], function (
  esriConfig,
  Map,
  MapView,
  Search,
  Graphic,
  locator
) {

  // personal key you get when creating an account
  esriConfig.apiKey =
    "AAPKb5e85b9a05094518bae3e354702dd925tXnugQuLKZ1E2-8mqOGMcgwYGeXie6ZNF0QnWLyYdKUUxpgHygzy-t9CITenrolG";

    // base map layer... different base maps will have different asthetic and functional features to use.
  const map = new Map({
    basemap: "arcgis-navigation", // Basemap layer service
  });

  const view = new MapView({
    map: map,
    center: [-111.7924237, 43.8231096], // Longitude, latitude
    zoom: 13, // Zoom level
    container: "viewDiv", // Div element
  });

  const locatorUrl = "http://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer";

  const places = ["Choose a place type:", "Restaurant", "Gas Station", "Park"]

  const select = document.createElement("select","");
      select.setAttribute("class", "esri-widget esri-select");
      select.setAttribute("style", "width: 175px; font-family: 'Avenir Next W00'; font-size: 1em;");

      places.forEach(function(p){
        const option = document.createElement("option");
        option.value = p;
        option.innerHTML = p;
        select.appendChild(option);
      });

      view.ui.add(select, "top-right");

      function findPlaces(category, pt) {
        locator.addressToLocations(locatorUrl, {
          location: pt,
          categories: [category],
          maxLocations: 25,
          outFields: ["Place_addr", "PlaceName"]
        })

        .then(function(results) {
          view.popup.close();
          view.graphics.removeAll();

          results.forEach(function(result){
            view.graphics.add(
              new Graphic({
                attributes: result.attributes,  // Data attributes returned
                geometry: result.location, // Point returned
                symbol: {
                 type: "simple-marker",
                 color: "#398557",
                 size: "12px",
                 outline: {
                   color: "#62676A",
                   width: "2px"
                 }
                },
    
                popupTemplate: {
                  title: "{PlaceName}", // Data attribute names
                  id: "popUpTemplate",
                  content: "{Place_addr}",
                }
             }));
          });
    
        });
    
      }
      view.watch("stationary", function(val) {
        if (val) {
           findPlaces(select.value, view.center);
        }
        });

        select.addEventListener('change', function (event) {
          findPlaces(event.target.value, view.center);
        });
  
  const search = new Search({
      //Add Search widget
      view: view,
    });
    view.ui.add(search, "top-right");
    search.setAttribute("style", "margin-bottom: 75px");

  });

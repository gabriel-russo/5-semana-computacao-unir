/*
    Criando um mapa interativo com Leaflet!
 */

/*
Criando instanciando o Objeto mapa Leaflet
 */
var map = L.map('map', {
    center: [-8.748, -63.8757],
    zoom: 6
});

/*
    Adicionando uma camada base open street maps
 */
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

/*
    Fazendo uma requisição para o geoserver, solicitando um JSON da feição
 */
$.ajax('http://localhost:8600/geoserver/mapas/ows', { // Link do geoserver
    type: 'GET', // Tipo de requisição
    data: {
        service: 'WFS', // Serviço do tipo Web Feature Server (WFS)
        version: '1.1.0', // Versão do WFS
        request: 'GetFeature', // Tipo de requisição para o servidor
        typename: 'mapas:BRA_BIOMAS', // Nome da Camada
        srsname: 'EPSG:4326', // Sistema de coordenada
        outputFormat: 'text/javascript', // Retornará um JSON
    },
    dataType: 'jsonp', // Json with Padding
    jsonpCallback: 'callback:adiciona_camada',
    jsonp: 'format_options'
});

/*
    Função para colorir baseado no nome da feição
 */
function colorir_Biomas(nome) {
    return nome === 'Amazônia'       ? '#20d43b' :
           nome === 'Caatinga'       ? '#ffe565' :
           nome === 'Cerrado'        ? '#eeaf00' :
           nome === 'Mata Atlântica' ? '#287800' :
           nome === 'Pampa'          ? '#81e6ff' :
           nome === 'Pantanal'       ? '#d6440a' :
                                       '#D0D0D0D0';
}

/*
    Assim que a requisição for terminada, chamará essa função para adicionar o mapa com os biomas
 */
function adiciona_camada(data) {
    var bioma = L.geoJson(data, {
        onEachFeature: function (feature, layer) {
            let popupContent = "<p>Olá! Sou o Bioma " +
                feature.properties.NOME + "!</p>";
            layer.bindPopup(popupContent);
        },
        style: function (feature) {
            return {
                fillColor: colorir_Biomas(feature.properties.NOME),
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 0.7
            };
        }
    }).addTo(map);
    map.fitBounds(bioma.getBounds());
}

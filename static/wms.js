var param = {
    name: '범죄주의구간(전체)',
    serverUrl: 'www.safemap.go.kr/openApiService/wms/getLayerData.do?apikey=[WV0LBMXE-WV0L-WV0L-WV0L-WV0LBMXEFR]',
    layername: 'A2SM_CRMNLHSPOT_TOT',
    styles: 'A2SM_CrmnlHspot_Tot_Tot'
};

var wmsLayer = new OpenLayers.Layer.WMS(
    param.name,
    param.serverUrl,
    {
        layers: '' + param.layername,
        styles: param.styles,
        format: 'image/png',
        exceptions: 'text/xml',
        transparent: true
    },
    {
        isBaseLayer: false
    }
);

var legendApiUrl = 'http://www.safemap.go.kr/legend/legendApiXml.do?apikey=[WV0LBMXE-WV0L-WV0L-WV0L-WV0LBMXEFR]&layer=A2SM_CRMNLHSPOT_TOT&style=A2SM_CrmnlHspot_Tot_Tot';

fetch(legendApiUrl)
    .then(response => response.text())
    .then(xmlText => {
        // Process the XML response (xmlText)
        console.log(xmlText);
    })
    .catch(error => {
        console.error('Error fetching legend API:', error);
    });

